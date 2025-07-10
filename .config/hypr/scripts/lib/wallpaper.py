import fnmatch
import os
import random
from pathlib import Path
from time import sleep
from typing import List, Optional

from psutil import boot_time

from lib.command import run
from lib.constants import ALLOWED_WALLPAPER_EXTENSIONS, WALLPAPER_DIR
from lib.logger import logger
from lib.monitor import get_all_monitors, get_monitor_by_resolution
from lib.types.active_wallpaper import ActiveWallpaper
from lib.types.monitor import Monitor
from lib.types.wallpaper import Wallpaper
from lib.types.wallpaper_playlist import WallpaperPlaylist
from lib.wallpaper_playlist import get_current_playlist


def _get_image_files_in_dir(dir: Path) -> List[str]:
    files_in_dir = sorted(os.listdir(dir))

    image_files = []
    for ext in ALLOWED_WALLPAPER_EXTENSIONS:
        image_files.extend(fnmatch.filter(files_in_dir, ext))

    return image_files


def _files_to_wallpapers(
    file_names: List[str], dir: str | Path, resolution: str, skip_dotfiles: bool = True
) -> List[Wallpaper]:
    return [
        Wallpaper(path=os.path.join(dir, f), filename=f, resolution=resolution)
        for f in file_names
        if not f.startswith(".") or not skip_dotfiles
    ]


def _filter_wallpapers_with_playlist(
    playlist: WallpaperPlaylist, monitor: Monitor, wallpapers: List[Wallpaper]
) -> List[Wallpaper]:
    allowed = playlist.get_files_for_monitor(monitor)
    if not allowed:
        return []

    filtered = []

    for w in wallpapers:
        for a in allowed:
            if w.matches(a):
                filtered.append(w)

    return filtered


def get_wallpapers(
    monitor: Monitor, playlist: Optional[WallpaperPlaylist] = None
) -> List[Wallpaper]:
    resolution = monitor.transform_resolution()
    image_dir = WALLPAPER_DIR / resolution
    image_files = _get_image_files_in_dir(image_dir)

    wallpapers = _files_to_wallpapers(
        image_files,
        image_dir,
        resolution,
        skip_dotfiles=not playlist,
    )

    if not playlist:
        return wallpapers

    return _filter_wallpapers_with_playlist(playlist, monitor, wallpapers)


def _get_active() -> List[ActiveWallpaper]:
    result, _ = run(["hyprctl", "hyprpaper", "listactive"])

    if not result:
        return []

    return [
        ActiveWallpaper(monitor=monitor.strip(), path=path.strip())
        for line in result.splitlines()
        if "=" in line
        for monitor, path in [line.split("=", 1)]
    ]


def _get_active_for_resolution(resolution: str) -> List[ActiveWallpaper]:
    monitors = get_monitor_by_resolution(resolution)
    monitor_names = {m.name for m in monitors}
    active = _get_active()

    return [a for a in active if a.monitor in monitor_names]


def _get_active_for_monitor(monitor: Monitor) -> Optional[ActiveWallpaper]:
    active = _get_active()
    for a in active:
        if a.monitor == monitor.name:
            return a
    return None


def get_next_wallpaper(monitor: Monitor) -> Optional[Wallpaper]:
    resolution = monitor.transform_resolution()
    playlist = get_current_playlist()
    available = get_wallpapers(monitor, playlist)

    if not available:
        return None

    random.seed(int(boot_time()))
    random.shuffle(available)

    active = _get_active_for_resolution(resolution)
    active_paths = [a.path for a in active]
    prev_file = _get_prev(resolution)

    start_index = 0
    if prev_file is not None:
        for i, a in enumerate(available):
            if a.path == prev_file:
                start_index = (i + 1) % len(available)
                break

    n = len(available)
    for offset in range(n):
        idx = (start_index + offset) % n
        candidate = available[idx]
        if candidate.path not in active_paths:
            return candidate

    candidate = available[start_index]
    return candidate


def _prev_path(resolution: str) -> Path:
    return Path.home() / ".cache" / f"prev_wallpaper_{resolution}"


def _get_prev(resolution: str) -> Optional[str]:
    prev_file = _prev_path(resolution)
    if not prev_file.is_file():
        return None
    content = prev_file.read_text(encoding="utf-8").strip()
    return content if content else None


def _set_prev(resolution: str, path: str):
    file = _prev_path(resolution)
    file.write_text(path, encoding="utf-8")


def _is_currently_active(monitor: Monitor, wallpaper: Wallpaper) -> bool:
    active = _get_active_for_monitor(monitor)
    if active and active.path == wallpaper.path:
        return True
    return False


def set_wallpaper(monitor: Monitor, wallpaper: Optional[Wallpaper]):
    if not wallpaper:
        logger.info("no wallpaper provided")
        return

    if _is_currently_active(monitor, wallpaper):
        logger.info(f"wallpaper {wallpaper} already active")
        return

    _set_prev(monitor.transform_resolution(), wallpaper.path)

    command = ["hyprctl", "hyprpaper", "reload", f"{monitor.name},", wallpaper.path]
    run(command)


def find_wallpaper(monitor: Monitor, query: str) -> Optional[Wallpaper]:
    available = get_wallpapers(monitor)

    for item in available:
        if item.matches(query):
            return item

    logger.warning(
        f'Wallpaper "{query}" not found for monitor "{
            monitor.label()}"'
    )
    return None


def shuffle_wallpapers(interval: float = 0):
    logger.info("shuffling wallpapers")
    for m in get_all_monitors():
        selected = get_next_wallpaper(m)
        set_wallpaper(m, selected)
        sleep(interval)
