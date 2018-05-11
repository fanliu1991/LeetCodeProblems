'''
Given a collection of numbers that might contain duplicates, return all possible unique permutations.

Example:

Input: [1,1,2]
Output: 
[
    [1,1,2],
    [1,2,1],
    [2,1,1]
]

'''

import sys, optparse, os

class Solution(object):
    def permuteUnique(self, nums):
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
            used_numbers = []
            for i in range(len(nums)):
                if nums[i] not in used_numbers:
                    used_numbers.append(nums[i])
                    self.dfs(nums[:i] + nums[i+1:], start_num + [nums[i]])


nums = [1,1,2,2]

solution = Solution()
result = solution.permuteUnique(nums)
print result


'''
Complexity Analysis
Time complexity : O(|V|+|E|).
    Depth first search.

Space complexity : O(|V|+|E|).
'''
