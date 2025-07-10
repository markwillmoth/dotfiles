from dataclasses import dataclass
from typing import List, Tuple


@dataclass
class ClientWorkspace:
    id: int
    name: str


@dataclass
class Client:
    address: str
    mapped: bool
    hidden: bool
    at: Tuple[int, int]
    size: Tuple[int, int]
    workspace: ClientWorkspace
    floating: bool
    pseudo: bool
    monitor: int
    class_name: str  # Renamed from "class"
    title: str
    initial_class: str
    initial_title: str
    pid: int
    xwayland: bool
    pinned: bool
    fullscreen: int
    fullscreen_client: int
    grouped: List[str]
    tags: List[str]
    swallowing: str
    focus_history_id: int
    inhibiting_idle: bool
    xdg_tag: str
    xdg_description: str

    def __str__(self) -> str:
        info = [
            f"Address: {self.address}",
            f"Mapped: {self.mapped}",
            f"Hidden: {self.hidden}",
            f"Position: {self.at}",
            f"Size: {self.size}",
            f"Workspace: {self.workspace}",
            f"Floating: {self.floating}",
            f"Pseudo: {self.pseudo}",
            f"Monitor: {self.monitor}",
            f"Class: {self.class_name}",
            f"Title: {self.title}",
            f"Initial Class: {self.initial_class}",
            f"Initial Title: {self.initial_title}",
            f"PID: {self.pid}",
            f"XWayland: {self.xwayland}",
            f"Pinned: {self.pinned}",
            f"Fullscreen: {self.fullscreen}",
            f"Fullscreen Client: {self.fullscreen_client}",
            f"Grouped: {self.grouped}",
            f"Tags: {self.tags}",
            f"Swallowing: {self.swallowing}",
            f"Focus History ID: {self.focus_history_id}",
            f"Inhibiting Idle: {self.inhibiting_idle}",
            f"XDG Tag: {self.xdg_tag}",
            f"XDG Description: {self.xdg_description}",
        ]
        return "\n".join([f"  {line}" for line in info])
