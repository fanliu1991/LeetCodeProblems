'''
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.

Now consider if some obstacles are added to the grids.
How many possible unique paths are there?

Note: m and n will be at most 100.
      An obstacle and empty space is marked as 1 and 0 respectively in the grid.

Example:

Input:
[
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

Output: 2

Explanation:
There is one obstacle in the middle of the 3x3 grid above.
There are two ways to reach the bottom-right corner:
1. Right -> Right -> Down -> Down
2. Down -> Down -> Right -> Right

'''

import sys, optparse, os

class Solution(object):
    def uniquePathsWithObstacles(self, obstacleGrid):
        """
        :type obstacleGrid: List[List[int]]
        :rtype: int
        """

        # Dynamic Programming method

        if len(obstacleGrid) == 0 or len(obstacleGrid[0]) == 0 or obstacleGrid[0][0] == 1:
            return 0
        elif len(obstacleGrid) == 1:
            if 1 in obstacleGrid[0]:
                return 0
            else:
                return 1
        elif len(obstacleGrid[0]) == 1:
            for row in obstacleGrid:
                if 1 in row:
                    return 0
            return 1
        else:
            m = len(obstacleGrid)
            n = len(obstacleGrid[0])
            grid = [[1 for _ in range(n)] for _ in range(m)]

            for j in range(1, n):
                if obstacleGrid[0][j] == 0:
                    grid[0][j] = grid[0][j-1]
                else:
                    grid[0][j] = 0

            for i in range(1, m):
                if obstacleGrid[i][0] == 0:
                    grid[i][0] = grid[i-1][0]
                else:
                    grid[i][0] = 0

            for i in range(1, m):
                for j in range(1, n):
                    if obstacleGrid[i][j] == 1:
                        grid[i][j] = 0
                    else:
                        grid[i][j] = grid[i][j-1] + grid[i-1][j]

            return grid[-1][-1]


obstacleGrid = [
  [0,0,0],
  [0,1,0],
  [0,0,0]
]

solution = Solution()
result = solution.uniquePathsWithObstacles(obstacleGrid)
print result


'''
Complexity Analysis
Time complexity : O(n^2).

Space complexity : O(n^2).
'''
