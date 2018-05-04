'''
Suppose an array sorted in ascending order is rotated at some pivot unknown to you beforehand.
(i.e., [0,1,2,4,5,6,7] might become [4,5,6,7,0,1,2]).

You are given a target value to search. If found in the array return its index, otherwise return -1.
You may assume no duplicate exists in the array.

Example 1:

Input:
    nums = [4,5,6,7,0,1,2], target = 0
Output: 
    4

Example 2:

Input:
    nums = [4,5,6,7,0,1,2], target = 3
Output:
    -1

'''

import sys, optparse, os

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        if not nums:
            return -1

        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return mid

            if nums[left] <= nums[mid]: # nums[left : mid] is sorted, pivot in the nums[mid+1 : right]
                if nums[left] <= target and target < nums[mid]:
                    right = mid - 1
                else:
                    left = mid + 1
            else: # pivot in the nums[left : mid-1], nums[mid : right] is sorted
                if nums[mid] < target and target <= nums[right]:
                    left = mid + 1
                else:
                    right = mid - 1

        if nums[left] == target: # now left == right, nums[left] is same as nums[right]
            return left
        else:
            return -1

nums = [4,5,6,7,0,1,2]
target = 3

solution = Solution()
result = solution.search(nums, target)
print result

'''
Complexity Analysis
Time complexity : O(logn).
    Binary search solution.

Space complexity : O(1).
    No extra space is used. Only two extra variables left and right are needed.
'''