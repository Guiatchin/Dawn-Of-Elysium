#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random

from src.EntityMediator import EntityMediator
from src.enemy import Enemy
from src.entity import Entity
from src.entityFactory import EntityFactory
from pygame import Rect, Surface
from pygame.font import Font

from src.Const import WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, EVENT_ENEMY, COLOR_LIME
from src.player import Player


class Level:
    def __init__(self, window, name, game_mode):
        self.timeout = 20000  # 20 seconds
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity('bg30'))
        self.entity_list.append(EntityFactory.get_entity('Player1'))
        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            self.entity_list.append(EntityFactory.get_entity('Player2'))
        pygame.time.set_timer(EVENT_ENEMY,3000)
    def run(self, ):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)
            for ent in self.entity_list:
                self.window.blit(source=ent.surf,dest=ent.rect)
                ent.move()
                if isinstance(ent,(Player, Enemy)): #Guilherme Ferreira
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(ent.shoot())
                if ent.name =='Player1':
                    self.level_text(14, f'Player 1 - Health {ent.health} | Score: {ent.score}' , COLOR_LIME, (10,25))
                if ent.name =='Player2':
                    self.level_text(14, f'Player 2 - Health {ent.health} | Score: {ent.score}', COLOR_LIME, (10,45))

            for event in pygame.event.get(): #event listener
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Game
                    print('Game Closed')
                    quit()  # End Pygame
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1','Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))


            pygame.display.flip()

            self.level_text(14, f'{self.name} - timeout: {self.timeout / 1000 : .1f}s', COLOR_ORANGE, (10,5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_ORANGE, (10,WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_ORANGE, (10,WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.collision_check(entity_list=self.entity_list)
            EntityMediator.health_check(entity_list=self.entity_list)



    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0],top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)