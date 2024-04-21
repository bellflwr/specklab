from typing import Protocol, runtime_checkable
from pygame.math import Vector2


@runtime_checkable
class HasPos(Protocol):
    pos: Vector2
