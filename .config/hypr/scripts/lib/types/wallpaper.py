import os
import fnmatch

from dataclasses import dataclass

from lib.util import remove_dot_prefix


@dataclass
class Wallpaper:
    path: str
    filename: str
    resolution: str

    def name(self) -> str:
        name = os.path.splitext(self.filename)[0]
        return name

    def matches(self, query: str) -> bool:
        q = _normalize(query)
        name = _normalize(os.path.splitext(self.filename)[0])
        filename = self.filename.lower()
        path = self.path.lower()

        return (
            fnmatch.fnmatch(name, q)
            or fnmatch.fnmatch(filename, q)
            or fnmatch.fnmatch(path, q)
        )


def _normalize(text: str) -> str:
    return remove_dot_prefix(text).lower()
