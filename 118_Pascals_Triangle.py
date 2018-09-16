'''
Given a non-negative integer numRows, 
generate the first numRows of Pascal's triangle

In Pascal's triangle, 
each number is the sum of the two numbers directly above it.

Example:
Input: 5

Output: 
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

'''

import sys, optparse, os

class Solution:
    def generate(self, numRows):
        """
        :type numRows: int
        :rtype: List[List[int]]
        """

        if not numRows:
            return []

        result = []

        for row in range(numRows):
            nums = [1 for _ in range(row+1)]
            nums[0], nums[-1] = 1, 1

            for i in range(1, row):
                nums[i] = result[row-1][i-1] + result[row-1][i]
            result.append(nums)

        return result

        # map solution
        '''
        Any row can be constructed using the offset sum of the previous row.
        Example:
                1 3 3 1 0 
             +  0 1 3 3 1
             =  1 4 6 4 1
        '''

        res = [[1]]

        for i in range(1, numRows):
            res = res + [map(lambda x, y: x+y, res[-1] + [0], [0] + res[-1])]
        return res if numRows else []



numRows = 5

solution = Solution()
result = solution.generate(numRows)
print result


'''
Complexity Analysis
Time complexity : O(n^2).
    We need to compute 1, 2, 3, ..., n elements for row 0, 1, ..., n-1, respectively.

Space complexity : O(n^2).
    We need to store 1, 2, 3, ..., n elements for row 0, 1, ..., n-1, respectively.

'''

