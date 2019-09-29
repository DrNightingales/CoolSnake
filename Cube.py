import pygame as pg

from GameObject import GameObject
from constants import *


class Cube(GameObject):
    """
    Cube GO for the, part of the snake
    """

    def __init__(self, surface, color, x, y, a):
        """
        Initiation function for the cube
        :param color: Color of the cube
        :param surface: Surface to be blit on
        :param x: x coordinate
        :param y: y coordinate
        :param a: size of the edge
        """
        super().__init__(surface, color, x, y)
        self.a = a * SF

    @property
    def rect(self):
        return pg.Rect((SF * 1.5 + self.x * CELL_SIZE, SF * 1.5 + self.y * CELL_SIZE), (self.a, self.a))

    def update(self, event_list):
        pg.draw.rect(self.surface, self.color, self.rect)

    def move(self, dx, dy):
        if self.x / SF + dx * SF >= 21:
            self.x = 0
        elif self.x / SF + dx * SF <= -2:
            self.x = 19 * SF
        else:
            self.x += dx * SF

        if self.y / SF + dy * SF >= 21:
            self.y = 0
        elif self.y / SF + dy * SF <= -2:
            self.y = 19 * SF
        else:
            self.y += dy * SF
