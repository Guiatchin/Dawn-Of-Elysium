#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame as pg

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.level import Level
from code.menu import Menu


class Game:
    def __init__(self):
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pg.init()


    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()

            match menu_return:
                case 'NEW GAME 1P':
                    level = Level(self.window, 'Level 1', menu_return)
                    level_return = level.run()
                case 'NEW GAME 2P - COOPERATIVE':
                    level = Level(self.window, 'Level 1', menu_return)
                    level_return = level.run()

                case 'EXIT':
                    pygame.quit()  # Close Game
                    print('Game Closed')
                    quit()  # End Pygame
                case _:
                    pass


