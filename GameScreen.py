from sys import exit

import pygame as pg

from constants import *


class GameScreen:
    """
    Base screen class (game objects will be drawn here)
    """
    def __init__(self,
                 width=WIDTH,
                 height=HEIGHT,
                 bg_color=RETRO_VIOLET):

        # Scaling factor for HiDPI monitors

        self.width = width*SF
        self.height = height*SF
        self.bg_color = bg_color

        self.win = pg.display.set_mode((self.width, self.height))
        self._GOs = {}  # Dict of GOs, which belong to the current screen
        self.event_list = []  # List of events, updated per frame

    @property
    def game_objects(self):
        return self._GOs

    @game_objects.setter
    def game_objects(self, value):
        raise Exception("Can't set game_objects")

    def add_game_object(self, name, game_object):
        """
        Adds a GameObject to the screen

        :param game_object: (priority, GameObject class instance)
        name: name of the object
        """
        self._GOs[name] = game_object

    def remove_game_object(self, name):
        """
        Removes GO from the screen
        :param name: remove GO by name
        """
        del self._GOs[name]

    def screen_update(self):
        """
        Updates the screen, redraws objects, updates list of events
        """

        self.handle_events()
        self.redraw()
        self.update_objects()

        pg.display.update()

    def handle_events(self):
        """
        Method gets event list and listens for QUIT event
        """
        self.event_list = pg.event.get()
        for event in self.event_list:
            if event.type == pg.QUIT:
                pg.quit()
                exit()

    def redraw(self):
        """
        Method redraws the screen
        """
        self.win.fill(self.bg_color)

    def update_objects(self):
        """
        Updates all GameObjects on the screen
        """
        object_list = [v for v in self._GOs.values()]
        object_list.sort()
        for obj in object_list:
            obj[1].update(self.event_list)





