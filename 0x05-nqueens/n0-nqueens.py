#!/usr/bin/python3
"""Solve the N queens problem using backtracking"""
import sys


def print_board(board):
    """Print the board solution"""
    solution = [[i, board[i]] for i in range(len(board))]
    print(solution)


def is_safe(board, row, col):
    """Check if a queen can be placed on board[row][col]"""
    for i in range(col):
        if board[i] == row or \
                board[i] - i == row - col or \
                board[i] + i == row + col:
            return False
    return True


def solve_n_queens(board, col):
    """Use backtracking to find all solutions"""
    N = len(board)
    if col == N:
        print_board(board)
        return

    for row in range(N):
        if is_safe(board, row, col):
            board[col] = row
            solve_n_queens(board, col + 1)


def n_queens(N):
    """Solve the N queens problem"""
    board = [-1] * N
    solve_n_queens(board, 0)


if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Usage: nqueens N")
        sys.exit(1)
    try:
        N = int(sys.argv[1])
    except ValueError:
        print("N must be a number")
        sys.exit(1)
    if N < 4:
        print("N must be at least 4")
        sys.exit(1)
    n_queens(N)
