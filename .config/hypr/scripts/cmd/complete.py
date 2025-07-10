import argparse
from argparse import ArgumentParser, Namespace
from typing import List

import lib.wallpaper_playlist
from lib.complete.get_values import (
    get_wallpaper_values,
    monitor_select_values,
    range_values,
)
from lib.complete.types import Option
from lib.complete.utils import (
    get_arg_value,
    initial_filter,
    parse_arguments,
    print_options,
)
from lib.logger import logger
from lib.monitor import get_focused_monitor
from lib.types.monitor import Monitor
from lib.workspace import get_workspace_by_monitor


def add_arguments(parser: ArgumentParser) -> None:
    parser.add_argument("words", nargs=argparse.REMAINDER)


def exec_cmd(args: Namespace, commands: List[str]) -> None:
    words = initial_filter(args.words)
    logger.debug(f"words: {words}")

    if not words:
        print(*commands, sep="\n")
        return

    if len(words) == 1:
        suggestions = [c for c in commands if c.startswith(words[0]) and c != words[0]]
        if len(suggestions) > 0:
            print(*suggestions, sep="\n")
            return

    command = words[0]

    command_words = words[1:]
    logger.debug(f"command: {command}")
    logger.debug(f"command_words: {command_words}")

    func = globals().get(f"handle_{command}")
    logger.debug(f"func: {func}")

    if callable(func):
        func(command_words)
    else:
        logger.warning(f"no complete handler for command: {command}")


def handle_wallpaper_playlist(words: List[str]):
    opt_next = Option("-n", "--next", bool)
    opt_get = Option("-g", "--get-playlist", bool)
    opt_list = Option("-l", "--list", bool)
    opt_all = Option("-a", "--all", bool)
    opt_fuzzel = Option("-f", "--fuzzel", bool)
    opt_shuffle = Option("-S", "--shuffle", bool)
    opt_shuffle_daemon = Option("-d", "--shuffle-daemon", bool)

    opt_set = Option(
        "-s", "--set-playlist", str, get_values=lib.wallpaper_playlist.get_all_playlist_keys
    )

    options = [
        opt_next,
        opt_get,
        opt_list,
        opt_set,
        opt_all,
        opt_fuzzel,
        opt_shuffle,
        opt_shuffle_daemon,
    ]

    arguments = parse_arguments(words, options)

    if len(arguments) == 0:
        print_options(options, exclude=[opt_all])
        return

    last_argument = arguments[-1]

    if not last_argument.complete():
        last_argument.option.print_allowed_values()
        return

    if last_argument.option == opt_fuzzel or last_argument.option == opt_list:
        print_options([opt_all])


def handle_change_workspace(words: List[str]):
    monitor = get_focused_monitor()
    if not monitor:
        return

    workspaces = get_workspace_by_monitor(monitor)
    workspace_count = len(workspaces)

    logger.debug(f"workspace_count: {workspace_count}")

    opt_next = Option("-n", "--next", bool)
    opt_prev = Option("-p", "--prev", bool)
    opt_workspace = Option("-w", "--workspace", int, range_values(1, workspace_count))

    options = [opt_next, opt_prev, opt_workspace]

    arguments = parse_arguments(words, options)
    logger.debug(f"arguments: {arguments}")

    if len(arguments) == 0:
        print_options(options)
        return

    last_argument = arguments[-1]
    if not last_argument.complete():
        last_argument.option.print_allowed_values()
        return


def handle_client(words: List[str]):
    opt_tag = Option("-t", "--tag", str, allow_any=True)
    opt_list = Option("-l", "--list", bool)
    options = [opt_tag, opt_list]
    arguments = parse_arguments(words, options)
    if len(arguments) == 0:
        print_options(options)
        return


def handle_change_wallpaper(words: List[str]):
    opt_monitor = Option("-m", "--monitor", Monitor, get_values=monitor_select_values)
    options = [opt_monitor]

    arguments = parse_arguments(words, options)

    if len(arguments) == 0:
        print_options(options)
        return

    last_argument = arguments[-1]
    if not last_argument.complete():
        last_argument.option.print_allowed_values()
        return

    monitor = get_arg_value(arguments, opt_monitor)
    opt_next = Option("-n", "--next", bool)
    opt_wallpaper = Option(
        "-w", "--wallpaper", str, get_values=get_wallpaper_values(monitor)
    )
    options = [opt_next, opt_wallpaper]
    arguments = parse_arguments(words, options)

    if len(arguments) == 0:
        print_options(options)
        return

    last_argument = arguments[-1]
    if not last_argument.complete():
        last_argument.option.print_allowed_values()
        return
