import pygame
from pygame import Surface

from specklab.mathutil import convert_space
from specklab.sim import Sim


def render_basic(surf: Surface, sim: Sim):
    for ptc in sim.ptcs:
        screen_pos = convert_space(ptc.pos, sim.sim_space, surf.get_rect())

        pygame.draw.circle(surf, ptc.color, screen_pos, 5)
