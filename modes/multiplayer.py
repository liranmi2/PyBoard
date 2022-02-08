
import pygame

from gui.menu_items import MultiplayerMenu as Menu
from gui.menu_items import BACKGROUND, BACK, BACK_G
from gui.board import draw_board, draw_moves, tiles
from modes.online_menu import main as onlinemenu
from engine.moves import LOGIC, legal_moves


localCoord = (330, 250, 120, 70)
onlineCoord = (320, 350, 130, 70)


def draw_menu(screen):
    screen.blit(BACKGROUND, (0, 0))
    screen.blit(Menu.LOCATE,  (180, 100))
    screen.blit(Menu.LOCAL, localCoord[:2])
    screen.blit(Menu.ONLINE, onlineCoord[:2])
    screen.blit(BACK, (50, 550))


def play(screen):
    clock = pygame.time.Clock()
    board = LOGIC
    board[4][3], board[7][0] = board[7][0], board[4][3]
    board[3][6], board[0][7] = board[0][7], board[3][6]
    board[0][2], board[3][2] = board[3][2], board[0][2]

    coord = draw_board(screen, board)
    coord_tiles = dict(zip(tiles, coord))
    board_tiles = dict(zip(tiles, [item for sublist in board for item in sublist]))
    moves = None
    pos = None
    turn = 0
    turn_dict = {0: "w", 1: "b"}
    tile = None
    # for c in coord_tiles:
    #     print(c,coord_tiles[c])
    # for c in board_tiles:
    #     print(c,board_tiles[c])
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                for i in range(len(coord)):
                    if coord[i][0] < x < coord[i][0] + 60 and coord[i][1] < y < coord[i][1] + 60:
                        tile = list(coord_tiles.keys())[list(coord_tiles.values()).index(coord[i])]
                        if moves is not None:
                            for move in moves:
                                if i == move[0] * 8 + move[1]:
                                    board[move[0]][move[1]] = board[pos[0]][pos[1]]
                                    board[pos[0]][pos[1]] = None
                                    board_tiles = dict(zip(tiles, [item for sublist in board for item in sublist]))
                                    draw_board(screen, board)
                                    moves = None
                                    turn = (turn + 1) % 2
                                    break
                        break

                draw_board(screen, board)
                if tile is not None and board_tiles[tile] is not None and board_tiles[tile][0] == turn_dict[turn]:
                    moves, pos = legal_moves(board, board_tiles[tile])
                    draw_moves(screen, moves, board)
        pygame.display.update()


def main(screen):
    clock = pygame.time.Clock()
    while True:
        clock.tick(24)
        draw_menu(screen)
        x, y = pygame.mouse.get_pos()

        # Menu items will turn gray while hovering them
        if localCoord[0] < x < sum(localCoord[::2]) and localCoord[1] < y < sum(localCoord[1::2]):
            screen.blit(Menu.LOCAL_G, localCoord[:2])

        if onlineCoord[0] < x < sum(onlineCoord[::2]) and onlineCoord[1] < y < sum(onlineCoord[1::2]):
            screen.blit(Menu.ONLINE_G, onlineCoord[:2])

        if 50 < x < 120 and 550 < y < 600:
            screen.blit(BACK_G, (50, 550))

        for event in pygame.event.get():

            if event.type == pygame.QUIT:
                return 0

            elif event.type == pygame.MOUSEBUTTONDOWN:
                x, y = event.pos
                if 50 < x < 120 and 550 < y < 600:
                    return 1
                # if localCoord[0] < x < sum(localCoord[::2]) and localCoord[1] < y < sum(localCoord[1::2]):
                #     play()
                if pygame.Rect(onlineCoord).collidepoint(pygame.mouse.get_pos()):
                    ret = onlinemenu(screen)
                    if ret == 0:
                        return 0
                if pygame.Rect(localCoord).collidepoint(pygame.mouse.get_pos()):
                    # draw_board(screen)
                    ret = play(screen)
                    if ret == 0:
                        return 0

        pygame.display.update()
