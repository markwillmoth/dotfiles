from argparse import Namespace
from typing import List


def exec_cmd(_: Namespace, commands: List[str]):
    commands = sorted([c for c in commands if c != "complete"])
    print(*commands, sep="\n")
