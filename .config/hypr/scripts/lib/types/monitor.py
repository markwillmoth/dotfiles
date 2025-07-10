from dataclasses import dataclass
from typing import List
from lib.types.monitor_workspace import MonitorWorkspace


@dataclass
class Monitor:
    id: int
    name: str
    description: str
    make: str
    model: str
    serial: str
    width: int
    height: int
    refreshRate: float
    x: int
    y: int
    activeWorkspace: MonitorWorkspace
    specialWorkspace: MonitorWorkspace
    reserved: List[int]
    scale: float
    transform: int
    focused: bool
    dpmsStatus: bool
    vrr: bool
    solitary: str
    activelyTearing: bool
    directScanoutTo: str
    disabled: bool
    currentFormat: str
    mirrorOf: str
    availableModes: List[str]

    def resolution(self) -> str:
        return f"{self.width}x{self.height}"

    def transform_resolution(self) -> str:
        if self.transform == 0 or self.transform == 2:
            return self.resolution()
        return f"{self.height}x{self.width}"

    def label(self) -> str:
        return f"{self.name}:{self.transform_resolution()}"

    def __repr__(self) -> str:
        return f"Monitor(id={
            self.id}, name={
            self.name}, description={
            self.description}, resolution={
                self.transform_resolution()}, position={
                    self.x}, {
                        self.y})"

    def __str__(self) -> str:
        return self.__repr__()

    def details(self) -> str:
        # Create a string representation of the Monitor object with indentation
        monitor_info = [
            f"Monitor ID: {self.id}",
            f"Name: {self.name}",
            f"Description: {self.description}",
            f"Make: {self.make}",
            f"Model: {self.model}",
            f"Serial: {self.serial}",
            f"Resolution: {self.resolution()}",
            f"Transform Resolution: {self.transform_resolution()}",
            f"Refresh Rate: {self.refreshRate}Hz",
            f"Position: ({self.x}, {self.y})",
            f"Scale: {self.scale}",
            f"Transform: {self.transform}",
            f"Focused: {self.focused}",
            f"Reserved: {self.reserved}",
            f"DPMS Status: {self.dpmsStatus}",
            f"VRR: {self.vrr}",
            f"Solitary: {self.solitary}",
            f"Actively Tearing: {self.activelyTearing}",
            f"Direct Scanout To: {self.directScanoutTo}",
            f"Disabled: {self.disabled}",
            f"Current Format: {self.currentFormat}",
            f"Mirror Of: {self.mirrorOf}",
            f"Available Modes: {', '.join(self.availableModes)}",
            f"Active Workspace: {self.activeWorkspace}",
            f"Special Workspace: {self.specialWorkspace}",
        ]

        # Return the formatted string with indentation for each line
        return "\n".join([f"  {line}" for line in monitor_info])
