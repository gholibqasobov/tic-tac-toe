"""
Tic Tac Toe Player
"""

import math

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
    # raise NotImplementedError
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
    # raise NotImplementedError
    for i in range(len(board)):
        for j in range(len(board[i])):
            if board[i][j] == EMPTY:
                options.add((i, j))
    return options


def result(board, action):
    """
    Returns the board that results from making move (i, j) on the board.
    """
    row, col = action
    # raise NotImplementedError
    if board[row][col] == EMPTY:
        board[row][col] = player(board)
        return board
    else:
        return 'Invalid choice'


def winner(board):
    """
    Returns the winner of the game, if there is one.
    """
    # raise NotImplementedError
    """
    [[EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]]
    """

    val = None
    diag = []
    rev_diag = []
    for i in range(3):
        vertical = []
        if board[i].count(X) == 3:
            val = X
        elif board[i].count(O) == 3:
            val = O
        for j in range(3):
            vertical.append(board[j][i])
            if i == j:
                diag.append(board[i][j])
            if i + j == 2:
                rev_diag.append(board[i][j])
        if vertical.count(X) == 3:
            val = X
        elif vertical.count(O) == 3:
            val = O

    if diag.count(X) == 3 or rev_diag.count(X) == 3:
        val = X
    elif diag.count(O) == 3 or rev_diag.count(O) == 3:
        val = O

    return val


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    # raise NotImplementedError
    if winner(board) is not None:
        return True
    else:
        for i in range(3):
            if not all(board[i]):
                return False

    return False


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    # raise NotImplementedError
    if winner(board) == 'X':
        return 1
    elif winner(board) == 'O':
        return -1
    else:
        return 0


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError
