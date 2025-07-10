from dataclasses import dataclass


@dataclass
class MonitorWorkspace:
    id: int
    name: str

    def __str__(self) -> str:
        return f"Workspace ID: {self.id}, Name: {self.name}"
