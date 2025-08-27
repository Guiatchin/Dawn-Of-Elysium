#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame
import random

from src.EntityMediator import EntityMediator
from src.boss import Boss
from src.enemy import Enemy
from src.entity import Entity
from src.entityFactory import EntityFactory
from pygame import Rect, Surface
from pygame.font import Font

from src.Const import WIN_HEIGHT, COLOR_ORANGE, MENU_OPTION, EVENT_ENEMY, COLOR_LIME, EVENT_TIMEOUT, TIMEOUT_STEP, \
    TIMEOUT_LEVEL, COLOR_BLUE, COLOR_PURPLE
from src.player import Player


class Level:
    def __init__(self, window, name, game_mode, player_score: list[int]):
        self.timeout = TIMEOUT_LEVEL  # 20 seconds
        self.window = window
        self.name = name
        self.game_mode = game_mode
        self.level_state = ''
        self.entity_list: list[Entity] = []
        self.entity_list.extend(EntityFactory.get_entity(self.name + 'bg0'))
        player = EntityFactory.get_entity('Player1')
        player.score = player_score[0]
        self.entity_list.append(player)

        if game_mode in [MENU_OPTION[1], MENU_OPTION[2]]:
            player = EntityFactory.get_entity('Player2')
            player.score = player_score[1]
            self.entity_list.append(player)

        pygame.time.set_timer(EVENT_ENEMY, 3000)
        pygame.time.set_timer(EVENT_TIMEOUT, TIMEOUT_STEP)

    def run(self, player_score: list[int]):
        clock = pygame.time.Clock()
        while True:
            clock.tick(60)

            for ent in self.entity_list:
                self.window.blit(source=ent.surf, dest=ent.rect)
                ent.move()
                if isinstance(ent, (Player, Enemy)):  # Guilherme Ferreira
                    shoot = ent.shoot()
                    if shoot is not None:
                        self.entity_list.append(shoot)
                if ent.name == 'Player1':
                    self.level_text(14, f'Player 1 - Health {ent.health} | Score: {ent.score}', COLOR_BLUE, (10, 25))
                if ent.name == 'Player2':
                    self.level_text(14, f'Player 2 - Health {ent.health} | Score: {ent.score}', COLOR_PURPLE, (10, 45))

            for event in pygame.event.get():  # event listener
                if event.type == pygame.QUIT:
                    pygame.quit()  # Close Game
                    print('Game Closed')
                    quit()  # End Pygame
                if event.type == EVENT_ENEMY:
                    choice = random.choice(('Enemy1', 'Enemy2'))
                    self.entity_list.append(EntityFactory.get_entity(choice))
                if event.type == EVENT_TIMEOUT:
                    self.timeout -= TIMEOUT_STEP
                    if self.timeout == 0 and self.name =='Level1':
                        for ent in self.entity_list:
                            if isinstance(ent, Player) and ent.name == 'Player1':
                                player_score[0] = ent.score
                            if isinstance(ent, Player) and ent.name == 'Player2':
                                player_score[1] = ent.score
                        return True

                    elif self.timeout == 0 and self.name == 'Level2':
                            self.entity_list.append(EntityFactory.get_entity('Boss'))
                            print(f"Existe algum Boss na lista? {any(isinstance(ent, Boss) for ent in self.entity_list)}")
                            self.level_state = 'boss battle'

            if self.level_state == 'boss battle':
                if any(isinstance(ent, Boss) for ent in self.entity_list):
                    pass
                else:
                    self.level_state = 'vitoria'

            if self.level_state == 'vitoria':
                print(self.level_state)
                for ent in self.entity_list:
                    if isinstance(ent, Player) and ent.name == 'Player1':
                        player_score[0] = ent.score
                    if isinstance(ent, Player) and ent.name == 'Player2':
                        player_score[1] = ent.score
                return True


                # found_player = False
                # for ent in self.entity_list:
                #     if isinstance(ent, Player):
                #         found_player = True
                #     if not found_player:
                #         return False

            self.level_text(14, f'{self.name} - timeout: {self.timeout / 1000 : .1f}s', COLOR_ORANGE, (10, 5))
            self.level_text(14, f'fps: {clock.get_fps():.0f}', COLOR_ORANGE, (10, WIN_HEIGHT - 35))
            self.level_text(14, f'entidades: {len(self.entity_list)}', COLOR_ORANGE, (10, WIN_HEIGHT - 20))
            pygame.display.flip()
            EntityMediator.collision_check(entity_list=self.entity_list)
            EntityMediator.health_check(entity_list=self.entity_list)

    def level_text(self, text_size: int, text: str, text_color: tuple, text_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(left=text_pos[0], top=text_pos[1])
        self.window.blit(source=text_surf, dest=text_rect)
