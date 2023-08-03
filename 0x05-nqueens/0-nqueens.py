#!/usr/bin/python3

"""
N Queens Problem Solver
"""
import sys


def is_safe(board, row, col, n):
    """Check if it's safe to place a queen at a specific position."""
    for i in range(row):
        if board[i][col] == 1:
            return False

    # Check upper left diagonal
    for i, j in zip(range(row, -1, -1), range(col, -1, -1)):
        if board[i][j] == 1:
            return False

    # Check upper right diagonal
    for i, j in zip(range(row, -1, -1), range(col, n)):
        if board[i][j] == 1:
            return False

    return True


def nqueens(board, row, n):
    """Solve N Queens problem using backtracking."""
    if row == n:
        queens_positions = []
        for i in range(n):
            for j in range(n):
                if board[i][j] == 1:
                    queens_positions.append([i, j])
        print(queens_positions)
        return

    for col in range(n):
        if is_safe(board, row, col, n):
            board[row][col] = 1
            nqueens(board, row + 1, n)
            board[row][col] = 0


def solve_nqueens(n):
    """Entry function to solve the N Queens problem."""
    if not n.isnumeric():
        print("N must be a number")
        sys.exit(1)

    n = int(n)
    if n < 4:
        print("N must be at least 4")
        sys.exit(1)

    board = [[0 for _ in range(n)] for _ in range(n)]
    nqueens(board, 0, n)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)

    solve_nqueens(sys.argv[1])
