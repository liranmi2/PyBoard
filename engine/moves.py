
LOGIC = [[("b", "r1"), ("b", "n1"), ("b", "b1"), ("b", "q"), ("b", "k"), ("b", "b2"), ("b", "n2"), ("b", "r2")],
         [("b", "p1"), ("b", "p2"), ("b", "p3"), ("b", "p4"), ("b", "p5"), ("b", "p6"), ("b", "p7"), ("b", "p8")],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [None,       None,       None,       None,       None,       None,       None,       None],
         [("w", "p1"), ("w", "p2"), ("w", "p3"), ("w", "p4"), ("w", "p5"), ("w", "p6"), ("w", "p7"), ("w", "p8")],
         [("w", "r1"), ("w", "n1"), ("w", "b1"), ("w", "q"), ("w", "k"), ("w", "b2"), ("w", "n2"), ("w", "r2")]]


def legal_moves(board, piece):

    # direction = 1 if piece[0] == "b" else -1
    # start_row = pos[0] + 1 if direction == 1 else 8
    # end_row = 9 if direction == 1 else pos[0]
    # start_col = pos[1] + 1 if direction == 1 else 8
    # end_col = 9 if direction == 1 else pos[1]
    pos = [[i, row.index(piece)] for i, row in enumerate(board) if piece in row][0]
    moves = list()

    # rook
    if piece[1][0] == "r":
        print("rook")
        # down
        for i in range(pos[0]+1, 8):
            if board[i][pos[1]] is not None:
                break
            moves.append((i, pos[1]))

        # up
        for i in range(pos[0]-1, -1, -1):
            if board[i][pos[1]] is not None:
                break
            moves.append((i, pos[1]))

        # left
        for i in range(pos[1]+1, 8):
            if board[pos[0]][i] is not None:
                break
            moves.append((pos[0], i))

        # right
        for i in range(pos[1]-1, -1, -1):
            if board[pos[0]][i] is not None:
                break
            moves.append((pos[0], i))

    # bishop
    # elif piece[1] == "b":
    #
    # elif piece[1] == "n":
    #
    # elif piece[1] == "q":
    #
    # elif piece[1] == "k":
    #
    # elif piece[1] == "p":

    return moves, pos


