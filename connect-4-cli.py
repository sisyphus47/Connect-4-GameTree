import numpy as np
import re


ROW_COUNT = 6
COLUMN_COUNT = 7


def create_board():
    board = np.zeros((ROW_COUNT, COLUMN_COUNT))
    return board


def drop_piece(board, row, col, piece):
    board[row][col] = piece


def is_valid_location(board, col):
    return board[0][col] == 0


def get_next_open_row(board, col):
    for r in range(ROW_COUNT - 1, -1, -1):
        if board[r][col] == 0:
            return r


def winning_move(board, piece):
    p = re.compile("(" + str(piece) + ".( )?){4}")
    # vertical
    for c in range(COLUMN_COUNT):
        if p.search(str(board[:, c])) is not None:
            return True

    # horizontal
    for r in range(ROW_COUNT):
        if p.search(str(board[r, :])) is not None:
            return True

    # diagonal
    for offset in range(-ROW_COUNT + 4, COLUMN_COUNT - 3):
        if (
            p.search(str(np.diagonal(board, offset))) is not None
            or p.search(str(np.diagonal(np.flip(board, 1), offset))) is not None
        ):
            return True


board = create_board()
game_over = False
turn = 0

while not game_over:
    if turn == 0:

        col = int(input("Player 1 Make your Selection(0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 1)
            print(board)
            turn += 1
            if winning_move(board, 1):
                print("Player 1 Wins!!!")
                game_over = True

    else:

        col = int(input("Player 2 Make your Selection(0-6):"))
        if is_valid_location(board, col):
            row = get_next_open_row(board, col)
            drop_piece(board, row, col, 2)
            print(board)
            turn -= 1
            if winning_move(board, 1):
                print("Player 1 Wins!!!")
                game_over = True
