import pygame

from nlc_dino_runner.utils.constants import SCREEN_WIDTH, SCREEN_HEIGHT

FONT_STYLE = "freesansbold.ttf"
BLACK_COLOR = (0, 0, 0)
WHITE_COLOR = (255, 255, 255)

def get_score_element(points, dark):
    font = pygame.font.Font(FONT_STYLE, 22)
    if dark:
        text = font.render("Points: " + str(points), True, WHITE_COLOR)
    else:
        text = font.render("Points: " + str(points), True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (1020, 30)

    return (text,text_rect)

def get_centered_masage(masage, width=SCREEN_WIDTH // 2, height=SCREEN_HEIGHT // 2, size=30, dark=False):

    font = pygame.font.Font(FONT_STYLE, size)
    if dark:
        text = font.render(masage, True, WHITE_COLOR)
    else:
        text = font.render(masage, True, BLACK_COLOR)
    text_rect = text.get_rect()
    text_rect.center = (width, height)
    return (text,text_rect)
