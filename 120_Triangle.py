'''
Given a triangle, find the minimum path sum from top to bottom.
Each step you may move to adjacent numbers on the row below.

Use O(n) extra space, where n is the total number of rows in the triangle

Example:

Input: given the following triangle
[
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

Output: 11

Explanation:
The minimum path sum from top to bottom is 2 + 3 + 5 + 1 = 11

'''

import sys, optparse, os

class Solution:
    def minimumTotal(self, triangle):
        """
        :type triangle: List[List[int]]
        :rtype: int
        """

        if not triangle:
            return 0

        if len(triangle) == 1:
            return triangle[0][0]

        prev_row = triangle[0]

        for row in range(1, len(triangle)):
            nums = [0 for _ in range(row+1)]
            nums[0] = prev_row[0] + triangle[row][0]
            nums[-1] = prev_row[-1] + triangle[row][-1]

            for i in range(1, row):
                nums[i] = min(prev_row[i-1], prev_row[i]) + triangle[row][i]

            prev_row = copy.deepcopy(nums)

        return min(prev_row)

        # bottom-up solution
        '''
        [
            [2],
            [3,4],
            [6,5,7],
            [4,1,8,3]
        ]
        '''
        result = [0] * (len(triangle) + 1)

        for row in triangle[::-1]:
            for i in range(len(row)):
                result[i] = row[i] + min(result[i], result[i+1])

        return result[0]





triangle = [
     [2],
    [3,4],
   [6,5,7],
  [4,1,8,3]
]

solution = Solution()
result = solution.minimumTotal(triangle)
print result

'''
Complexity Analysis
Time complexity: O(n^2).
    We need to compute 1, 2, 3, ..., n elements for row 0, 1, ..., n-1, respectively.


Space complexity: O(n)
    Extra space is used to store the minimum sum paths end at each element in current row.

'''
