'''
Given a m x n grid filled with non-negative numbers,
find a path from top left to bottom right
which minimizes the sum of all numbers along its path.

Note: You can only move either down or right at any point in time.

Example:

Input:
[
    [1,3,1],
    [1,5,1],
    [4,2,1]
]
Output: 7
Explanation: Because the path 1->3->1->1->1 minimizes the sum.

'''

import sys, optparse, os

class Solution(object):
    def minPathSum(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """

        # Dynamic Programming method

        if len(grid) == 0 or len(grid[0]) == 0:
            return 0
        else:
            m = len(grid)
            n = len(grid[0])

            for j in range(1, n):
                grid[0][j] += grid[0][j-1]

            for i in range(1, m):
                grid[i][0] += grid[i-1][0]

            for i in range(1, m):
                for j in range(1, n):
                    grid[i][j] = grid[i][j] + min(grid[i][j-1], grid[i-1][j])

            return grid[-1][-1]


grid = [
    [1,3,1],
    [1,5,1],
    [4,2,1]
]

solution = Solution()
result = solution.minPathSum(grid)
print result


'''
Complexity Analysis
Time complexity : O(n^2).

Space complexity : O(1).
    In place calculation, no extra space used.
'''
