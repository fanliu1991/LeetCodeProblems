'''
Given a non-negative index k where k ≤ 33, 
return the k-th index row of the Pascal's triangle.

Note that the row index starts from 0.

In Pascal's triangle, 
each number is the sum of the two numbers directly above it.

Example:
Input: 3
Output: [1,3,3,1]

Explanation: 
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
    def getRow(self, rowIndex):
        """
        :type rowIndex: int
        :rtype: List[int]
        """

        '''
        When generating each row, we can use the previous row directly.
        For each new row, we append a 1 to the head of previous row, 
        and let i iterate from row[2] to row[-2], 
        and set row[i] = row[i] + row[i+1]

        e.g.
        row index = 4, previous row = [1,3,3,1]
        append a 1 to previous row, row = [1,1,3,3,1]
        after row[i] = row[i] + row[i+1],
        row = [1,4,6,4,1]
        '''

        result = []

        for _ in range(rowIndex+1):
            result = [1] + result
            for i in range(1, len(result)-1) :
                result[i] = result[i] + result[i+1]

        return result

        # simple solution
        '''
        Any row can be constructed using the offset sum of the previous row.
        Example:
                1 3 3 1 0 
             +  0 1 3 3 1
             =  1 4 6 4 1
        '''

        # row = [1]
        # for _ in range(rowIndex):
        #     row = [x + y for x, y in zip([0]+row, row+[0])]
        # return row


numRows = 5

solution = Solution()
result = solution.getRow(rowIndex)
print result


'''
Complexity Analysis
Time complexity : O(k^2).
    We need to compute k-2 elements for k-th row.

Space complexity : O(k).
    We need k+1 spaces to store the k-th row.

'''

