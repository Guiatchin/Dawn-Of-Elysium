#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame as pg

from code.menu import Menu


class Game:
    def __init__(self):
        self.window = None
        pg.init()
        screen = pg.display.set_mode(size=(800, 600))

    def run(self):

        while True:
            menu = Menu(self.window)
            menu.run()
            pass

            # for event in pg.event.get():
            #     if event.type == pg.QUIT:
            #         pg.quit()  # Close Game
            #         print('Game Closed')
            #         quit()  # End Pygame

