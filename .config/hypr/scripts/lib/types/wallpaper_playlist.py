import re
from typing import Dict, List

from lib.types.monitor import Monitor


class WallpaperResolutionSet:
    resolution: str
    monitor: str | None
    files: List[str]

    def __init__(self, resolution: str, monitor: str, files: List[str]) -> None:
        self.resolution = resolution
        self.monitor = monitor
        self.files = files

    def __repr__(self) -> str:
        return f"WallpaperResolutionSet(resolution={
            self.resolution} monitor={
            self.monitor} files={
            self.files})"


pattern = re.compile(r"^\d+x\d+(?:_[A-Za-z0-9-]+)?$")


class WallpaperPlaylist:
    key: str
    name: str
    hidden: bool
    sets: List[WallpaperResolutionSet]

    def __repr__(self) -> str:
        return f"WallpaperPlaylist(key={
            self.key} name={
            self.name} hidden={
            self.hidden} sets={
                self.sets})"

    def __str__(self) -> str:
        return self.__repr__()

    def __eq__(self, other) -> bool:
        return self.key == other.key

    def __init__(self, key: str, data: Dict[str, any]):
        self.key = key
        self.name = data["name"] if "name" in data else key
        self.hidden = bool(data["hidden"] if "hidden" in data else False)

        matching_keys = [key for key in data.keys() if pattern.match(key)]

        sets = []

        for key in matching_keys:
            parts = key.split("_")
            resolution = parts[0]
            monitor = parts[1] if len(parts) > 1 else None
            sets.append(WallpaperResolutionSet(resolution, monitor, data[key]))

        self.sets = sets

    def get_files_for_monitor(self, monitor: Monitor) -> List[str]:
        items = []
        for s in self.sets:
            if s.resolution == monitor.transform_resolution() and (
                s.monitor is None or s.monitor == monitor.name
            ):
                items += s.files
        return items
