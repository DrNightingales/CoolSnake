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





