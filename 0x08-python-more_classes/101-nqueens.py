#!/usr/bin/python3

"""

N-Queens Problem Solver

Usage: nqueens N

This program solves the N-Queens problem, which is the challenge of placing N non-attacking queens on an N×N chessboard.

It prints every possible solution to the problem, with one solution per line.

Arguments:

N - An integer representing the size of the chessboard and the number of queens.

Exit Status:

1 - If the user called the program with the wrong number of arguments or invalid argument values.

Example:

$ python nqueens.py 4

.Q..

...Q

Q...

..Q.

"""

import sys

def is_safe(board, row, col):

    """

    Check if it is safe to place a queen at the specified position on the board.

    Args:

    board - A list of lists representing the chessboard.

    row - The current row to be checked.

    col - The current column to be checked.

    Returns:

    True if it is safe to place a queen, False otherwise.

    """

    # Check if there is a queen in the same column

    for i in range(row):

        if board[i][col] == 'Q':

            return False

    # Check if there is a queen in the upper left diagonal

    i, j = row, col

    while i >= 0 and j >= 0:

        if board[i][j] == 'Q':

            return False

        i -= 1

        j -= 1

    # Check if there is a queen in the upper right diagonal

    i, j = row, col

    while i >= 0 and j < len(board):

        if board[i][j] == 'Q':

            return False

        i -= 1

        j += 1

    return True

def solve_nqueens(n):

    """

    Solve the N-Queens problem and return a list of all possible solutions.

    Args:

    n - An integer representing the size of the chessboard and the number of queens.

    Returns:

    A list of lists representing all possible solutions to the N-Queens problem.

    """

    board = [['.' for _ in range(n)] for _ in range(n)]

    solutions = []

    def backtrack(row):

        if row == n:

            solutions.append([''.join(row) for row in board])

            return

        for col in range(n):

            if is_safe(board, row, col):

                board[row][col] = 'Q'

                backtrack(row + 1)

                board[row][col] = '.'

    backtrack(0)

    return solutions

def print_solutions(solutions):

    """

    Print all the solutions to the N-Queens problem.

    Args:

    solutions - A list of lists representing all the solutions.

    """

    for solution in solutions:

        for row in solution:

            print(row)

        print()

def main():

    """

    Main entry point of the program.

    """

    if len(sys.argv) != 2:

        print("Usage: nqueens N")

        sys.exit(1)

    try:

        n = int(sys.argv[1])

    except ValueError:

        print("N must be a number")

        sys.exit(1)

    if n < 4:

        print("N must be at least 4")

        sys.exit(1)

    solutions = solve_nqueens(n)

    print_solutions(solutions)

if __name__ == '__main__':

    main()

