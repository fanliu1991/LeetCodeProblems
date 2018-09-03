'''
Given two integers n and k,
return all possible combinations of k numbers out of 1 ... n.

Example:

Input: n = 4, k = 2

Output:
[
    [2,4],
    [3,4],
    [2,3],
    [1,2],
    [1,3],
    [1,4],
]

'''

import sys, optparse, os

class Solution(object):
    def combine(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: List[List[int]]
        """

        '''
        Two conditions for back track:
        (1) the stack length is already k
        (2) the current value is too large for the rest slots to fit 
        '''

        if k == 0 or k > n:
            return []

        res = []
        stack = []
        x = 1
        
        while True:
            # print(x, stack)
            if len(stack) == k:
                res.append(stack[:])

            if len(stack) < k and x <= n:
                stack.append(x)
                x += 1
            else: # len(stack) == k or x > n:
                x = stack.pop() + 1
                if x <= n:
                    stack.append(x)
                    x += 1
                if stack == []:
                    return res
        
#         simplified version
        
#         while True:
#             # print(x, stack)
#             if len(stack) == k:
#                 res.append(stack[:])
#             if len(stack) == k or x > n:
#                 if not stack:
#                     return res
#                 x = stack.pop() + 1
#             else:
#                 stack.append(x)
#                 x += 1



n = 4
k = 2

solution = Solution()
result = solution.combine(n, k)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the nums.

Space complexity : O(1).
    Nums are sorted in place and no extra space is used. Only extra variables are needed.

'''

