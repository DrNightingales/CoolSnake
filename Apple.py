from random import choice as ch

import pygame as pg

from Cube import Cube


class Apple(Cube):
    """
    Apple class, GO for snake to eat
    """

    def __init__(self, surface, color, a):
        coors = [i for i in range(19) if i != 10]
        x, y = ch(coors), ch(coors)
        super().__init__(surface, color, x, y, a)
        del coors

    def update(self, event_list):
        """
        Detects snake-apple interaction, updates score, extends snake and reposition the apple
        :param event_list: event list from host screen
        :return:
        """
        pg.draw.rect(self.surface, self.color, self.rect)

