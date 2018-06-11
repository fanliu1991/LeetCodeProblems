'''
Write an efficient algorithm that searches for a value in an m x n matrix.

This matrix has the following properties:
1. Integers in each row are sorted from left to right.
2. The first integer of each row is greater than the last integer of the previous row.


Example 1:

Input:
matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 3

Output: true

Example 2:

Input: 
matrix = [
    [1,   3,  5,  7],
    [10, 11, 16, 20],
    [23, 30, 34, 50]
]
target = 13

Output: false

'''

import sys, optparse, os

class Solution(object):
    def searchMatrix(self, matrix, target):
        """
        :type matrix: List[List[int]]
        :type target: int
        :rtype: bool
        """

        if not matrix or not matrix[0]:
            return False

        m, n = len(matrix), len(matrix[0])

        if target > matrix[-1][-1]:
            return False
        else:
            for i in range(m):
                if matrix[i][-1] >= target:
                    row = matrix[i]
                    break

        if target < row[0]:
            return False
        else:
            left, right = 0, n
            while left < right:
                middle = (left + right) / 2
                if row[middle] == target:
                    return True
                elif row[middle] < target:
                    left = middle + 1
                else:
                    right = middle
            return False

        '''
        Or we can simply not treat it as a 2D matrix,
        but just treat it as a sorted list.
        '''

        left, right = 0, m * n - 1
        
        while left <= right:
            middle = (left + right) / 2
            num = matrix[middle / n][middle % n]

            if num == target:
                return True
            elif num < target:
                left = middle + 1
            else:
                right = middle - 1
        
        return False


path = "//home/a/./b/../../c/"

solution = Solution()
result = solution.simplifyPath(path)
print result

'''
Complexity Analysis
Time complexity : O(mn).
    We are doing one pass through the matrix.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
