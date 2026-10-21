from dataclasses import dataclass
import pygame as pg

@dataclass
class Ball:
    velocity: pg.Vector2
    rotation: float
    speed: float
    decceleration: float = 40.0
    strength: float = 1

@dataclass
class Arrow:
    rotation: float = 0

@dataclass
class InvBall:
    pass