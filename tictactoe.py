"""
Tic Tac Toe Player
"""

import math

X = "X"
O = "O"
EMPTY = None
board = [
    [X, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY],
    [EMPTY, EMPTY, EMPTY]
]

# board = [
#     [EMPTY, O, X],
#     [O, X, EMPTY],
#     [X, O, X]
# ]


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


# print(actions(board))

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
    'hello world'


def terminal(board):
    """
    Returns True if game is over, False otherwise.
    """
    raise NotImplementedError


def utility(board):
    """
    Returns 1 if X has won the game, -1 if O has won, 0 otherwise.
    """
    raise NotImplementedError


def minimax(board):
    """
    Returns the optimal action for the current player on the board.
    """
    raise NotImplementedError






# print(x_count, y_count)