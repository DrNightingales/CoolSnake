import pygame as pg
from constants import *
from GameScreen import GameScreen
from LoadScreen import LoadScreen
from PlayScreen import  PlayScreen
from Button import Button


class Game:
    def __init__(self):
        self.load_screen = LoadScreen(gradient=True, grad_color=RETRO_PINK)
        self.play_screen = PlayScreen()
        self.active_screen = self.load_screen

    @staticmethod
    def exit_trigger():
        pg.quit()
        exit()

    def check_play_screen(self):
        self.active_screen = self.play_screen

    def run(self):

        play_btn = Button(self.load_screen.win, RETRO_BLUE, 0.106125 * WIDTH, 0.702 * HEIGHT, size=100,
                          on_click=self.check_play_screen, btn_text="Play")
        self.load_screen.add_game_object((10, play_btn))

        exit_btn = Button(self.load_screen.win, RETRO_BLUE, 0.76375 * WIDTH, 0.702 * HEIGHT, size=100,
                          on_click=self.exit_trigger, btn_text="Exit")
        self.load_screen.add_game_object((11, exit_btn))

        settings_btn = Button(self.load_screen.win, RETRO_BLUE, 0.39625 * WIDTH, 0.702 * HEIGHT, size=100,
                              on_click=None, btn_text="Settings")
        self.load_screen.add_game_object((12, settings_btn))
        while True:
            self.active_screen.screen_update()


if __name__ == "__main__":
    game = Game()
    game.run()
