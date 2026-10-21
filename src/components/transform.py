from dataclasses import dataclass

@dataclass
class Position:
    x: float = 0.0
    y: float = 0.0

@dataclass
class Rotation:
    r: float = 0.0

@dataclass
class Scale:
    x: float = 0.0
    y: float = 0.0
