#!/usr/bin/env python3

import argparse
import importlib
import os

from lib.logger import logger


def main():
    parser = argparse.ArgumentParser(prog="hyprcmd")
    subparsers = parser.add_subparsers(dest="command", required=True)

    cmd_dir = os.path.join(os.path.dirname(__file__), "cmd")
    commands = []

    modules = {}

    for filename in os.listdir(cmd_dir):
        if filename.endswith(".py") and filename != "__init__.py":
            cmd_name = filename[:-3]
            commands.append(cmd_name)
            module = importlib.import_module(f"cmd.{cmd_name}")
            modules[cmd_name] = module
            subparser = subparsers.add_parser(cmd_name)
            if hasattr(module, "add_arguments"):
                module.add_arguments(subparser)

    args = parser.parse_args()

    module = modules[args.command]
    try:
        if args.command == "list" or args.command == "complete":
            module.exec_cmd(args, commands=commands)
        else:
            module.exec_cmd(args)
    except KeyboardInterrupt:
        logger.info("exiting")
    except Exception as ex:
        logger.error(f"error: {ex}")


if __name__ == "__main__":
    main()
