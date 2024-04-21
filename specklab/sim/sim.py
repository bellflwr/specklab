from specklab.sim.particle import Ptc
from pygame import Rect


class Sim:
    sim_space: Rect
    ptcs: list[Ptc]

    def __init__(self, sim_space: Rect | tuple[int, int]):
        if isinstance(sim_space, tuple):
            sim_space = Rect(0, 0, *sim_space)
        self.sim_space = sim_space

        self.ptcs = []

    def update(self, dt: float) -> None:
        pass
