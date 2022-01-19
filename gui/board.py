import pygame

from gui.menu_items import BACKGROUND, BACK, BACK_G


# def draw_pieces(screen):
#     print


def draw_board(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(BACK, (50, 550))
    pygame.draw.rect(screen, (128, 76, 60), (144, 72, 480, 480))
    pygame.draw.rect(screen, (70, 26, 11), (139, 67, 490, 489), 5, 5)
    for y in range(1, 9):
        for x in range(2, 10):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, (88, 44, 44), (60 * (x+0.4), 60 * (y+0.2), 60, 60))
            # else:
            #     pygame.draw.rect(screen, (220, 240, 240), (100 * x, 100 * y, 100, 100))
    # draw_pieces(screen)

