from typing import Callable, List, Optional, Type, Union

from lib.types.monitor import Monitor

Value = Union[str, int, float, bool, Monitor, None]
GetValuesFunc = Optional[Callable[[], List[str]]]


class Option:
    short: str
    long: str
    type: Type
    get_values: GetValuesFunc
    allow_any: bool

    def __init__(
        self,
        short: str,
        long: str,
        type: Type,
        get_values: GetValuesFunc = None,
        allow_any: bool = False,
    ):
        self.short = short
        self.long = long
        self.type = type
        self.get_values = get_values
        self.allow_any = allow_any

    def __eq__(self, other) -> bool:
        return (
            self.short == other.short
            and self.long == self.long
            and self.type == self.type
        )

    def __repr__(self) -> str:
        return f"Option(short={
            self.short} long={
            self.long} type={type} allowed_values={
            self.get_values()})"

    def __str__(self) -> str:
        return self.__repr__()

    def allowed_values(self) -> Optional[List[str]]:
        if not self.get_values and not callable(self.get_values):
            return None
        return self.get_values()

    def print_allowed_values(self):
        values = self.allowed_values()
        print(*values, sep="\n")


class Argument:
    option: Option
    value: Value

    def __init__(self, option: Option, value: Value):
        self.option = option
        self.value = value

    def __repr__(self) -> str:
        return f"Argument(option={self.option} value={self.value})"

    def __str__(self) -> str:
        return self.__repr__()

    def complete(self) -> bool:
        if self.option.type == bool:
            return True

        if not callable(self.option.get_values):
            return True

        if self.option.type == str and self.option.allow_any:
            if self.value:
                return True

        if self.option.type == Monitor and self.value:
            return True

        allowed_values = self.option.get_values()

        for v in allowed_values:
            if self.value == v:
                return True
        return False
