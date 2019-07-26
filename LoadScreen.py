import pygame as pg
from constants import *
from GameScreen import GameScreen
from fill_gradient import fill_gradient


class LoadScreen(GameScreen):
    def __init__(self,
                 width=WIDTH,
                 height=HEIGHT,
                 bg_color=RETRO_VIOLET,
                 gradient=False,
                 grad_color=None):

        super().__init__(width,
                         height,
                         bg_color)
        self.gradient = gradient
        if self.gradient:
            self.grad_color = grad_color

    def redraw(self):
        if self.gradient:
            upper_section = pg.Rect((0, 0), (self.width, self.height*0.75))
            lower_section = pg.Rect((0, self.height*0.75), (self.width, self.height*0.25))
            fill_gradient(self.win, self.bg_color, self.grad_color, rect=upper_section, forward=False)
            self.win.fill(self.bg_color, lower_section)
        else:
            self.win.fill(self.bg_color)
