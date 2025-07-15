import tomllib
from typing import List, Optional

from lib.constants import WALLPAPER_CURRENT_PLAYLIST_PATH, WALLPAPER_PLAYLIST_PATH
from lib.logger import logger
from lib.types.wallpaper_playlist import WallpaperPlaylist
from lib.util import next_item

file = WALLPAPER_CURRENT_PLAYLIST_PATH


def get_current_playlist() -> WallpaperPlaylist | None:
    if not file.is_file():
        return None

    key = file.read_text(encoding="utf-8").strip().lower()

    if key == "all":
        return None

    for playlist in get_all_playlists(include_hidden=True):
        if playlist.key == key:
            return playlist

    return None


def get_playlist(key: str) -> Optional[WallpaperPlaylist]:
    for p in get_all_playlists():
        if p.key == key:
            return p
    return None


def set_current_playlist(playlist: str | WallpaperPlaylist) -> None:
    if isinstance(playlist, WallpaperPlaylist):
        playlist = playlist.key

    logger.info(f"setting current playlist to {playlist}")
    file.write_text(playlist, encoding="utf-8")


def get_next_playlist(include_hidden: bool = False) -> WallpaperPlaylist:
    playlists = get_all_playlists(include_hidden)
    return next_item(playlists, playlists.index(get_current_playlist()))


def get_all_playlists(include_hidden: bool = False) -> List[WallpaperPlaylist] | None:
    path = WALLPAPER_PLAYLIST_PATH
    with path.open("rb") as f:
        data = tomllib.load(f)
        playlists = [WallpaperPlaylist(key, data[key]) for key in data]
        return [p for p in playlists if include_hidden or not p.hidden]


def get_all_playlist_keys() -> List[str]:
    path = WALLPAPER_PLAYLIST_PATH
    with path.open("rb") as f:
        data = tomllib.load(f)

    res = []
    for key in data:
        res.append(key)

    return res
