'''
Given a 2D binary matrix filled with 0's and 1's,
find the largest rectangle containing only 1's and return its area.


Example 1:
Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6
'''

import sys, optparse, os

class Solution:
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """

        """
        For each row i,
            for each col j,
                if row[j] == "1", 
                    height[j] = number of continuous "1" above current row[j]
                    l = left[j] is the last coordinate to the left 
                        where all rows in the height[j] from row[l] to row[j] are "1", 
                    r = right[j] is the last coordinate to the right 
                        where all rows in the height[j] from row[j] to row[r-1] are "1".

                if row[j] != "1",
                    its left[j] = 0 and right[j] = n, with height[j] = 0.
                    
            compute the maximal area of "1" in the area between row[0] and row[i]

        """

        if not matrix or not matrix[0]:
            return 0

        m = len(matrix)
        n = len(matrix[0])

        left = [0 for _ in range(n)]
        right = [n for _ in range(n)]
        height = [0 for _ in range(n)]

        max_area = 0
 
        for i in range(m):

            for j in range(n):
                if matrix[i][j] == "1":
                    height[j] += 1
                else:
                    height[j] = 0

            current_left = 0
            for j in range(n):
                if matrix[i][j] == "1":
                    left[j] = max(left[j], current_left)
                else:
                    left[j] = 0
                    current_left = j + 1

            current_right = n
            for j in range(n-1, -1, -1):
                if matrix[i][j] == "1":
                    right[j] = min(right[j], current_right)
                else:
                    right[j] = n
                    current_right = j

            # print(height, left, right)
            for j in range(n):
                max_area = max(max_area, height[j] * (right[j] - left[j]))

        return max_area


matrix = [
  ["1","0","1","1","0"],
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]

solution = Solution()
result = solution.maximalRectangle(matrix)
print result



'''
Complexity Analysis
Time complexity : O(m*n).
    This solution proceeds matrix row by row, from the first column to the last one.

Space complexity : O(n).
    Extra space is used to store height, left and right.

'''

