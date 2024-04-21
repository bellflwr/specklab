from __future__ import annotations

from pygame import Color
from pygame.math import Vector2

from math import inf

from specklab.protocol import HasPos


# "Particle" is abbreveated to "ptc"
class Ptc:
    pos: Vector2
    vel: Vector2
    acc: Vector2

    color: Color

    def __init__(
        self,
        pos: Vector2 | None = None,
        vel: Vector2 | None = None,
        color: Color | None = None,
    ) -> None:
        if pos is None:
            pos = Vector2()
        if vel is None:
            vel = Vector2()
        if color is None:
            color = Color("white")

        self.pos = pos
        self.vel = vel
        self.acc = Vector2()
        self.color = color

    def update(self, dt: float) -> None:
        self.pos += self.vel * dt
        self.vel += self.acc * dt

        self.acc = Vector2()

    def distance_to(self, other: HasPos | Vector2):
        if not isinstance(other, Vector2):
            other = other.pos

        return self.pos.distance_to(other)

    def distance_squared_to(self, other: HasPos | Vector2):
        if not isinstance(other, Vector2):
            other = other.pos

        return self.pos.distance_squared_to(other)

    def inverse_distance_to(self, other: HasPos | Vector2) -> float:
        dist = self.distance_to(other)
        if dist == 0:
            return inf
        return 1 / dist

    def inverse_square_distance_to(self, other: HasPos | Vector2) -> float:
        dist = self.distance_squared_to(other)
        if dist == 0:
            return inf
        return 1 / dist
