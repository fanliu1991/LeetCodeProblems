'''
Given a collection of distinct integers, return all possible permutations.

Example:

Input: [1,2,3]
Output: 
[
    [1,2,3],
    [1,3,2],
    [2,1,3],
    [2,3,1],
    [3,1,2],
    [3,2,1]
]

'''

import sys, optparse, os

class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        self.permutations = []

        if nums:
            self.dfs(nums, [])

        return self.permutations

    def dfs(self, nums, start_num):
        if len(nums) == 1:
            self.permutations.append(start_num + nums)
        else:
            for i in range(len(nums)):
                self.dfs(nums[:i] + nums[i+1:], start_num + [nums[i]])


nums = [1,2,3,4]

solution = Solution()
result = solution.permute(nums)
print result


'''
Complexity Analysis
Time complexity : O(|V|+|E|).
    Depth first search.

Space complexity : O(|V|+|E|).
'''
