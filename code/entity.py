#!/usr/bin/python
# -*- coding: utf-8 -*-
from abc import ABC

import pygame


class Entity(ABC):
    def __init__(self, name: str, position: tuple):
        self.name = name
        self.surf = pygame.image.load('./assets' + name + '.png')
        self.rect = None

    def move(self, ):
        pass
