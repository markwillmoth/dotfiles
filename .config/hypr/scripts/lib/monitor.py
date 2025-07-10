import json
from typing import List, Dict, Any, Optional

from lib.command import run
from lib.types.monitor import Monitor
from lib.types.monitor_workspace import MonitorWorkspace
from lib.util import normalize_match


def _create_monitor_from_dict(data: Dict[str, Any]) -> Monitor:

    active_workspace = MonitorWorkspace(
        id=data["activeWorkspace"]["id"],
        name=data["activeWorkspace"]["name"],
    )

    special_workspace = MonitorWorkspace(
        id=data["specialWorkspace"]["id"],
        name=data["specialWorkspace"]["name"],
    )

    return Monitor(
        id=data["id"],
        name=data["name"],
        description=data["description"],
        make=data["make"],
        model=data["model"],
        serial=data["serial"],
        width=data["width"],
        height=data["height"],
        refreshRate=data["refreshRate"],
        x=data["x"],
        y=data["y"],
        activeWorkspace=active_workspace,
        specialWorkspace=special_workspace,
        reserved=data["reserved"],
        scale=data["scale"],
        transform=data["transform"],
        focused=data["focused"],
        dpmsStatus=data["dpmsStatus"],
        vrr=data["vrr"],
        solitary=data["solitary"],
        activelyTearing=data["activelyTearing"],
        directScanoutTo=data["directScanoutTo"],
        disabled=data["disabled"],
        currentFormat=data["currentFormat"],
        mirrorOf=data["mirrorOf"],
        availableModes=data["availableModes"],
    )


def _get_monitors_json() -> str:
    command = ["hyprctl", "monitors", "-j"]
    result, _ = run(command)
    return result


def get_all_monitors() -> List[Monitor]:
    monitors_json = _get_monitors_json()
    monitor_dicts = json.loads(monitors_json)
    monitors = list(map(_create_monitor_from_dict, monitor_dicts))
    monitors.sort(key=lambda m: m.id)
    return monitors


def get_monitor_by_name(name: str) -> Optional[Monitor]:
    for m in get_all_monitors():
        if normalize_match(m.name, name):
            return m
    return None


def get_focused_monitor() -> Optional[Monitor]:
    for m in get_all_monitors():
        if m.focused:
            return m
    return None


def get_monitor_by_resolution(resolution: str) -> List[Monitor]:
    return [m for m in get_all_monitors() if m.transform_resolution() == resolution]
