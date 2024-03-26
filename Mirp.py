from random import choice

from Port import get_ports
from Vessel import Vessel
from constants import VESSEL_COLORS


class Mirp:
    def __init__(self, distances, starting_ports):
        self.ports = get_ports(distances)
        self.vessels = [Vessel(VESSEL_COLORS[i], self.ports[sp].x, self.ports[sp].y) for i, sp in enumerate(starting_ports)]

    def draw(self, win):
        for p in self.ports:
            p.draw(win)
        for v in self.vessels:
            v.draw(win)

    def step(self):
        for v in self.vessels:
            if v.target is None:
                target_port = choice(self.ports)
                v.set_target(target_port.x, target_port.y)
            v.move()
