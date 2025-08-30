#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
from pygame import Rect, Surface
from pygame.font import Font

from src.Const import WIN_WIDTH, COLOR_RED, MENU_OPTION, COLOR_BLACK


class Menu:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/background2/orig.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def run(self):
        menu_option = 0
        pygame.mixer_music.load('./assets/menu.ogg')
        pygame.mixer_music.play(-1)
        pygame.mixer_music.set_volume(0.4)

        while True:
            pygame.display.set_caption('Dawn Of Elysium')
            self.window.blit(source=self.surf, dest=self.rect)

            self.menu_text(60, 'Dawn Of', COLOR_RED, ((WIN_WIDTH / 2), 70))
            self.menu_text(60, 'ELYSIUM', COLOR_RED, ((WIN_WIDTH / 2), 120))

            for i in range(len(MENU_OPTION)):
                if i == menu_option:
                    self.menu_text(20, MENU_OPTION[i], COLOR_RED, ((WIN_WIDTH / 2), 200 + 25 * i))
                else:
                    self.menu_text(20, MENU_OPTION[i], COLOR_BLACK, ((WIN_WIDTH / 2), 200 + 25 * i))

            pygame.display.flip()

            # Check for events
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Game
                    print('Game Closed')
                    quit()  # End Pygame
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_DOWN:
                        if menu_option < len(MENU_OPTION) - 1:
                            menu_option += 1
                        else:
                            menu_option = 0

                    if event.key == pygame.K_UP:
                        if menu_option > 0:
                            menu_option -= 1
                        else:
                            menu_option = len(MENU_OPTION) - 1
                    if event.key == pygame.K_RETURN:
                        return MENU_OPTION[menu_option]

    def menu_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)
