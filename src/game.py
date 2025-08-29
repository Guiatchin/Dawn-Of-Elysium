#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import pygame as pg

from src.Const import WIN_WIDTH, WIN_HEIGHT
from src.Score import Score
from src.level import Level
from src.menu import Menu


class Game:
    def __init__(self):
        self.window = pg.display.set_mode(size=(WIN_WIDTH, WIN_HEIGHT))
        pg.init()

    def run(self):
        while True:
            menu = Menu(self.window)
            menu_return = menu.run()
            player_score = [0, 0]  # [Player1, PLayer2]
            score = Score(self.window)

            match menu_return:
                case 'NEW GAME 1P':
                    level = Level(self.window, 'Level1', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level2', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)

                case 'NEW GAME 2P - COOPERATIVE':
                    level = Level(self.window, 'Level1', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level2', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)
                case 'NEW GAME 2P - COMPETITIVE':
                    level = Level(self.window, 'Level1', menu_return, player_score)
                    level_return = level.run(player_score)
                    if level_return:
                        level = Level(self.window, 'Level2', menu_return, player_score)
                        level_return = level.run(player_score)
                        if level_return:
                            score.save(menu_return, player_score)

                case 'SCORE':
                    score.show()

                case 'EXIT':
                    pygame.quit()  # Close Game
                    print('Game Closed')
                    quit()  # End Pygame
                case _:
                    pass
