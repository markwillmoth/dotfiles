from typing import Callable, List, Optional, TypeVar

from lib.command import run

T = TypeVar("T")


def fuzzel(
    items: List[T], get_label: Optional[Callable[[T], str]] = None
) -> Optional[T]:
    if not get_label:

        def get_label(item):
            return str(item)

    labels = [get_label(i) for i in items]
    lookup = {get_label(i): i for i in items}

    choice, _ = run(
        ["fuzzel", "--dmenu"],
        input="\n".join(labels),
    )

    if not choice:
        return None

    selected = lookup.get(choice)
    return selected if selected else None
