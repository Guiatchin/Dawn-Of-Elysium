# C
import pygame

COLOR_RED = (255, 57, 36)
COLOR_LIME = (186, 255, 36)
COLOR_WHITE = (255, 255, 255)
COLOR_BLACK = (0, 0, 0)
COLOR_ORANGE = (255, 165, 0)
# E
ENTITY_DAMAGE = {'bg30': 0, 'bg31': 0,
                 'bg32': 0, 'bg33': 0,
                 'bg34': 0, 'bg40': 0,
                 'bg41': 0, 'bg42': 0,
                 'bg43': 0, 'bg44': 0,
                 'bg45': 0, 'Player1Shot': 25,
                 'Player1': 5, 'Player2Shot': 25,
                 'Player2': 5,
                 'Enemy1Shot': 15, 'Enemy1': 5,
                 'Enemy2Shot': 20, 'Enemy2': 5
                 }
ENTITY_SCORE = {'bg30': 0, 'bg31': 0,
                'bg32': 0, 'bg33': 0,
                'bg34': 0, 'bg40': 0,
                'bg41': 0, 'bg42': 0,
                'bg43': 0, 'bg44': 0,
                'bg45': 0, 'Player1Shot': 0,
                'Player1': 0, 'Player2Shot': 0,
                'Player2': 0,
                'Enemy1Shot': 0, 'Enemy1': 100,
                'Enemy2Shot': 0, 'Enemy2': 115
                }
ENTITY_HEALTH = {
    'bg30': 999, 'bg31': 999,
    'bg32': 999, 'bg33': 999,
    'bg34': 999, 'bg40': 999,
    'bg41': 999, 'bg42': 999,
    'bg43': 999, 'bg44': 999,
    'bg45': 999,
    'Player1': 200, 'Player1Shot': 1,
    'Player2': 200, 'Player2Shot': 1,
    'Enemy1': 50, 'Enemy1Shot': 1,
    'Enemy2': 60, 'Enemy2Shot': 1

}
ENTITY_SPEED = {'bg30': 0,
                'bg31': 1,
                'bg32': 2,
                'bg33': 3,
                'bg34': 4,
                'Player1': 3,
                'Player1Shot': 7,
                'Player2': 3,
                'Player2Shot': 7,
                'Enemy1': 2,
                'Enemy1Shot': 6,
                'Enemy2': 3,
                'Enemy2Shot': 7
                }
ENTITY_SHOT_DELAY = {'Player1': 15,
                     'Player2': 15,
                     'Enemy1': 60,
                     'Enemy2': 60,
                     }
EVENT_ENEMY = pygame.USEREVENT + 1

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
                    'Player2': pygame.K_LCTRL}

# W
WIN_WIDTH = 576
WIN_HEIGHT = 324

# S

SCORE_POS = {'Title': (WIN_WIDTH / 2, 50),
             'EnterName': (WIN_WIDTH / 2, 80),
             'Label': (WIN_WIDTH / 2, 90),
             'Name': (WIN_WIDTH / 2, 110),
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
