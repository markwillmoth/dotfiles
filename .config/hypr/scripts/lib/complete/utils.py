from typing import List, Optional

from lib.complete.types import Argument, Option, Value
from lib.monitor import get_focused_monitor, get_monitor_by_name
from lib.types.monitor import Monitor


def get_arg_value(arguments: List[Argument], option: Option) -> Value:
    for arg in arguments:
        if arg.option == option:
            return arg.value

    return None


def initial_filter(words: List[str]) -> List[str]:
    if "hyprcmd" in words:
        index = words.index("hyprcmd") + 1
        words = words[index:]
    return [w for w in words]


def get_value(words: List[str], option: Option, index: int) -> Value:
    if option.type == bool:
        return True

    next_word_index = index + 1
    next_word = words[next_word_index] if next_word_index < len(words) else None

    if not next_word:
        return None

    if option.type == int:
        return int(next_word)
    elif option.type == float:
        return float(next_word)
    elif option.type == str:
        return str(next_word)
    elif option.type == Monitor:
        return (
            get_focused_monitor()
            if next_word == "focused"
            else get_monitor_by_name(next_word)
        )

    return None


def parse_arguments(words: List[str], options: List[Option]) -> List[Argument]:
    res = []

    for i, w in enumerate(words):
        for o in options:
            if o.short == w or o.long == w:
                argument = Argument(o, get_value(words, o, i))
                res.append(argument)

    return res


def print_options(options: List[Option], exclude: Optional[List[Option]] = None):
    filtered = []

    for o in options:
        include = True
        if exclude:
            for e in exclude:
                if e == o:
                    include = False
                    break

        if include:
            filtered.append(o)

    for f in filtered:
        print(f.long)
