from argparse import ArgumentParser, Namespace

from lib.arg_types import bounded_int
from lib.monitor import get_focused_monitor
from lib.workspace import (
    get_next_workspace,
    get_prev_workspace,
    get_workspace_by_monitor,
    get_workspace_by_monitor_and_index,
)
from lib.command import run


def add_arguments(parser: ArgumentParser) -> None:
    monitor = get_focused_monitor()
    if not monitor:
        return

    workspaces = get_workspace_by_monitor(monitor)
    workspace_count = len(workspaces)

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument(
        "-w",
        "--workspace",
        type=bounded_int(1, workspace_count),
        help=f"change to workspace number (1–{workspace_count}) on focused monitor",
    )
    group.add_argument(
        "-n", "--next", action="store_true", help="change to next workspace"
    )
    group.add_argument(
        "-p", "--prev", action="store_true", help="change to previous workspace"
    )


def exec_cmd(args: Namespace) -> None:
    monitor = get_focused_monitor()
    if not monitor:
        return

    workspace = None

    if args.next:
        workspace = get_next_workspace(monitor)
    elif args.prev:
        workspace = get_prev_workspace(monitor)
    elif args.workspace:
        workspace = get_workspace_by_monitor_and_index(monitor, args.workspace)
    if workspace is None:
        return

    command = ["hyprctl", "dispatch", "workspace", str(workspace.id)]
    run(command)
