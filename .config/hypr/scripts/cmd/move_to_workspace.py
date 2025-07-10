from argparse import ArgumentParser, Namespace

from lib.arg_types import bounded_int
from lib.command import run
from lib.monitor import get_focused_monitor
from lib.workspace import get_workspace_by_monitor, get_workspace_by_monitor_and_index


def add_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-s",
        "--silent",
        action="store_true",
        help="move focused client without changing current workspace",
    )

    help_text = "move focused client to workspace on focused monitor."
    monitor = get_focused_monitor()
    max_value = None
    if monitor is not None:
        workspaces = get_workspace_by_monitor(monitor)
        max_value = len(workspaces)
        help_text = f"move focused client to workspace number (1–{max_value}) on focused monitor"

    parser.add_argument(
        "-w",
        "--workspace",
        type=bounded_int(1, max_value) if max_value else int,
        required=True,
        help=help_text,
    )


def exec_cmd(args: Namespace) -> None:
    monitor = get_focused_monitor()
    if not monitor:
        return

    workspace = get_workspace_by_monitor_and_index(monitor, args.workspace)
    if not workspace:
        return

    dispatcher = "movetoworkspacesilent" if args.silent else "movetoworkspace"
    command = ["hyprctl", "dispatch", dispatcher, str(workspace.id)]

    run(command)
