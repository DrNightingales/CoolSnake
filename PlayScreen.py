from random import randint as ri

import pygame as pg

from GameScreen import GameScreen
from constants import *


class PlayScreen(GameScreen):
    def __init__(self):
        super().__init__()
        self.cell_size = CELL_SIZE * SF
        self.n_lines = int(self.height / self.cell_size)

    def draw_grid(self):
        for i in range(self.n_lines+1):
            pg.draw.line(self.win, WHITE, (i * self.cell_size, 0), (i * self.cell_size, self.height),
                         SF)  # Vertical line
            pg.draw.line(self.win, WHITE, (0, i * self.cell_size), (self.height, i * self.cell_size),
                         SF)  # Horizontal line
            pg.draw.line(self.win, WHITE, (0, self.height-1), (self.height, self.height-1))

    def redraw(self):
        """
        Method redraws the screen
        """
        self.win.fill(self.bg_color)
        self.draw_grid()

    def update_objects(self):
        self.eat_apple()
        super().update_objects()

    def eat_apple(self):
        """
        Handles collision of the apple with the head of the snake
        :return:
        """
        if self._GOs["snake"][1].head.pos == self._GOs["apple"][1].pos:
            self._GOs["snake"][1].extend()
            self.update_apple()
            self._GOs["score_box"][1].text = "Score: " + str(len(self._GOs["snake"][1].body) - 1)

    def update_apple(self):
        """
        Updates apple position
        :return:
        """
        x, y = ri(0, 19), ri(0, 19)
        coors = [(c.x / SF, c.y / SF) for c in self._GOs["snake"][1].body]
        while (x, y) in coors:
            x, y = ri(0, 19), ri(0, 19)

        self._GOs["apple"][1].x = x * SF
        self._GOs["apple"][1].y = y * SF
