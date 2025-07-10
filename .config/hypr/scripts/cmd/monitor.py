from argparse import Namespace, ArgumentParser
from typing import List, Union

from lib.monitor import get_monitor_by_name, get_all_monitors, get_focused_monitor
from lib.types.monitor import Monitor


def add_arguments(parser: ArgumentParser) -> None:
    parser.add_argument(
        "-d",
        "--detailed",
        action="store_true",
        help="output detailed info of monitor/s",
    )

    group = parser.add_mutually_exclusive_group(required=True)
    group.add_argument("-m", "--monitor", help="get monitor by name")
    group.add_argument(
        "-f", "--focused", action="store_true", help="get focused monitor"
    )
    group.add_argument("-a", "--all", action="store_true", help="get all monitors")


def output(monitor: Union[List[Monitor], Monitor, None], detailed: bool) -> None:
    if not monitor:
        print("monitor not found")
        return

    monitors = monitor if isinstance(monitor, list) else [monitor]

    lines = [
        m.details() if detailed else f"{m.name}:{m.transform_resolution()}"
        for m in monitors
    ]
    print(*lines, sep="\n")


def exec_cmd(args: Namespace) -> None:
    if args.all:
        monitor = get_all_monitors()
    elif args.monitor:
        monitor = get_monitor_by_name(args.monitor)
    elif args.focused:
        monitor = get_focused_monitor()
    else:
        monitor = None

    output(monitor, detailed=args.detailed)
