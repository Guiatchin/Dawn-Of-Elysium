#!/usr/bin/python
# -*- coding: utf-8 -*-
import pygame

from src.Const import ENTITY_SPEED, ENTITY_SHOT_DELAY, ENTITY_HEALTH, COLOR_RED, COLOR_BLACK
from src.EnemyShot import EnemyShot
from src.entity import Entity


class Enemy(Entity):
    def __init__(self, name: str, position: tuple):
        super().__init__(name, position)
        self.shot_delay = ENTITY_SHOT_DELAY[self.name]
        self.max_health = ENTITY_HEALTH[self.name]
        self.health = self.max_health
        self.healthbar_width = self.rect.width
        self.healthbar_height = 7
        self.healthbar_offset_y = -10

    def move(self, ):
        self.rect.centerx -= ENTITY_SPEED[self.name]

    def shoot(self):
        self.shot_delay -= 1
        if self.shot_delay == 0:
            self.shot_delay = ENTITY_SHOT_DELAY[self.name]
            return EnemyShot(name=f'{self.name}Shot', position=(self.rect.centerx, self.rect.centery))

    def healthbar(self, window):
        if self.health < self.max_health:
            x = self.rect.x
            y = self.rect.y + self.healthbar_offset_y
            #health bar background
            healthbar_bg = pygame.Rect(x,y,self.healthbar_width, self.healthbar_height)
            pygame.draw.rect(window,COLOR_BLACK,healthbar_bg)
            #Current health
            current_health = (self.health / self.max_health) *  self.healthbar_width
            #current health bar
            current_health_width = pygame.Rect(x,y,current_health, self.healthbar_height)
            pygame.draw.rect(window,COLOR_RED,current_health_width)