import random

from src.Const import WIN_WIDTH, WIN_HEIGHT
from src.background import Background
from src.boss import Boss
from src.enemy import Enemy
from src.player import Player


class EntityFactory:

    @staticmethod
    def get_entity(entity_name):
        match entity_name:
            case 'Level1bg0': #Level 1
                list_bg = []
                for i in range(5): #Level 1 Bg images
                    list_bg.append(Background(f'Level1bg{i}', (0,0)))
                    list_bg.append(Background(f'Level1bg{i}', (WIN_WIDTH,0)))
                return list_bg

            case 'Level2bg0': #Level 2
                list_bg = []
                for i in range(6): #Level 2 Bg images
                    list_bg.append(Background(f'Level2bg{i}', (0, 0)))
                    list_bg.append(Background(f'Level2bg{i}', (WIN_WIDTH, 0)))
                return list_bg

            case 'Player1':
                return Player('Player1', (10,WIN_HEIGHT / 2 -30))
            case 'Player2':
                return Player('Player2', (10,WIN_HEIGHT / 2 + 30))
            case 'Enemy1':
                return Enemy('Enemy1',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40) ))
            case 'Enemy2':
                return Enemy('Enemy2',(WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 40) ))
            case 'Boss':
                return Boss('Boss', (WIN_WIDTH + 10, random.randint(40, WIN_HEIGHT - 70) ))




