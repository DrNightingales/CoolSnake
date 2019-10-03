import pygame as pg

from GameObject import GameObject


class TextBox(GameObject):
    """
    GO for printing text on screen
    """

    def __init__(self, surface, color, x, y, font, text, font_size=100):
        super().__init__(surface, color, x, y)
        pg.font.init()
        self.font = pg.font.Font(font, font_size)
        self.text_surface = self.font.render(text, True, color)
        self.width, self.height = self.font.size(text)
        self._text = text

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        self._text = text

    def update(self, event_list):
        """
        Updates text sign
        :param event_list: List of pygame events
        """
        self.text_surface = self.font.render(self._text, True, self.color)
        self.width, self.height = self.font.size(self._text)
        self.surface.blit(self.text_surface, (self.x, self.y))
