"""
Tic Tac Toe Player
"""

import math
import copy

X = "X"
O = "O"
EMPTY = None


def initial_state():
    """
    Returns starting state of the board.
    """
    return [[EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY],
            [EMPTY, EMPTY, EMPTY]]


def player(board):
    """
    Returns player who has the next turn on a board.
    """
    x_count = 0
    o_count = 0
    for row in board:
        x_count += row.count(X)
        o_count += row.count(O)

    if x_count == 0 or x_count == o_count:
        return X
    else:
        return O


def actions(board):
    """
    Returns set of all possible actions (i, j) available on the board.
    """
    options = set()
    for i in range(3):
        for j in range(3):
            if board[i][j] == EMPTY:
                options.add((i, j))
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    board_copy = copy.deepcopy(board)
    row, col = action
    if board_copy[row][col] == EMPTY:
        board_copy[row][col] = player(board)
        return board_copy
    else:
        raise Exception('The cell is Full!')


def row_win(board):
    for row in board:
        if row.count(X) == 3:
            return X
        elif row.count(O) == 3:
            return O
    return None


def col_win(board):
    for i in range(3):
        col = []
        for j in range(3):
            col.append(board[j][i])
        if col.count(X) == 3:
            return X
        if col.count(O) == 3:
            return O
    return None


def diag_win(board):
    right_diag = []
    left_diag = []
    for i in range(3):
        for j in range(3):
            if i == j:
                left_diag.append(board[i][j])
            if i + j == 2:
                right_diag.append(board[i][j])

    if left_diag.count(X) == 3 or right_diag.count(X) == 3:
        return X
    elif left_diag.count(O) == 3 or right_diag.count(O) == 3:
        return O

    return None


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    if row_win(board) is not None:
        return row_win(board)
    elif col_win(board) is not None:
        return col_win(board)
    elif diag_win(board) is not None:
        return diag_win(board)
    return None


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    if winner(board) is not None:
        return True
    else:
        for i in range(3):
            if board[i].count(EMPTY) != 0:
                return False
        return True


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    elif winner(board) is None:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    if player(board) == X:
        for action in actions(board):
            if min_val(result(board, action)) == max_val(board):
                return action
    elif player(board) == O:
        for action in actions(board):
            if max_val(result(board, action)) == min_val(board):
                return action


def max_val(board):
    if terminal(board):
        return utility(board)
    v = -math.inf
    for action in actions(board):
        v = max(v, min_val(result(board, action)))
    return v


def min_val(board):
    if terminal(board):
        return utility(board)
    v = math.inf
    for action in actions(board):
        v = min(v, max_val(result(board, action)))
    return v
