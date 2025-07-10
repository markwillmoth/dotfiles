from typing import List, TypeVar


def normalize_string(input_string: str) -> str:
    return input_string.lower().replace(" ", "").strip()


def normalize_match(a: str, b: str) -> bool:
    return normalize_string(a) == normalize_string(b)


def remove_dot_prefix(text: str) -> str:
    return text[1:] if text.startswith(".") else text


T = TypeVar("T")


def next_item(items: List[T], current_index: int) -> T:
    return items[next_index(items, current_index)]


def next_index(items: List[T], current_index: int) -> int:
    if not items:
        raise ValueError("List must not be empty")
    if current_index < 0 or current_index + 1 >= len(items):
        return 0
    return current_index + 1


def prev_item(items: List[T], current_index: int) -> T:
    return items[prev_index(items, current_index)]


def prev_index(items: List[T], current_index: int) -> int:
    if not items:
        raise ValueError("List must not be empty")
    if current_index <= 0 or current_index >= len(items):
        return len(items) - 1
    return current_index - 1
