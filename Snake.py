from sys import exit

import pygame as pg

from Cube import Cube
from constants import *


class Snake:
    """
    Snake Object, which unifies and manages it's cubes
    SO is a manager class, rather than a GO class
    """

    def __init__(self, surface):
        """
        Initialization method for the snake
        :param surface: Surface for cubes to be drawn on
        """
        self.surface = surface
        self.head = Cube(self.surface, NEON_YELLOW, 10, 10, 28)
        self.body = [self.head]
        self.d_vector = (0, 0)  # direction vector
        self.impedance = IMPEDANCE  # Impedance before moving the object

    def update(self, event_list):
        """
        Updates each cube in the snake's body
        :param event_list: list of events sent by host screen
        """
        # Movement allowed only after some delay
        if self.impedance > 0:
            self.impedance -= 1
        else:
            self.impedance = IMPEDANCE
            self.register_key()

            # Each cube is moved to the position of a previous one
            for i in range(len(self.body) - 1, 0, -1):
                self.body[i].x = self.body[i - 1].x
                self.body[i].y = self.body[i - 1].y
            # Head is moved by the vector
            self.head.move(*self.d_vector)

        for cube in self.body:
            cube.update(event_list)

        # Collision detection
        if self.head.pos in [c.pos for c in self.body[1:]]:
            pg.quit()
            exit()

    def register_key(self):
        """
        Method for registration of current pressed keys and changing the vector of direction for the snake
        :return:
        """
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
        """
        Method, which extends snake by 1 cube
        :return:
        """
        self.body.insert(1, Cube(self.surface, NEON_YELLOW, self.head.x / 2, self.head.y / 2, 28))
        self.head.move(*self.d_vector)
