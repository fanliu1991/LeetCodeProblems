'''
Given an n x n 2D matrix representing an image.
Rotate the image by 90 degrees (clockwise).

Note:
You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
DO NOT allocate another 2D matrix and do the rotation.

Example 1:

Input:
[
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

Output: 
[
    [7,4,1],
    [8,5,2],
    [9,6,3]
]

Example 2:

Input:
[
    [ 5, 1, 9,11],
    [ 2, 4, 8,10],
    [13, 3, 6, 7],
    [15,14,12,16]
], 

Output:
[
    [15,13, 2, 5],
    [14, 3, 4, 1],
    [12, 6, 8, 9],
    [16, 7,10,11]
]


'''

import sys, optparse, os

class Solution(object):
    def rotate(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: void Do not return anything, modify matrix in-place instead.
        """

        '''
        Common method to solve the image rotation problems:

        *** clockwise rotate
            first reverse up to down, then swap the symmetry, matrix[i][j] <=> matrix[j][i]
                1 2 3     7 8 9     7 4 1
                4 5 6  => 4 5 6  => 8 5 2
                7 8 9     1 2 3     9 6 3

        *** anticlockwise rotate
                first reverse left to right, then swap the symmetry, matrix[i][j] <=> matrix[j][i]
                1 2 3     3 2 1     3 6 9
                4 5 6  => 6 5 4  => 2 5 8
                7 8 9     9 8 7     1 4 7

        for i in range(len(matrix_length)):
            for j in range(i+1, matrix_length):
                swap(matrix[i][j], matrix[j][i])

        '''

        if not matrix:
            return [[]]

        # rotate matrix by mirror inversion
        # so 
        # [
        #     [1,2,3],
        #     [4,5,6],
        #     [7,8,9]
        # ]
        # becomes
        # [
        #     [3,2,1],
        #     [6,5,4],
        #     [9,8,7]
        # ]
        matrix_row_length = len(matrix[0])
        for row in matrix:
            for i in range(matrix_row_length/2):
                temp = row[i]
                row[i] = row[matrix_row_length - 1 - i]
                row[matrix_row_length - 1 - i] = temp

        # then swap the matrix symmetrically (by up-left to bottom-right symmetry)
        for i in range(matrix_row_length):
            for j in range(matrix_row_length - i):
                temp = matrix[i][j]
                matrix[i][j] = matrix[matrix_row_length - 1 - j][matrix_row_length - 1 - i]
                matrix[matrix_row_length - 1 - j][matrix_row_length - 1 - i] = temp

        return matrix


matrix = [
    [1,2,3],
    [4,5,6],
    [7,8,9]
]

# matrix = [
#     [ 5, 1, 9,11],
#     [ 2, 4, 8,10],
#     [13, 3, 6, 7],
#     [15,14,12,16]
# ]


solution = Solution()
result = solution.rotate(matrix)
print result


'''
Complexity Analysis
Time complexity : O(n^2).
    Processing on half of elements in n x n matrix is needed.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
