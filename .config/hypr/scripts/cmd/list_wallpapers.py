from argparse import ArgumentParser, Namespace

from lib.monitor import get_monitor_by_name
from lib.wallpaper import get_wallpapers
from lib.wallpaper_playlist import get_playlist


def add_arguments(parser: ArgumentParser):
    parser.add_argument(
        "-m", "--monitor", type=str, help="Name of monitor.", required=True
    )

    parser.add_argument(
        "-p",
        "--playlist",
        type=str,
        help="filter to playlist",
    )


def exec_cmd(args: Namespace):

    monitor = get_monitor_by_name(args.monitor)
    if not monitor:
        print(f'Monitor "{args.monitor}" not found')
        return

    playlist_key = args.playlist
    playlist = get_playlist(playlist_key) if playlist_key else None

    wallpapers = get_wallpapers(monitor, playlist)

    print(*(w.name() for w in wallpapers), sep="\n")
