import time
from argparse import ArgumentParser, Namespace

from lib.fuzzel import fuzzel
from lib.wallpaper import shuffle_wallpapers
from lib.wallpaper_playlist import (
    get_all_playlists,
    get_current_playlist,
    get_next_playlist,
    set_current_playlist,
)


def add_arguments(parser: ArgumentParser, required: bool = True):
    group = parser.add_mutually_exclusive_group(required=required)

    group.add_argument(
        "-g", "--get-playlist", action="store_true", help="get current playlist"
    )
    group.add_argument("-s", "--set-playlist", type=str, help="set playlist")
    group.add_argument(
        "-n", "--next", action="store_true", help="change to next playlist"
    )
    group.add_argument("-l", "--list", action="store_true", help="list playlists")
    group.add_argument("-f", "--fuzzel", action="store_true", help="use fuzzel menu")
    group.add_argument(
        "-S", "--shuffle", action="store_true", help="shuffle wallpapers"
    )

    group.add_argument(
        "-d",
        "--shuffle-daemon",
        type=int,
        help="shuffle wallpapers at interval specified (seconds)",
        default=60,
    )

    parser.add_argument(
        "-a", "--all", action="store_true", help="show all playlists including hidden"
    )


def exec_cmd(args: Namespace):
    if args.get_playlist:
        current = get_current_playlist()
        print(current.key if current else "")

    elif args.set_playlist:
        set_current_playlist(args.set_playlist)
        shuffle_wallpapers()

    elif args.next:
        set_current_playlist(get_next_playlist())
        shuffle_wallpapers()

    elif args.list:
        for p in get_all_playlists(include_hidden=args.all):
            print(p.key)

    elif args.fuzzel:
        playlists = get_all_playlists(include_hidden=args.all)
        selected = fuzzel(playlists, lambda x: x.name)
        if not selected:
            return
        set_current_playlist(selected)
        shuffle_wallpapers()
    elif args.shuffle:
        shuffle_wallpapers()
    elif args.shuffle_daemon:
        while True:
            shuffle_wallpapers()
            time.sleep(args.shuffle_daemon)
