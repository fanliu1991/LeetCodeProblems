'''
Write a program to solve a Sudoku puzzle by filling the empty cells.

A sudoku solution must satisfy all of the following rules:

1. Each of the digits 1-9 must occur exactly once in each row.
2. Each of the digits 1-9 must occur exactly once in each column.
3. Each of the the digits 1-9 must occur exactly once in each of the 9 3x3 sub-boxes of the grid.

Empty cells are indicated by the character '.'.

Note:

The given board contain only digits 1-9 and the character '.'.
You may assume that the given Sudoku puzzle will have a single unique solution.
The given board size is always 9x9.


Example 1:

Input: 
[
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]

Output: true

'''

import sys, optparse, os

class Solution(object):
    def solveSudoku(self, board):
        self.board = board
        self.solve()

    def solve(self):
        for row in range(9):
            for column in range(9):
                if self.board[row][column] == ".":
                    for possible_value in ["1","2","3","4","5","6","7","8","9"]:
                        if self.isValid(row, column, possible_value):
                            self.board[row][column] = possible_value
                            if self.solve():
                                return True
                            else:
                                self.board[row][column] = "."
                    return False

        # no empty cell is found, puzzle solved
        return True


    def isValid(self, row, column, value):
        subbox_row = row - row % 3
        subbox_column = column - column % 3

        for i in range(9):
            # check if current row has the value
            if self.board[row][i] == value:
                return False
            # check if current column has the value
            if self.board[i][column] == value:
                return False

        # check if current sub box has the value
        subbox_row = row - row % 3
        subbox_column = column - column % 3

        for i in range(subbox_row, subbox_row + 3):
            for j in range(subbox_column, subbox_column + 3):
                if self.board[i][j] == value:
                    return False
        
        return True


board = [
  ["5","3",".",".","7",".",".",".","."],
  ["6",".",".","1","9","5",".",".","."],
  [".","9","8",".",".",".",".","6","."],
  ["8",".",".",".","6",".",".",".","3"],
  ["4",".",".","8",".","3",".",".","1"],
  ["7",".",".",".","2",".",".",".","6"],
  [".","6",".",".",".",".","2","8","."],
  [".",".",".","4","1","9",".",".","5"],
  [".",".",".",".","8",".",".","7","9"]
]
solution = Solution()
result = solution.solveSudoku(board)
print result

'''
Complexity Analysis
Time complexity : O(logn).
    Binary search solution.

Space complexity : O(1).
    No extra space is used. Only two extra variables left and right are needed.
'''