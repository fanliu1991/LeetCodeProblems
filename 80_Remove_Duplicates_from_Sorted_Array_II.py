'''
Given a sorted array nums, remove the duplicates in-place
such that duplicates appeared at most twice and return the new length.

Do not allocate extra space for another array,
you must do this by modifying the input array in-place
with O(1) extra memory.

It doesn't matter what values are set beyond the returned length.

Example 1:

Given nums = [1,1,1,2,2,3],

Your function should return length = 5, 
with the first five elements of nums being 1, 1, 2, 2 and 3 respectively.


Example 2:

Given nums = [0,0,1,1,1,1,2,3,3],

Your function should return length = 7, 
with the first seven elements of nums being modified to 0, 0, 1, 1, 2, 3 and 3 respectively.


'''

import sys, optparse, os

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 0

        replace_pos = 0

        for number in nums:
            if replace_pos < 2 or number > nums[replace_pos - 2]:
                nums[replace_pos] = number
                replace_pos += 1

        return replace_pos


nums = [0,0,1,1,1,1,2,3,3]

solution = Solution()
result = solution.removeDuplicates(nums)
print result

'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the nums

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
