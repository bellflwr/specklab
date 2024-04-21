import pygame
from pygame import Surface
from pygame.time import Clock

from specklab.sim import Sim
from specklab.render import render_basic

font = pygame.font.Font(None, 30)


class App:
    screen: Surface
    clock: Clock

    running: bool

    screen_size: tuple[int, int]
    screen_w: int
    screen_h: int

    screen_refresh: int

    sim: Sim

    def __init__(self, screen_size: tuple[int, int], screen_refresh: int):
        self.screen_size = self.screen_w, self.screen_h = screen_size
        self.screen_refresh = screen_refresh

        self.screen = pygame.display.set_mode(screen_size)
        self.clock = Clock()
        self.running = False

        self.sim = Sim((100, 100))

    def start(self) -> None:
        self.running = True

        dt = self.clock.get_time() / 1000.0

        while self.running:
            self.update(dt)

            dt = self.clock.tick(self.screen_refresh)

        pygame.quit()

    def update(self, dt: float) -> None:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                return

        self.sim.update(dt)

        self.render(dt)
        pygame.display.flip()

    def render(self, dt: float) -> None:
        self.screen.fill((0, 0, 0))

        render_basic(self.screen, self.sim)

        fps = str(round(self.clock.get_fps()))

        fps_surf = font.render(fps, True, "white")
        self.screen.blit(fps_surf, (10, 10))


def start(screen_size: tuple[int, int], screen_refresh: int):
    app = App(screen_size, screen_refresh)
    app.start()
