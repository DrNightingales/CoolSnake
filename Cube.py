from constants import *
from GameObject import GameObject


class Cube(GameObject):
    def __init__(self, color, surface, x, y):
        super().__init__(color, surface, x, y)