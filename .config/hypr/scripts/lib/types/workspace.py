from dataclasses import dataclass


@dataclass
class Workspace:
    id: int
    name: str
    monitor: str
    monitor_id: int
    windows: int
    has_fullscreen: bool
    last_window: str
    last_window_title: str
    is_persistent: str

    def __eq__(self, other) -> bool:
        return isinstance(other, Workspace) and self.id == other.id

    def __str__(self) -> str:
        # Create a string representation of the Workspace object
        workspace_info = [
            f"Workspace ID: {self.id}",
            f"Name: {self.name}",
            f"Monitor: {self.monitor}",
            f"Monitor ID: {self.monitor_id}",
            f"Windows: {self.windows}",
            f"Has Fullscreen: {self.has_fullscreen}",
            f"Last Window: {self.last_window}",
            f"Last Window Title: {self.last_window_title}",
            f"Is Persistent: {self.is_persistent}",
        ]

        # Return the formatted string with indentation for each line
        return "\n".join([f"  {line}" for line in workspace_info])
