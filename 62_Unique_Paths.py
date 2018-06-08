'''
A robot is located at the top-left corner of a m x n grid.

The robot can only move either down or right at any point in time. 
The robot is trying to reach the bottom-right corner of the grid.

How many possible unique paths are there?

Note: m and n will be at most 100.

Example 1:

Input: m = 2, n = 3
Output: 3

Explanation:
From the top-left corner, there are a total of 3 ways to reach the bottom-right corner:
1. Right -> Right -> Down
2. Right -> Down -> Right
3. Down -> Right -> Right

Example 2:

Input: m = 7, n = 3
Output: 28

'''

import sys, optparse, os

class Solution(object):
    def uniquePaths(self, m, n):
        """
        :type m: int
        :type n: int
        :rtype: int
        """

        # Dynamic Programming method

        if m == 0 or n == 0:
            return 0
        elif m == 1 or n == 1:
            return 1
        else:
            grid = [[1 for _ in range(n)] for _ in range(m)]
            for i in range(1, m):
                for j in range(1, n):
                    grid[i][j] = grid[i][j-1] + grid[i-1][j]
            return grid[-1][-1]

        # Binomial coefficient (combination) method
        """
        To reach the bottom-right corner from the top-left corner,
        we need to do n + m -2 movements, m - 1 down, n - 1 right.

        The path is the sequence of movements ( go down / go right),
        so we choose (n - 1) movements as number of steps to the right from (m + n - 2),
        then rest (m - 1) is number of steps down,
                ( m + n - 2 )          (m + n - 2) !
        i.e.    -------------   =  ----------------------
                (   n - 1   )       (n - 1) ! * (m - 1) !

        """

        # import math
        # res = math.factorial(m+n-2) / math.factorial(m-1) / math.factorial(n-1)
        # return res


m = 7
n = 3

solution = Solution()
result = solution.uniquePaths(m, n)
print result


'''
Complexity Analysis
Time complexity : O(n^2).

Space complexity : O(n^2).
'''
