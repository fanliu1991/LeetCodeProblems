'''
Given a sorted array and a target value, return the index if the target is found. If not, return the index where it would be if it were inserted in order.

You may assume no duplicates in the array.

Example 1:

Input: 1,3,5,6], 5
Output: 2

Example 2:

Input: [1,3,5,6], 2
Output: 1

Example 3:

Input: [1,3,5,6], 7
Output: 4

Example 4:

Input: [1,3,5,6], 0
Output: 0


'''

import sys, optparse, os

class Solution(object):
    def searchInsert(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        left, right = 0, len(nums)

        while left < right:
            mid = (left + right) / 2
            print(left, right, mid)
            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else: # nums[mid] > target
                right = mid

        return left


nums = [1,3]
target = 2

solution = Solution()
result = solution.searchInsert(nums, target)
print result

'''
Complexity Analysis
Time complexity : O(logn).
    Binary search solution.

Space complexity : O(1).
    No extra space is used. Only two extra variables left and right are needed.
'''