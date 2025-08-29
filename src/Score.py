import sys
from datetime import datetime

import pygame
from pygame import Surface, Rect, K_ESCAPE
from pygame.font import Font

from src.Const import SCORE_POS, MENU_OPTION, COLOR_BLACK, COLOR_RED
from src.DBProxy import DBProxy


class Score:
    def __init__(self, window):
        self.window = window
        self.surf = pygame.image.load('./assets/background1/orig.png').convert_alpha()
        self.rect = self.surf.get_rect(left=0, top=0)

    def save(self, game_mode: str, player_score: list[int]):
        db_proxy = DBProxy('DBScore')
        name = ''
        while True:
            self.window.blit(source=self.surf, dest=self.rect)
            self.score_text(48, 'YOU WIN!!', COLOR_RED, SCORE_POS['Title'])
            score = player_score[0]
            text = 'Enter Player 1 name (4 characters):'
            self.score_text(24, f'FINAL SCORE {score}', COLOR_RED, SCORE_POS['FinalScore'])

            if game_mode == MENU_OPTION[0]:
                score = player_score[0]
                self.score_text(24, f'FINAL SCORE {score}', COLOR_RED, SCORE_POS['FinalScore'])
            if game_mode == MENU_OPTION[1]:
                score = (player_score[0] + player_score[1]) / 2
                text = 'Enter TEAM name (4 characters):'
                self.score_text(24, f'FINAL SCORE {score}', COLOR_RED, SCORE_POS['FinalScore'])
            if game_mode == MENU_OPTION[2]:
                if player_score[0] >= player_score[1]:
                    score = player_score[0]
                    self.score_text(24, f'FINAL SCORE {score}', COLOR_RED, SCORE_POS['FinalScore'])
                else:
                    score = player_score[1]
                    text = 'Enter Player 2 name (4 characters):'
                    self.score_text(24, f'FINAL SCORE {score}', COLOR_RED, SCORE_POS['FinalScore'])
            self.score_text(20, text, COLOR_BLACK, SCORE_POS['EnterName'])

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN and len(name) == 4:
                        db_proxy.save({'name': name, 'score': score, 'date': get_formatted_date()})
                        self.show()
                        return
                    elif event.key == pygame.K_BACKSPACE:
                        name = name[:-1]
                    else:
                        if len(name) < 4:
                            name += event.unicode
            self.score_text(20, name, COLOR_BLACK, SCORE_POS['Name'])
            pygame.display.flip()
            pass

    def show(self):
        self.window.blit(source=self.surf, dest=self.rect)
        while True:
            self.score_text(48, 'TOP 10 SCORE', COLOR_BLACK, SCORE_POS['Title'])
            self.score_text(20, 'NAME     SCORE           DATE      ', COLOR_BLACK, SCORE_POS['Label'])
            db_proxy = DBProxy('DBScore')
            list_score = db_proxy.retrieve_top10()
            db_proxy.close()

            for player_score in list_score:
                id_, name, score, date = player_score
                self.score_text(20, f'{name}     {score:05d}     {date}', COLOR_BLACK,
                                SCORE_POS[list_score.index(player_score)])
            while True:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    if event.type == pygame.KEYDOWN:
                        if event.key == K_ESCAPE:
                            return
                pygame.display.flip()

    def score_text(self, text_size: int, text: str, text_color: tuple, text_center_pos: tuple):
        text_font: Font = pygame.font.SysFont(name="Lucida Sans Typewriter", size=text_size)
        text_surf: Surface = text_font.render(text, True, text_color).convert_alpha()
        text_rect: Rect = text_surf.get_rect(center=text_center_pos)
        self.window.blit(source=text_surf, dest=text_rect)


def get_formatted_date():
    current_datetime = datetime.now()
    current_time = current_datetime.strftime("%H:%M")
    current_date = current_datetime.strftime("%d/%m/%y")
    return f"{current_time} - {current_date}"
