
import copy

from engine.heuristics import *

INF = 1000000
DEPTH = 2


def evaluate(board):
    score = 0
    for i, row in enumerate(board):
        for j, piece in enumerate(row):
            if piece and piece[0] == "w":
                if piece[1][0] == "p":
                    score += 1 + pawnEvalWhite[i][j]
                elif piece[1][0] == "b":
                    score += 9 + bishopEvalWhite[i][j]
                elif piece[1][0] == "n":
                    score += 9 + knightEval[i][j]
                elif piece[1][0] == "r":
                    score += 14 + rookEvalWhite[i][j]
                elif piece[1][0] == "q":
                    score += 25 + queenEval[i][j]
                elif piece[1][0] == "k":
                    score += 200 + kingEvalWhite[i][j]
            elif piece and piece[0] == "b":
                if piece[1][0] == "p":
                    score -= 1 + pawnEvalBlack[i][j]
                elif piece[1][0] == "b":
                    score -= 9 + bishopEvalBlack[i][j]
                elif piece[1][0] == "n":
                    score -= 9 + knightEval[i][j]
                elif piece[1][0] == "r":
                    score -= 14 + rookEvalBlack[i][j]
                elif piece[1][0] == "q":
                    score -= 25 + queenEval[i][j]
                elif piece[1][0] == "k":
                    score -= 200 + kingEvalBlack[i][j]
    return score


def minimax(side, board, check, depth=DEPTH, alpha=-INF, beta=INF):
    from engine.moves import legal_moves, safety_check
    if depth == 0:
        return evaluate(board)
    if not side:
        best_val = -INF
        for row in board:
            for piece in row:
                if piece and piece[0] == "b":
                    moves, pos = legal_moves(board, piece)
                    for move in moves:
                        new_board = copy.deepcopy(board)
                        new_board[pos[0]][pos[1]] = piece
                        new_board[move[0]][move[1]] = new_board[pos[0]][pos[1]]
                        new_board[pos[0]][pos[1]] = None
                        if check and safety_check(new_board):
                            continue
                        node_val = minimax(not side, copy.deepcopy(new_board), check, depth - 1, alpha, beta)
                        if node_val > best_val:
                            best_val = node_val
                            if depth == DEPTH:
                                best_move = (list(pos), list(move))
                        alpha = max(alpha, best_val)
                        if alpha >= beta:
                            break
    else:
        best_val = INF
        for row in board:
            for piece in row:
                if piece and piece[0] == "b":
                    moves, pos = legal_moves(board, piece)
                    for move in moves:
                        new_board = copy.deepcopy(board)
                        new_board[pos[0]][pos[1]] = piece
                        new_board[move[0]][move[1]] = new_board[pos[0]][pos[1]]
                        new_board[pos[0]][pos[1]] = None
                        if check and safety_check(new_board):
                            continue
                        node_val = minimax(not side, copy.deepcopy(new_board), check, depth - 1, alpha, beta)
                        if node_val < best_val:
                            best_val = node_val
                            if depth == DEPTH:
                                best_move = (list(pos), list(move))
                        beta = min(beta, best_val)
                        if alpha >= beta:
                            break
    if depth == DEPTH:
        return best_move
    else:
        return best_val
