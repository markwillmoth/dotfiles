import json
from typing import Any, cast, Dict, List, Tuple

from lib.command import run
from lib.types.client import Client, ClientWorkspace


def get_all_clients() -> List[Client]:
    result, _ = run(["hyprctl", "clients", "-j"])
    clients = json.loads(result)
    return [_create_from_dict(c) for c in clients]


def get_focused_client() -> Client | None:
    clients = get_all_clients()
    for c in clients:
        if c.focus_history_id == 0:
            return c
    return None


def _create_from_dict(data: Dict[str, Any]) -> Client:
    workspace = ClientWorkspace(
        id=data["workspace"]["id"],
        name=data["workspace"]["name"],
    )

    return Client(
        address=data["address"],
        mapped=data["mapped"],
        hidden=data["hidden"],
        at=cast(Tuple[int, int], tuple(data["at"])),
        size=cast(Tuple[int, int], tuple(data["size"])),
        workspace=workspace,
        floating=data["floating"],
        pseudo=data["pseudo"],
        monitor=data["monitor"],
        class_name=data["class"],
        title=data["title"],
        initial_class=data["initialClass"],
        initial_title=data["initialTitle"],
        pid=data["pid"],
        xwayland=data["xwayland"],
        pinned=data["pinned"],
        fullscreen=data["fullscreen"],
        fullscreen_client=data["fullscreenClient"],
        grouped=data["grouped"],
        tags=data["tags"],
        swallowing=data["swallowing"],
        focus_history_id=data["focusHistoryID"],
        inhibiting_idle=data["inhibitingIdle"],
        xdg_tag=data["xdgTag"],
        xdg_description=data["xdgDescription"],
    )
