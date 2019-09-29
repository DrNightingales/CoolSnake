from random import randint as ri

import pygame as pg

from Cube import Cube
from constants import *


class Apple(Cube):
    def __init__(self, surface, color, a, snake):
        self.snake = snake
        x, y = self.get_coordinates()
        super().__init__(surface, color, x, y, a)

    def update(self, event_list):
        if self.pos == self.snake.head.pos:
            self.snake.extend()
            print(len(self.snake.body))
            x, y = self.get_coordinates()
            self.x, self.y = x * SF, y * SF
        pg.draw.rect(self.surface, self.color, self.rect)

    def get_coordinates(self):
        x, y = ri(0, 19), ri(0, 19)
        for cube in self.snake.body:
            while cube.x == x:
                x = ri(0, 19)
            while cube.y == y:
                y = ri(0, 19)
            return x, y
