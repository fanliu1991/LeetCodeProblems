'''
Given an array with n objects colored red, white or blue,
sort them in-place so that objects of the same color are adjacent,
with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2
to represent the color red, white, and blue respectively.

Note:

You are not suppose to use the library's sort function for this problem.

A rather straight forward solution is a two-pass algorithm using counting sort.
    First, iterate the array counting number of 0's, 1's, and 2's,
    then overwrite array with total number of 0's, then 1's and followed by 2's.

Could you come up with a one-pass algorithm using only constant space?

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]

'''

import sys, optparse, os

class Solution(object):
    def sortColors(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """

        '''
        Initially, we set the frist 1 and first 2 at position 0,

        For every number in the nums, we set it as 2,
        if it is 2, then we done,
        else if it is 0 or 1, then we set the value at first 2 position as 1 and mover forward the first 2 position,
        if it is 1, then we done,
        else if it is 0, then we set the value at first 1 position as 0 and mover forward the first 1 position.

        hence, [0, first_one), [first_one, first_two), [first_two, k) are 0s, 1s and 2s sorted in place for [0,k).
        '''

        first_one, first_two = 0, 0

        for i in range(len(nums)):
            value = nums[i]
            nums[i] = 2

            if value < 2:
                nums[first_two] = 1
                first_two += 1
            if value == 0:
                nums[first_one] = 0
                first_one += 1


nums = [2,0,2,1,1,0]

solution = Solution()
result = solution.sortColors(nums)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the nums.

Space complexity : O(1).
    Nums are sorted in place and no extra space is used. Only extra variables are needed.

'''

