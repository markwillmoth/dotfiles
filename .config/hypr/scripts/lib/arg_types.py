import argparse

from lib.monitor import get_focused_monitor, get_monitor_by_name
from lib.types.monitor import Monitor


def bounded_int(min_val: int, max_val: int):
    def check(value: str) -> int:
        int_value = int(value)
        if int_value < min_val or int_value > max_val:
            raise argparse.ArgumentTypeError(
                f"Value must be between {min_val} and {max_val}"
            )
        return int_value

    return check


def arg_monitor(monitor_name: str) -> Monitor:
    monitor = (
        get_focused_monitor()
        if monitor_name == "focused"
        else get_monitor_by_name(monitor_name)
    )
    if monitor is None:
        raise argparse.ArgumentTypeError(f"Monitor '{monitor_name}' not found")
    return monitor
