'''
Suppose an array sorted in ascending order is rotated
at some pivot unknown to you beforehand.

(i.e., [0,0,1,2,2,5,6] might become [2,5,6,0,0,1,2]).

You are given a target value to search. 
If found in the array return true, otherwise return false.

This is a follow up problem to 33. Search in Rotated Sorted Array,
where nums may contain duplicates.


Example 1:

Input:
nums = [2,5,6,0,0,1,2], target = 0

Output: true

Example 2:

Input:
nums = [2,5,6,0,0,1,2], target = 3

Output: false

'''

import sys, optparse, os

class Solution(object):
    def search(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: bool
        """

        if not nums:
            return False

        left, right = 0, len(nums)-1

        while left < right:
            mid = (left + right) / 2
            if nums[mid] == target:
                return True

            # different part from Rotated Sorted Array without duplication
            while left < mid and nums[left] == nums[mid]:
                left += 1

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
            return True
        else:
            return False



nums = [1,3,1,1,1]
target = 3

solution = Solution()
result = solution.search(nums, target)
print result

'''
Complexity Analysis
Time complexity : O(logn).
    Binary Search solution.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
