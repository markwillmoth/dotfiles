from argparse import ArgumentParser, Namespace

from lib.client import get_all_clients, get_focused_client
from lib.command import run


def add_arguments(parser: ArgumentParser):

    group = parser.add_mutually_exclusive_group(required=True)

    group.add_argument("-t", "--tag", type=str, help="toggle tag on active client")
    group.add_argument("-l", "--list", action="store_true", help="list all clients")


def exec_cmd(args: Namespace):

    if args.tag:
        client = get_focused_client()
        if not client:
            return

        if args.tag in client.tags:
            run(
                ["hyprctl", "dispatch", "tagwindow", "--", f"-{args.tag}"],
            )
        else:
            run(["hyprctl", "dispatch", "tagwindow", args.tag])
    if args.list:
        clients = get_all_clients()
        for client in clients:
            print(f"{client}\n")
