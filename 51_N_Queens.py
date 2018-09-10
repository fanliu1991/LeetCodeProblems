'''
The n-queens puzzle is the problem of placing n queens on an n×n chessboard 
such that no two queens attack each other.

Given an integer n, return all distinct solutions to the n-queens puzzle.
Each solution contains a distinct board configuration of the n-queens' placement, 
where 'Q' and '.' both indicate a queen and an empty space respectively.

Example:
Input: 4

Output: [
 [".Q..",  // Solution 1
  "...Q",
  "Q...",
  "..Q."],

 ["..Q.",  // Solution 2
  "Q...",
  "...Q",
  ".Q.."]
]

Explanation: There exist two distinct solutions to the 4-queens puzzle as shown above.

'''

import sys, optparse, os

class Solution:
    def solveNQueens(self, n):
        """
        :type n: int
        :rtype: List[List[str]]
        """

        """
        Use the DFS helper function to find solutions recursively.
        A solution will be found when all n rows are occupied by n queens.

        On an n×n chessboard,
        queen can attack other queens in the same row, same column, and same diagonals.

        When a queen is located at (x, y), it occupies the row with index x, 
        the column with index y, 
        the diagonal from top left to bottom right with coordinates = x - y, 
        and diagonal from top right to bottom left with coordinates = x + y.

        """

        def dfs(occupied_columns, occupied_diagonals_LeftToRight, occupied_diagonals_RightToReft):
            occupied_rows = len(occupied_columns)
            if occupied_rows == n:
                current_sol = ["." * i + "Q" + (n-i-1) * "." for i in occupied_columns]
                result.append(current_sol)
            else:
                current_row_index = occupied_rows
                for col_index in range(n):
                    current_diagonals_LeftToRight = current_row_index - col_index
                    current_diagonals_RightToReft = current_row_index + col_index

                    if col_index in occupied_columns or \
                    current_diagonals_LeftToRight in occupied_diagonals_LeftToRight or \
                    current_diagonals_RightToReft in occupied_diagonals_RightToReft:
                        continue
                    else:
                        dfs(occupied_columns + [col_index], 
                            occupied_diagonals_LeftToRight + [current_diagonals_LeftToRight], 
                            occupied_diagonals_RightToReft + [current_diagonals_RightToReft])

        result = []

        occupied_columns = []
        occupied_diagonals_LeftToRight = []
        occupied_diagonals_RightToReft = []

        dfs(occupied_columns, occupied_diagonals_LeftToRight, occupied_diagonals_RightToReft)

        return result


n = 6

solution = Solution()
result = solution.solveNQueens(n)
print result


'''
Complexity Analysis
Time complexity : O(n^n).
    There are n possible choices for column at current row, 
    and when a column is selected, there are n possible choices for column at next row.

Space complexity : O(n)
    Extra space is used to store occupied columns and occupied diagonals.
'''

