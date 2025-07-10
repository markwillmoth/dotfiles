from typing import List, Optional

from lib.complete.types import GetValuesFunc
from lib.monitor import get_all_monitors
from lib.types.monitor import Monitor
from lib.wallpaper import get_wallpapers


def get_wallpaper_values(monitor: Optional[Monitor]) -> GetValuesFunc:
    def func() -> List[str]:
        if not monitor:
            return []
        return [w.name() for w in get_wallpapers(monitor)]

    return func


def monitor_select_values():
    monitors = get_all_monitors()
    return ["focused"] + [m.name for m in monitors]


def range_values(min_val: int, max_val: int) -> GetValuesFunc:
    def range_func() -> List[str]:
        return [str(i) for i in range(min_val, max_val + 1)]

    return range_func
