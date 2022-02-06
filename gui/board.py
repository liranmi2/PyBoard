import os.path
import pygame

from gui.menu_items import BACKGROUND, BACK, BACK_G

PIECES = ({}, {})


def init_pieces():
    for i, ptype in enumerate(["r", "n", "b", "q", "k", "p"]):
        for j, color in enumerate(["w", "b"]):
            PIECES[j][i] = pygame.image.load(os.path.join("src", "img", color+"_"+ptype+".png"))
            PIECES[j][i] = pygame.transform.scale(PIECES[j][i], (60, 60))


def draw_pieces(screen):
    init_pieces()

    # draw black
    for x in range(8):
        if x > 4:
            screen.blit(PIECES[1][7 - x], (60 * (x+2.4), 60 * 1.2))
        else:
            screen.blit(PIECES[1][x], (60 * (x+2.4), 60 * 1.2))
        screen.blit(PIECES[1][5], (60 * (x + 2.4), 60 * 2.2))

    # draw white
    for x in range(8):
        if x > 4:
            screen.blit(PIECES[0][7 - x], (60 * (x+2.4), 60 * 8.2))
        else:
            screen.blit(PIECES[0][x], (60 * (x+2.4), 60 * 8.2))
        screen.blit(PIECES[0][5], (60 * (x + 2.4), 60 * 7.2))


def draw_board(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(BACK, (50, 550))
    pygame.draw.rect(screen, (128, 76, 60), (144, 72, 480, 480))
    pygame.draw.rect(screen, (56,56,56), (139, 67, 490, 489), 5, 1)
    for y in range(1, 9):
        for x in range(2, 10):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, (88, 44, 44), (60 * (x+0.4), 60 * (y+0.2), 60, 60))
            # else:
            #     pygame.draw.rect(screen, (220, 240, 240), (100 * x, 100 * y, 100, 100))
    draw_pieces(screen)

