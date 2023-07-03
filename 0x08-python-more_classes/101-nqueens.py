#!/usr/bin/python3

import sys


def is_valid(board, row, col, N):
    '''Check if there is a queen in the same column'''
    for i in range(row):
        if board[i][col] == 'Q':
            return False

    '''Check if there is a queen in the upper-left diagonal'''
    i = row - 1
    j = col - 1
    while i >= 0 and j >= 0:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j -= 1

    ''' Check if there is a queen in the upper-right diagonal'''
    i = row - 1
    j = col + 1
    while i >= 0 and j < N:
        if board[i][j] == 'Q':
            return False
        i -= 1
        j += 1

    return True


def solve_n_queens(board, row, N):
    if row == N:
        # Found a solution, print the board
        for i in range(N):
            print(" ".join(board[i]))
        print()
        return

    for col in range(N):
        if is_valid(board, row, col, N):
            board[row][col] = 'Q'
            solve_n_queens(board, row + 1, N)
            board[row][col] = '.'


def n_queens(N):
    board = [['.' for _ in range(N)] for _ in range(N)]
    solve_n_queens(board, 0, N)


if __name__ == "__main__":
    N = int(sys.argv[1])
    n_queens(N)
