import pygame as pg

from Cube import Cube
from constants import *


class Snake:
    """
    Snake Object, which unifies and manages it's cubes
    """

    def __init__(self, surface):
        self.surface = surface
        self.head = Cube(self.surface, NEON_YELLOW, 10, 10, 28)
        self.body = [self.head]
        self.d_vector = (0, 0)
        self.impedance = IMPEDANCE

    def update(self, event_list):
        if self.impedance > 0:
            self.impedance -= 1
        else:
            self.impedance = IMPEDANCE
            self.register_key()
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            self.head.move(*self.d_vector)

        for cube in self.body:
            cube.update(event_list)

        if self.head.pos in [c.pos for c in self.body[1:]]:
            pg.quit()

    def register_key(self):
        keys = pg.key.get_pressed()
        if keys[pg.K_LEFT] and not (self.d_vector == (1, 0) and len(self.body) != 1):
            self.d_vector = (-1, 0)
        if keys[pg.K_RIGHT] and not (self.d_vector == (-1, 0) and len(self.body) != 1):
            self.d_vector = (1, 0)
        if keys[pg.K_UP] and not (self.d_vector == (0, 1) and len(self.body) != 1):
            self.d_vector = (0, -1)
        if keys[pg.K_DOWN] and not (self.d_vector == (0, -1) and len(self.body) != 1):
            self.d_vector = (0, 1)

    def extend(self):
        self.body.insert(1, Cube(self.surface, NEON_YELLOW, self.head.x / 2, self.head.y / 2, 28))
        self.head.move(*self.d_vector)
