'''
Given a m x n matrix, 
if an element is 0, set its entire row and column to 0. 

Do it in-place.

Example 1:

Input: 
[
    [1,1,1],
    [1,0,1],
    [1,1,1]
]
Output: 
[
    [1,0,1],
    [0,0,0],
    [1,0,1]
]

Example 2:

Input: 
[
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]
Output: 
[
    [0,0,0,0],
    [0,4,5,0],
    [0,3,1,0]
]

Follow up:

A straight forward solution using O(mn) space is probably a bad idea.
A simple improvement uses O(m + n) space, but still not the best solution.
Could you devise a constant space solution?

'''

import sys, optparse, os

class Solution(object):
    def setZeroes(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        '''
        Use the first row and the first column as marker,
        to store whether the corresponding row and column supposed to be filled with zeros.

        '''

        if not matrix:
            return []

        m, n = len(matrix), len(matrix[0])
        first_row_has_zero = not all(matrix[0])
        first_col_has_zero = False

        for i in range(m):
            if matrix[i][0] == 0:
                first_col_has_zero = True
                break

        # scan the matrix to decide which row and column supposed to be filled with zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][j] == 0:
                    matrix[i][0] = 0
                    matrix[0][j] = 0

        # set the zeros
        for i in range(1, m):
            for j in range(1, n):
                if matrix[i][0] == 0 or matrix[0][j] == 0:
                    matrix[i][j] = 0

        if first_row_has_zero:
            matrix[0] = [0] * n

        if first_col_has_zero:
            for i in range(1, m):
                matrix[i][0] = 0


matrix = [
    [0,1,2,0],
    [3,4,5,2],
    [1,3,1,5]
]

solution = Solution()
result = solution.setZeroes(matrix)
print result

'''
Complexity Analysis
Time complexity : O(mn).
    We are doing one pass through the matrix.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
