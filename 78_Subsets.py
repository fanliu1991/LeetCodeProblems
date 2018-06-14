'''
Given a set of distinct integers, nums,
return all possible subsets (the power set).

Note: The solution set must not contain duplicate subsets.


Example:

Input: nums = [1,2,3]

Output:
[
  [3],
  [1],
  [2],
  [1,2,3],
  [1,3],
  [2,3],
  [1,2],
  []
]

'''

import sys, optparse, os

class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        if not nums:
            return []

        res = [[]]
        for num in nums:
            res = res + [[num] + ele for ele in res]

        return res



nums = [1,2,3]

solution = Solution()
result = solution.subsets(nums)
print result

'''
Complexity Analysis
Time complexity : O(n^2).
    We are doing one pass through the nums,
    and for each number in nums we are doing one pass through the result.

Space complexity : O(n).
    Extra space is used to store result subsets.
'''
