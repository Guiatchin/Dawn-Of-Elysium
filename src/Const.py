# C
import pygame

COLOR_RED = (255, 57, 36)
COLOR_LIME = (186, 255, 36)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ORANGE = (255, 165, 0)
COLOR_PURPLE = (74, 19, 122)
COLOR_BLUE = (0, 255, 0)
# E
ENTITY_DAMAGE = {'Level1bg0': 0, 'Level1bg1': 0,
                 'Level1bg2': 0, 'Level1bg3': 0,
                 'Level1bg4': 0, 'Level2bg0': 0,
                 'Level2bg1': 0, 'Level2bg2': 0,
                 'Level2bg3': 0, 'Level2bg4': 0,
                 'Level2bg5': 0, 'Player1Shot': 25,
                 'Player1': 5, 'Player2Shot': 25,
                 'Player2': 5, 'Boss': 100,
                 'Enemy1Shot': 20, 'Enemy1': 5,
                 'Enemy2Shot': 25, 'Enemy2': 5
                 }
ENTITY_SCORE = {'Level1bg0': 0, 'Level1bg1': 0,
                'Level1bg2': 0, 'Level1bg3': 0,
                'Level1bg4': 0, 'Level2bg0': 0,
                'Level2bg1': 0, 'Level2bg2': 0,
                'Level2bg3': 0, 'Level2bg4': 0,
                'Level2bg5': 0,
                'Player1Shot': 0,
                'Player1': 0, 'Player2Shot': 0,
                'Player2': 0, 'Boss': 300,
                'Enemy1Shot': 0, 'Enemy1': 100,
                'Enemy2Shot': 0, 'Enemy2': 120
                }
ENTITY_HEALTH = {'Level1bg0': 999, 'Level1bg1': 999,
                 'Level1bg2': 999, 'Level1bg3': 999,
                 'Level1bg4': 999, 'Level2bg0': 999,
                 'Level2bg1': 999, 'Level2bg2': 999,
                 'Level2bg3': 999, 'Level2bg4': 999,
                 'Level2bg5': 999, 'Boss': 400,
                 'Player1': 200, 'Player1Shot': 1,
                 'Player2': 200, 'Player2Shot': 1,
                 'Enemy1': 50, 'Enemy1Shot': 1,
                 'Enemy2': 50, 'Enemy2Shot': 1

                 }
ENTITY_SPEED = {'Level1bg0': 0, 'Level1bg1': 1,
                'Level1bg2': 2, 'Level1bg3': 3,
                'Level1bg4': 4, 'Level2bg0': 0,
                'Level2bg1': 3, 'Level2bg2': 2,
                'Level2bg3': 3, 'Level2bg4': 4,
                'Level2bg5': 5,

                'Player1': 3,
                'Player1Shot': 7,
                'Player2': 3,
                'Player2Shot': 7,
                'Enemy1': 2,
                'Enemy1Shot': 6,
                'Enemy2': 3,
                'Enemy2Shot': 7,
                'Boss': 1
                }
ENTITY_SHOT_DELAY = {'Player1': 15,
                     'Player2': 15,
                     'Enemy1': 60,
                     'Enemy2': 60,
                     'Boss': 999
                     }

EVENT_ENEMY = pygame.USEREVENT + 1
EVENT_TIMEOUT = pygame.USEREVENT + 2
# M
MENU_OPTION = ('NEW GAME 1P',
               'NEW GAME 2P - COOPERATIVE',
               'NEW GAME 2P - COMPETITIVE',
               'SCORE',
               'EXIT')
# P
PLAYER_KEY_UP = {'Player1': pygame.K_UP,
                 'Player2': pygame.K_w}
PLAYER_KEY_DOWN = {'Player1': pygame.K_DOWN,
                   'Player2': pygame.K_s}
PLAYER_KEY_LEFT = {'Player1': pygame.K_LEFT,
                   'Player2': pygame.K_a}
PLAYER_KEY_RIGHT = {'Player1': pygame.K_RIGHT,
                    'Player2': pygame.K_d}
PLAYER_KEY_SHOOT = {'Player1': pygame.K_RALT,
                    'Player2': pygame.K_LSHIFT}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
             'FinalScore': (WIN_WIDTH / 2, 140),
             0: (WIN_WIDTH / 2, 110),
             1: (WIN_WIDTH / 2, 130),
             2: (WIN_WIDTH / 2, 150),
             3: (WIN_WIDTH / 2, 170),
             4: (WIN_WIDTH / 2, 190),
             5: (WIN_WIDTH / 2, 210),
             6: (WIN_WIDTH / 2, 230),
             7: (WIN_WIDTH / 2, 250),
             8: (WIN_WIDTH / 2, 270),
             9: (WIN_WIDTH / 2, 290),
             }
# T
TIMEOUT_STEP = 100
TIMEOUT_LEVEL = 15000
