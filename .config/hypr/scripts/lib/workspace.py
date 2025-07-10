import json
from typing import Any, Dict, List, Optional

from lib.command import run
from lib.types.monitor import Monitor
from lib.types.workspace import Workspace
from lib.util import next_item, prev_item


def _get_workspaces_json() -> str:
    result, _ = run(["hyprctl", "workspaces", "-j"])
    return result


def _create_from_dict(data: Dict[str, Any]) -> Workspace:
    return Workspace(
        id=data["id"],
        name=data["name"],
        monitor=data["monitor"],
        monitor_id=data["monitorID"],
        windows=data["windows"],
        has_fullscreen=data["hasfullscreen"],
        last_window=data["lastwindow"],
        last_window_title=data["lastwindowtitle"],
        is_persistent=data["ispersistent"],
    )


def get_all_workspaces() -> List[Workspace]:
    workspaces_json = _get_workspaces_json()
    workspaces_dicts = json.loads(workspaces_json)
    return sorted([_create_from_dict(w) for w in workspaces_dicts], key=lambda x: x.id)


def get_workspace_by_monitor(monitor: Monitor) -> List[Workspace]:
    return [w for w in get_all_workspaces() if w.monitor_id == monitor.id]


def get_workspace_by_monitor_and_index(
    monitor: Monitor, index: int, start_at_one: bool = True
) -> Optional[Workspace]:
    if start_at_one:
        index = index - 1
    workspaces = get_workspace_by_monitor(monitor)
    return workspaces[index] if len(workspaces) > index else None


def _get_current_index(monitor: Monitor) -> int:
    workspaces = get_workspace_by_monitor(monitor)
    for i, workspace in enumerate(workspaces):
        if workspace.id == monitor.activeWorkspace.id:
            return i

    return 0


def get_next_workspace(monitor: Monitor) -> Workspace:
    return next_item(get_workspace_by_monitor(monitor), _get_current_index(monitor))


def get_prev_workspace(monitor: Monitor) -> Workspace:
    return prev_item(get_workspace_by_monitor(monitor), _get_current_index(monitor))
