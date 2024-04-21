import pygame

pygame.init()
pygame.font.init()

from . import app  # noqa: E402

__all__ = ("app",)
