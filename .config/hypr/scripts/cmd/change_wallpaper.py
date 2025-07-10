from argparse import ArgumentParser, Namespace

from lib.arg_types import arg_monitor
from lib.fuzzel import fuzzel
from lib.wallpaper import (
    find_wallpaper,
    get_next_wallpaper,
    get_wallpapers,
    set_wallpaper,
)


def add_arguments(parser: ArgumentParser):
    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-f", "--fuzzel", action="store_true", help="use fuzzel menu")
    group.add_argument(
        "-w", "--wallpaper", type=str, help="change using wallpaper name or path"
    )
    group.add_argument(
        "-n", "--next", action="store_true", help="change to next wallpaper"
    )

    parser.add_argument(
        "-m",
        "--monitor",
        type=arg_monitor,
        help="monitor to change wallpaper",
        required=True,
    )


def exec_cmd(args: Namespace):
    selected = None
    if args.next:
        selected = get_next_wallpaper(args.monitor)
    if args.wallpaper:
        selected = find_wallpaper(args.monitor, args.wallpaper)
    if args.fuzzel:
        wallpapers = get_wallpapers(args.monitor)
        selected = fuzzel(wallpapers, lambda x: x.name())

    set_wallpaper(args.monitor, selected)
