'''
Given an array of integers nums sorted in ascending order, find the starting and ending position of a given target value.

If the target is not found in the array, return [-1, -1].

Example 1:

Input:
    nums = [5,7,7,8,8,10], target = 8
Output: 
    [3, 4]

Example 2:

Input:
    nums = [5,7,7,8,8,10], target = 6
Output:
    [-1, -1]

'''

import sys, optparse, os

class Solution(object):
    def searchRange(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        """
        # standart solution
        def left_search(nums, target):
            low = 0
            high = len(nums)

            while low < high:
                mid = (low+high) / 2
                if nums[mid] >= target:
                    high = mid
                else: # nums[mid] < target
                    low = mid+1
            return low

        def right_search(nums, target):
            low = 0
            high = len(nums)

            while low < high:
                mid = (low+high) / 2
                if nums[mid] > target:
                    high = mid
                else: # nums[mid] <= target
                    low = mid+1
            return low


        if not nums:
            return [-1, -1]

        left = left_search(nums, target)
        right = right_search(nums, target)
        print(left, right)

        if left == len(nums) or nums[left] != target:
            return [-1, -1]

        return [left, right-1]



        """
        # my solution
        def left_search(nums, target): # find the index of first number that equals to target
            left, right = 0, len(nums)-1
            if nums[left] == target:
                return left

            while left < right:
                mid = (left + right) / 2
                if nums[mid] == target: # nums[mid] can not be larger than target
                    right = mid
                else: # nums[mid] < target
                    left = mid+1

            if nums[left] == target:
                return left
            else:
                return -1

        def right_search(nums, target): # find the index of first number that is larger than target
            left, right = 0, len(nums)-1
            if nums[right] == target:
                return right

            while left < right:
                mid = (left + right) / 2
                print("right_search", left, right, mid)
                if nums[mid] == target: # nums[mid] can not be smaller than target
                    left = mid+1
                else: # nums[mid] > target
                    right = mid

            if nums[right-1] == target:
                return right-1
            else:
                return -1


        if not nums:
            return [-1, -1]

        left, right = 0, len(nums)-1
        if nums[left] == target and nums[right] == target:
            return [left, right]

        while left < right:
            mid = (left + right) / 2
            print(left, right, mid)

            if nums[mid] > target: # target range is at left half
                right = mid-1
            elif nums[mid] < target: # target range is at right half
                left = mid+1
            else: # nums[mid] == target
                if mid == 0:
                    left = 0
                    right = right_search(nums[mid+1:], target) + 1 if right_search(nums[mid+1:], target) != -1 else left
                    return [left, right]
                else:
                    left = left_search(nums[left:mid], target) + left if left_search(nums[:mid], target) != -1 else mid
                    right = right_search(nums[mid:right+1], target) + mid if right_search(nums[mid+1:], target) != -1 else mid
                    return [left, right]

        if nums[left] == target: # left and right are the index of the number equals to target
            return [left, right]
        else: # left and right are the index of the max number that is smaller than target
            return [-1, -1]

        


nums = [2,2,9]
target = 4

solution = Solution()
result = solution.searchRange(nums, target)
print result

'''
Complexity Analysis
Time complexity : O(logn).
    Binary search solution.

Space complexity : O(1).
    No extra space is used. Only two extra variables left and right are needed.
'''