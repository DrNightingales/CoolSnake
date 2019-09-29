import pygame as pg

from GameObject import GameObject


class Button(GameObject):
    """
    Button class: rectangle with click handling
    """

    def __init__(self, surface, color, x, y, on_click, size=100, btn_text="Button!", font="fonts/true-crimes.ttf"):
        super().__init__(surface, color, x, y)
        pg.font.init()
        self.font = pg.font.Font(font, size)
        self.text_surface = self.font.render(btn_text, True, color)
        self.width, self.height = self.font.size(btn_text)
        self.rect = pg.Rect((self.x, self.y), (self.width, self.height))

        self.on_click = on_click
        self.text = btn_text

    def update(self, even_list):
        """
        Updates button, handles events
        :param even_list: List of pygame events on current screen
        """
        self.surface.blit(self.text_surface, (self.x, self.y))
        for event in even_list:
            if event.type == pg.MOUSEBUTTONDOWN and event.button == 1:  # Left click only on mouse
                mouse_pos = pg.mouse.get_pos()
                if self.rect.collidepoint(mouse_pos):
                    self.on_click()


