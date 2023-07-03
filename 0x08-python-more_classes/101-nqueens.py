#!/usr/bin/python3
"""Solves the N-queens puzzle.

Determines all possible solutions to placing N non-attacking queens on an NxN chessboard.

Example:
    $ ./101-nqueens.py N

N must be an integer greater than or equal to 4.

Attributes:
    chessboard (list): A list of lists representing the chessboard.
    solutions (list): A list of lists containing solutions.

Solutions are represented in the format [[r, c], [r, c], [r, c], [r, c]],
where `r` and `c` represent the row and column, respectively, where a
queen must be placed on the chessboard.
"""
import sys


def init_chessboard(n):
    """Initialize an `n`x`n` sized chessboard with empty spaces."""
    chessboard = []
    [chessboard.append([]) for _ in range(n)]
    [row.append(' ') for _ in range(n) for row in chessboard]
    return chessboard


def deepcopy_chessboard(chessboard):
    """Return a deepcopy of a chessboard."""
    if isinstance(chessboard, list):
        return list(map(deepcopy_chessboard, chessboard))
    return chessboard


def get_solution(chessboard):
    """Return the list of lists representation of a solved chessboard."""
    solution = []
    for r in range(len(chessboard)):
        for c in range(len(chessboard)):
            if chessboard[r][c] == "Q":
                solution.append([r, c])
                break
    return solution


def mark_non_attacking_spots(chessboard, row, col):
    """Mark spots on the chessboard as non-attacking.

    Mark all spots where non-attacking queens can no
    longer be placed on the chessboard.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The row where a queen was last placed.
        col (int): The column where a queen was last placed.
    """
    # Mark all spots in the same row as non-attacking
    for c in range(col + 1, len(chessboard)):
        chessboard[row][c] = "x"

    # Mark all spots in the same column as non-attacking
    for r in range(row + 1, len(chessboard)):
        chessboard[r][col] = "x"

    # Mark all spots diagonally to the right and downwards as non-attacking
    c = col + 1
    for r in range(row + 1, len(chessboard)):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1

    # Mark all spots diagonally to the left and upwards as non-attacking
    c = col - 1
    for r in range(row - 1, -1, -1):
        if c < 0:
            break
        chessboard[r][c] = "x"
        c -= 1

    # Mark all spots diagonally to the right and upwards as non-attacking
    c = col + 1
    for r in range(row - 1, -1, -1):
        if c >= len(chessboard):
            break
        chessboard[r][c] = "x"
        c += 1

    # Mark all spots diagonally to the left and downwards as non-attacking
    c = col - 1
    for r in range(row + 1, len(chessboard)):
        if c < 0:
            break
        chessboard[r][c] = "x"


def solve_nqueens(chessboard, row, queens, solutions):
    """Recursively solve an N-queens puzzle.

    Args:
        chessboard (list): The current working chessboard.
        row (int): The current working row.
        queens (int): The current number of placed queens.
        solutions (list): A list of lists of solutions.
    Returns:
        solutions (list): A list of lists containing solutions.
    """
    if queens == len(chessboard):
        solutions.append(get_solution(chessboard))
        return solutions

    for col in range(len(chessboard)):
        if chessboard[row][col] == " ":
            tmp_chessboard = deepcopy_chessboard(chessboard)
            tmp_chessboard[row][col] = "Q"
            mark_non_attacking_spots(tmp_chessboard, row, col)
            solutions = solve_nqueens(tmp_chessboard, row + 1, queens + 1, solutions)

    return solutions


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    if sys.argv[1].isdigit() is False:
        print("N must be a number")
        sys.exit(1)
    if int(sys.argv[1]) < 4:
        print("N must be at least 4")
        sys.exit(1)

    n = int(sys.argv[1])
    chessboard = init_chessboard(n)
    solutions = solve_nqueens(chessboard, 0, 0, [])
    for sol in solutions:
        print(sol)
