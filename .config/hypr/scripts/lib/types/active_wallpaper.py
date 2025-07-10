import os
from dataclasses import dataclass


@dataclass
class ActiveWallpaper:
    monitor: str
    path: str

    def name(self):
        return os.path.basename(self.path)

    def __str__(self) -> str:
        workspace_info = [
            f"Monitor: {self.monitor}",
            f"Path: {self.path}",
            f"Name: {self.name()}",
        ]

        return "\n".join([f"  {line}" for line in workspace_info])
