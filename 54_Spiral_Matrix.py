'''
Given a matrix of m x n elements (m rows, n columns),
return all elements of the matrix in spiral order.


Example 1:

Input:
[
    [ 1, 2, 3 ],
    [ 4, 5, 6 ],
    [ 7, 8, 9 ]
]

Output: [1,2,3,6,9,8,7,4,5]


Example 2:

Input:
[
    [1, 2, 3, 4],
    [5, 6, 7, 8],
    [9,10,11,12]
]

Output: [1,2,3,4,8,12,11,10,9,5,6,7]

'''

import sys, optparse, os

class Solution(object):
    def spiralOrder(self, matrix):
        """
        :type matrix: List[List[int]]
        :rtype: List[int]
        """

        if not matrix:
            return []

        row_num = len(matrix)
        col_num = len(matrix[0])

        if row_num == 1:
            return matrix[0]
        elif col_num == 0:
            return []
        elif col_num == 1:
            return [row[0] for row in matrix]
        else:
            spiral_order = []
            # firsr row
            spiral_order += matrix[0]
            # last element from the second row to the second last row
            for row_index in range(1, row_num-1):
                spiral_order += [matrix[row_index][-1]]
            # last row
            matrix[-1].reverse()
            spiral_order += matrix[-1]
            # first element from the second last row to the second row
            for row_index in range(row_num-2, 0, -1):
                spiral_order += [matrix[row_index][0]]

            return spiral_order + self.spiralOrder([matrix[row_index][1:col_num-1] for row_index in range(1, row_num-1)])

        # generator method
        '''
        [     c1                 c2
        r1    [1, 1, 1, 1, 1, 1, 1],
              [1, 2, 2, 2, 2, 2, 1],
              [1, 2, 3, 3, 3, 2, 1],
              [1, 2, 2, 2, 2, 2, 1],
        r2    [1, 1, 1, 1, 1, 1, 1]
         ]
        '''
        '''
        def spiral_coords(r1, c1, r2, c2):
            for c in range(c1, c2 + 1):
                yield r1, c
            for r in range(r1 + 1, r2 + 1):
                yield r, c2
            if r1 < r2 and c1 < c2:
                for c in range(c2 - 1, c1, -1):
                    yield r2, c
                for r in range(r2, r1, -1):
                    yield r, c1

        if not matrix: return []
        spiral_order = []
        r1, r2 = 0, len(matrix) - 1
        c1, c2 = 0, len(matrix[0]) - 1
        while r1 <= r2 and c1 <= c2:
            for r, c in spiral_coords(r1, c1, r2, c2):
                spiral_order.append(matrix[r][c])
            r1 += 1; r2 -= 1
            c1 += 1; c2 -= 1
        return spiral_order
        '''


matrix = [[1,11],[2,12],[3,13],[4,14],[5,15],[6,16],[7,17],[8,18],[9,19],[10,20]]

solution = Solution()
result = solution.spiralOrder(matrix)
print result


'''
Complexity Analysis
Time complexity : O(n). 
     where n is the total number of elements in the input matrix.
     We add every element in the matrix to our final answer.

Space complexity : O(n).
    The information stored in spiral_order.
'''
