from pygame import Rect
from pygame.math import Vector2


def convert_space(orig: Vector2, from_: Rect, to: Rect):
    return Vector2(
        (orig.x - from_.left) / from_.width * to.width + to.left,
        (orig.y - from_.top) / from_.height * to.height + to.top,
    )
