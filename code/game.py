#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame as pg

from code.Const import WIN_WIDTH, WIN_HEIGHT
from code.menu import Menu


class Game:
    def __init__(self):
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pg.init()


    def run(self):
        while True:
            menu = Menu(self.window)
            menu.run()

