
LOGIC = [[("b", "r1"), ("b", "n1"), ("b", "b1"), ("b", "q"), ("b", "k"), ("b", "b2"), ("b", "n2"), ("b", "r2")],
         [("b", "p1"), ("b", "p2"), ("b", "p3"), ("b", "p4"), ("b", "p5"), ("b", "p6"), ("b", "p7"), ("b", "p8")],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [("w", "p1"), ("w", "p2"), ("w", "p3"), ("w", "p4"), ("w", "p5"), ("w", "p6"), ("w", "p7"), ("w", "p8")],
         [("w", "r1"), ("w", "n1"), ("w", "b1"), ("w", "q"), ("w", "k"), ("w", "b2"), ("w", "n2"), ("w", "r2")]]


def legal_moves(board, piece):

    pos = [[i, row.index(piece)] for i, row in enumerate(board) if piece in row][0]
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
        print("bishop")
        j = pos[1] + 1
        for i in range(pos[0]+1, 8):
            print(i, j)
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j += 1
            if j == 8:
                break

        j = pos[1] + 1
        for i in range(pos[0]-1, -1, -1):
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j += 1
            if j == 8:
                break

        j = pos[1] - 1
        for i in range(pos[0]-1, -1, -1):
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                break
            moves.append((i, j))
            j -= 1
            if j == -1:
                break

        j = pos[1] - 1
        for i in range(pos[0]+1, 8):
            if board[i][j] is not None:
                if board[i][j][0] != piece[0]:
                    moves.append((i, j))
                flag = 1
                break
            moves.append((i, j))
            j -= 1
            if j == -1:
                break

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

    # elif piece[1] == "k":
    ############### pawn ###############
    elif piece[1][0] == "p":

        if piece[0] == "w":
            if pos[0] - 1 > -1 and board[pos[0]-1][pos[1]] is None:
                moves.append((pos[0]-1, pos[1]))
            if pos[0] - 2 > -1 and board[pos[0]-2][pos[1]] is None and pos[0] == 6:
                moves.append((pos[0]-2, pos[1]))
            if pos[0] - 2 > -1 and pos[1] - 1 > -1 and\
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


