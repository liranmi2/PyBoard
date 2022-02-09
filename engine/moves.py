
import pygame

from gui.board import draw_board, draw_moves, tiles
from gui.menu_items import BoardGame as Game
from gui.menu_items import BACK_G
from engine.stockfish import StockFish, getSFpath, rmSFpath

LOGIC = [[("b", "r1"), ("b", "n1"), ("b", "b1"), ("b", "q"), ("b", "k"), ("b", "b2"), ("b", "n2"), ("b", "r2")],
         [("b", "p1"), ("b", "p2"), ("b", "p3"), ("b", "p4"), ("b", "p5"), ("b", "p6"), ("b", "p7"), ("b", "p8")],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [("w", "p1"), ("w", "p2"), ("w", "p3"), ("w", "p4"), ("w", "p5"), ("w", "p6"), ("w", "p7"), ("w", "p8")],
         [("w", "r1"), ("w", "n1"), ("w", "b1"), ("w", "q"), ("w", "k"), ("w", "b2"), ("w", "n2"), ("w", "r2")]]


def legal_moves(board, piece):

    pos = [[i, row.index(piece)] for i, row in enumerate(board) if piece in row]
    if pos is None:
        return None, None
    pos = pos[0]
    moves = list()

    ############### rook ###############
    if piece[1][0] == "r" or piece[1][0] == "q":
        # down
        for i in range(pos[0]+1, 8):
            if board[i][pos[1]] is not None:
                if board[i][pos[1]][0] != piece[0]:
                    moves.append((i, pos[1]))
                break
            moves.append((i, pos[1]))

        # up
        for i in range(pos[0]-1, -1, -1):
            if board[i][pos[1]] is not None:
                if board[i][pos[1]][0] != piece[0]:
                    moves.append((i, pos[1]))
                break
            moves.append((i, pos[1]))

        # left
        for i in range(pos[1]+1, 8):
            if board[pos[0]][i] is not None:
                if board[pos[0]][i][0] != piece[0]:
                    moves.append((pos[0], i))
                break
            moves.append((pos[0], i))

        # right
        for i in range(pos[1]-1, -1, -1):
            if board[pos[0]][i] is not None:
                if board[pos[0]][i][0] != piece[0]:
                    moves.append((pos[0], i))
                break
            moves.append((pos[0], i))

    ############### bishop ###############
    if piece[1][0] == "b" or piece[1][0] == "q":
        j = pos[1] + 1
        for i in range(pos[0]+1, 8):
            if j == 8:
                break
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j += 1

        j = pos[1] + 1
        for i in range(pos[0]-1, -1, -1):
            if j == 8:
                break
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j += 1

        j = pos[1] - 1
        for i in range(pos[0]-1, -1, -1):
            if j == -1:
                break
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j -= 1

        j = pos[1] - 1
        for i in range(pos[0]+1, 8):
            if j == -1:
                break
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                flag = 1
                break
            moves.append((i, j))
            j -= 1

    ############### knight ###############
    elif piece[1][0] == "n":
        if (pos[0] - 1 > -1 and pos[1] - 2 > -1) and\
                (board[pos[0]-1][pos[1]-2] is None or board[pos[0]-1][pos[1]-2][0] != piece[0]):
            moves.append((pos[0]-1, pos[1]-2))
        if (pos[0] - 1 > -1 and pos[1] + 2 < 8) and \
                (board[pos[0]-1][pos[1]+2] is None or board[pos[0]-1][pos[1]+2][0] != piece[0]):
            moves.append((pos[0]-1, pos[1]+2))
        if (pos[0] - 2 > -1 and pos[1] - 1 > -1) and \
                (board[pos[0]-2][pos[1]-1] is None or board[pos[0]-2][pos[1]-1][0] != piece[0]):
            moves.append((pos[0]-2, pos[1]-1))
        if (pos[0] - 2 > -1 and pos[1] + 1 < 8) and \
                (board[pos[0]-2][pos[1]+1] is None or board[pos[0]-2][pos[1]+1][0] != piece[0]):
            moves.append((pos[0]-2, pos[1]+1))
        if (pos[0] + 1 < 8 and pos[1] - 2 > -1) and \
                (board[pos[0]+1][pos[1]-2] is None or board[pos[0]+1][pos[1]-2][0] != piece[0]):
            moves.append((pos[0]+1, pos[1]-2))
        if (pos[0] + 1 < 8 and pos[1] + 2 < 8) and \
                (board[pos[0]+1][pos[1]+2] is None or board[pos[0]+1][pos[1]+2][0] != piece[0]):
            moves.append((pos[0]+1, pos[1]+2))
        if (pos[0] + 2 < 8 and pos[1] - 1 > -1) and \
                (board[pos[0]+2][pos[1]-1] is None or board[pos[0]+2][pos[1]-1][0] != piece[0]):
            moves.append((pos[0]+2, pos[1]-1))
        if (pos[0] + 2 < 8 and pos[1] +1 < 8) and \
                (board[pos[0]+2][pos[1]+1] is None or board[pos[0]+2][pos[1]+1][0] != piece[0]):
            moves.append((pos[0]+2, pos[1]+1))

    ############### king ###############
    elif piece[1] == "k":
        if pos[0] - 1 > -1 and (board[pos[0] - 1][pos[1]] is None or board[pos[0] - 1][pos[1]][0] != piece[0]):
            moves.append((pos[0] - 1, pos[1]))
        if pos[0] - 1 > -1 and pos[1] - 1 > -1 and \
                (board[pos[0] - 1][pos[1] - 1] is None or board[pos[0] - 1][pos[1] - 1][0] != piece[0]):
            moves.append((pos[0]-1, pos[1]-1))
        if pos[0] - 1 > -1 and pos[1] + 1 < 8 and \
                (board[pos[0] - 1][pos[1] + 1] is None or board[pos[0] - 1][pos[1] + 1][0] != piece[0]):
            moves.append((pos[0] - 1, pos[1] + 1))
        if pos[1] + 1 < 8 and (board[pos[0]][pos[1] + 1] is None or board[pos[0]][pos[1] + 1][0] != piece[0]):
            moves.append((pos[0], pos[1] + 1))
        if pos[1] - 1 > -1 and (board[pos[0]][pos[1] - 1] is None or board[pos[0]][pos[1] - 1][0] != piece[0]):
            moves.append((pos[0], pos[1] - 1))
        if pos[0] + 1 < 8 and (board[pos[0] + 1][pos[1]] is None or board[pos[0] + 1][pos[1]][0] != piece[0]):
            moves.append((pos[0] + 1, pos[1]))
        if pos[0] + 1 < 8 and pos[1] - 1 > -1 and \
                (board[pos[0] + 1][pos[1] - 1] is None or board[pos[0] + 1][pos[1] - 1][0] != piece[0]):
            moves.append((pos[0] + 1, pos[1]-1))
        if pos[0] + 1 < 8 and pos[1] + 1 < 8 and \
                (board[pos[0] + 1][pos[1] + 1] is None or board[pos[0] + 1][pos[1] + 1][0] != piece[0]):
            moves.append((pos[0] + 1, pos[1] + 1))
        # if len(moves) > 0:
        #     checkmate = safety_check(moves, board, piece)


    ############### pawn ###############
    elif piece[1][0] == "p":

        if piece[0] == "w":
            if pos[0] - 1 > -1 and board[pos[0]-1][pos[1]] is None:
                moves.append((pos[0]-1, pos[1]))
            if pos[0] - 2 > -1 and board[pos[0]-2][pos[1]] is None and pos[0] == 6:
                moves.append((pos[0]-2, pos[1]))
            if pos[0] - 1 > -1 and pos[1] - 1 > -1 and\
                    board[pos[0]-1][pos[1]-1] is not None and board[pos[0]-1][pos[1]-1][0] != piece[0]:
                moves.append((pos[0]-1, pos[1]-1))
            if pos[0] - 1 > -1 and pos[1] + 1 < 8 and\
                    board[pos[0]-1][pos[1]+1] is not None and board[pos[0]-1][pos[1]+1][0] != piece[0]:
                moves.append((pos[0]-1, pos[1]+1))

        elif piece[0] == "b":
            if pos[0] + 1 < 8 and board[pos[0]+1][pos[1]] is None:
                moves.append((pos[0]+1, pos[1]))
            if pos[0] + 2 < 8 and board[pos[0]+2][pos[1]] is None and pos[0] == 1:
                moves.append((pos[0]+2, pos[1]))
            if pos[0] + 1 < 8 and pos[1] - 1 > -1 and \
                    board[pos[0]+1][pos[1]-1] is not None and board[pos[0]+1][pos[1]-1][0] != piece[0]:
                moves.append((pos[0]+1, pos[1]-1))
            if pos[0] + 1 < 8 and pos[1] + 1 < 8 and \
                    board[pos[0]+1][pos[1]+1] is not None and board[pos[0]+1][pos[1]+1][0] != piece[0]:
                moves.append((pos[0]+1, pos[1]+1))

    return moves, pos


def safety_check(board):
    for row in board:
        for piece in row:
            if piece is not None:
                moves, pos = legal_moves(board, piece)
                for move in moves:
                    if board[move[0]][move[1]] is not None and piece[0] != board[move[0]][move[1]][0] and board[move[0]][move[1]][1] == "k":
                        return True
    return False


def play(screen, mode, level=None):
    clock = pygame.time.Clock()
    board = LOGIC
    coord = draw_board(screen, board)
    coord_tiles = dict(zip(tiles, coord))
    board_tiles = dict(zip(tiles, [item for sublist in board for item in sublist]))
    moves = None
    pos = None
    turn = 0
    turn_dict = {0: "w", 1: "b"}
    tile = None
    check = False
    checkmate = False
    condition = None
    # if mode == "single player":
    #     fish = StockFish(getSFpath(), level)
    #     if not fish.isActive():
    #         return 1
    #     fish.startGame()
    while True:
        clock.tick(24)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                fish.close()
                return 0
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if pygame.Rect(50, 550, 120, 600).collidepoint(event.pos) or checkmate:
                    return 1
                if mode == "single player" and turn == 1:
                    continue
                x, y = event.pos
                for i in range(len(coord)):
                    if coord[i][0] < x < coord[i][0] + 60 and coord[i][1] < y < coord[i][1] + 60:
                        tile = list(coord_tiles.keys())[list(coord_tiles.values()).index(coord[i])]
                        if moves is not None:
                            for move in moves:
                                if i == move[0] * 8 + move[1]:
                                    if board[move[0]][move[1]] is not None and board[move[0]][move[1]][1] == "k":
                                        checkmate = True
                                        if mode == "multiplayer":
                                            condition = board[pos[0]][pos[1]][0]
                                    board[move[0]][move[1]] = board[pos[0]][pos[1]]
                                    board[pos[0]][pos[1]] = None
                                    board_tiles = dict(zip(tiles, [item for sublist in board for item in sublist]))
                                    draw_board(screen, board)
                                    moves = None
                                    turn = (turn + 1) % 2
                                    break
                        break
                check = safety_check(board)
        draw_board(screen, board)
        if checkmate:
            draw_board(screen, board)
            s = pygame.Surface((750, 650))
            s.set_alpha(128)
            s.fill((0, 0, 0))
            screen.blit(Game.CHECKMATE, (300, 20))
            screen.blit(s, (0, 0))
            if mode == "multiplayer":
                if condition == "w":
                    screen.blit(Game.WHITE_W, (270, 270))
                else:
                    screen.blit(Game.BLACK_W, (270, 270))
        elif check:
            screen.blit(Game.CHECK, (350, 20))
        x, y = pygame.mouse.get_pos()
        if 50 < x < 120 and 550 < y < 600:
            screen.blit(BACK_G, (50, 550))
        if tile and board_tiles[tile] and board_tiles[tile][0] == turn_dict[turn]:
            moves, pos = legal_moves(board, board_tiles[tile])
            draw_moves(screen, moves, board)
        pygame.display.update()
