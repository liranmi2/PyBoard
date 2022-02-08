import os.path
import pygame

from gui.menu_items import BACKGROUND, BACK, BACK_G

PIECES = {}

coord = list()
tiles = ["a8", "b8", "c8", "d8", "e8", "f8", "g8", "h8",
         "a7", "b7", "c7", "d7", "e7", "f7", "g7", "h7",
         "a6", "b6", "c6", "d6", "e6", "f6", "g6", "h6",
         "a5", "b5", "c5", "d5", "e5", "f5", "g5", "h5",
         "a4", "b4", "c4", "d4", "e4", "f4", "g4", "h4",
         "a3", "b3", "c3", "d3", "e3", "f3", "g3", "h3",
         "a2", "b2", "c2", "d2", "e2", "f2", "g2", "h2",
         "a1", "b1", "c1", "d1", "e1", "f1", "g1", "h1"]


def init_pieces(screen):
    for ptype in ["r", "n", "b", "q", "k", "p"]:
        for color in ["w", "b"]:
            PIECES[color+ptype] = pygame.image.load(os.path.join("src", "img", color+"_"+ptype+".png"))
            PIECES[color+ptype] = pygame.transform.scale(PIECES[color+ptype], (60, 60))
            PIECES[color+ptype] = PIECES[color+ptype].convert_alpha(screen)


def draw_pieces(screen, board):
    init_pieces(screen)
    for i in range(8):
        for j in range(8):
            if board[i][j] is not None:
                piece = board[i][j][0] + board[i][j][1][0]
                screen.blit(PIECES[piece], (60 * (j+2.4), 60 * (i+1.2)))
    # draw black
    # for x in range(8):
    #     if x > 4:
    #         screen.blit(PIECES[1][7 - x], (60 * (x+2.4), 60 * 1.2))
    #     else:
    #         screen.blit(PIECES[1][x], (60 * (x+2.4), 60 * 1.2))
    #     screen.blit(PIECES[1][5], (60 * (x + 2.4), 60 * 2.2))
    #
    # # draw white
    # for x in range(8):
    #     if x > 4:
    #         screen.blit(PIECES[0][7 - x], (60 * (x+2.4), 60 * 8.2))
    #     else:
    #         screen.blit(PIECES[0][x], (60 * (x+2.4), 60 * 8.2))
    #     screen.blit(PIECES[0][5], (60 * (x + 2.4), 60 * 7.2))


def draw_board(screen, board):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(BACK, (50, 550))
    pygame.draw.rect(screen, (128, 76, 60), (144, 72, 480, 480))
    pygame.draw.rect(screen, (56,56,56), (139, 67, 490, 489), 5, 1)
    for y in range(1, 9):
        for x in range(2, 10):
            if (x + y) % 2 == 0:
                pygame.draw.rect(screen, (88, 44, 44), (60 * (x+0.4), 60 * (y+0.2), 60, 60))
            coord.append((60 * (x+0.4), 60 * (y+0.2)))
            # else:
            #     pygame.draw.rect(screen, (220, 240, 240), (100 * x, 100 * y, 100, 100))
    draw_pieces(screen, board)
    return coord


def draw_moves(screen, moves, board):
    for move in moves:
        pygame.draw.rect(screen,(232, 187, 72), (60 * (move[1] + 2.4), 60 * (move[0] + 1.2), 58, 58))
    draw_pieces(screen, board)

