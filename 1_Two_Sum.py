'''
Given an array of integers, return indices of the two numbers such that they add up to a specific target.
You may assume that each input would have exactly one solution, and you may not use the same element twice.

Example:

Given nums = [2, 7, 11, 15], target = 9,

Because nums[0] + nums[1] = 2 + 7 = 9,
return [0, 1].

'''
import sys, optparse, os

class Solution:
    def twoSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[int]
        """

        '''
        One-pass Hash Table:
            While we iterate and inserting elements into the table, we also look back to check if current element's complement already exists in the table. 
        If it exists, we have found a solution and return immediately.

        '''

        diff_dict = {}
        # for i in xrange(len(nums)):
            # if nums[i]  in diff_dict:
            #     return [diff_dict[nums[i]], i]
            # else:
            #     difference = target - nums[i]
            #     diff_dict[difference] = i

        for i, num in enumerate(nums):
            if num in diff_dict:
                return [diff_dict[num], i]
            else:
                diff_dict[target - num] = i


nums = [2, 7, 11, 15, 19]
target = 22

solution = Solution()
indices = solution.twoSum(nums, target)
print indices

'''
Complexity Analysis
Time complexity : O(n).
    We traverse the list containing nnn elements only once. Each look up in the table costs only O(1) time.

Space complexity : O(n).
    The extra space required depends on the number of items stored in the hash table, which stores at most nnn elements.
'''