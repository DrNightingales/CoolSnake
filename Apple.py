from random import randint as ri

import pygame as pg

from Cube import Cube
from constants import *


class Apple(Cube):
    """
    Apple class, GO for snake to eat
    """

    def __init__(self, surface, color, a, snake, score_box):
        self.snake = snake  # Apple watches snake
        x, y = self.get_coordinates()
        super().__init__(surface, color, x, y, a)
        self.score_box = score_box
        self.score = 0


    def update(self, event_list):
        """
        Detects snake-apple interaction, updates score, extends snake and reposition the apple
        :param event_list: event list from host screen
        :return:
        """
        if self.pos == self.snake.head.pos:
            self.snake.extend()
            self.score += 1
            self.score_box.text = f"Score: {self.score}"
            print(len(self.snake.body))
            x, y = self.get_coordinates()
            self.x, self.y = x * SF, y * SF
        pg.draw.rect(self.surface, self.color, self.rect)

    def get_coordinates(self):
        """
        Updates apple coordinates randomly, but in a way to avoid apple be places in the snake
        :return: x, y - a pair of new coors.
        """
        x, y = ri(0, 19), ri(0, 19)
        coors = [(c.x / SF, c.y / SF) for c in self.snake.body]
        while (x, y) in coors:
            x, y = ri(0, 19), ri(0, 19)

        return x, y
