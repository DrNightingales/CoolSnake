import pygame as pg

from GameScreen import GameScreen
from constants import *
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

        font = pg.font.Font("fonts/libr3am.otf", 100)
        font.set_italic(True)
        text_width, _ = font.size("Retro Neon Cool Snake")
        text_surface = font.render("Retro Neon Cool Snake", True, RETRO_VIOLET)
        sur_rect = pg.Surface((800 * 2, 600 * 2))
        self.win.blit(text_surface, ((self.width - text_width) / 2, 100))
        #
        # font2 = pg.font.Font("fonts/libr3am.otf", 90)
        # font2.set_bold(True)
        # font2.set_italic(True)
        # text_width2, _ = font2.size("Retro Neon Cool Snake")
        # text_surface2 = font2.render("Retro Neon Cool Snake", True, RETRO_VIOLET)
        # sur_rect.blit(text_surface2, ((self.width-text_width2)/2, 150))
        # self.win.blit(sur_rect, (0,0),)

        # TODO: https://stackoverflow.com/questions/49594895/render-anti-aliased-transparent-text-in-pygame
