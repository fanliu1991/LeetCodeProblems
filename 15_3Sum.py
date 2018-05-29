'''
Given an array S of n integers, are there elements a, b, c in S such that a + b + c = 0?
Find all unique triplets in the array which gives the sum of zero.

Note: The solution set must not contain duplicate triplets.

Example:

Given array S = [-1, 0, 1, 2, -1, -4],

A solution set is:
[
  [-1, 0, 1],
  [-1, -1, 2]
]

'''
import sys, optparse, os

class Solution(object):
    def threeSum(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        '''
        Algorithm:
            To find the combinations of 3 numbers, we iterate through the list with the first pointer, and then trying to find two extra numbers to sum to 0.
            Since the list is ordered after sorting, the right pointer will always be higher than the left pointer. 
            So if the sum is too large, we can move the right pointer back one. On the other hand, if the sum is too small (below 0), then move the left pointer up one.

        '''


        res = []
        nums.sort()
        for i in xrange(len(nums) - 2):
            if i > 0 and nums[i] == nums[i-1]:
                continue # The continue statement rejects all the remaining statements in the current iteration of the loop and moves the control back to the top of the loop.
            left, right = i+1, len(nums) - 1
            while left < right:
                three_sum = nums[i] + nums[left] + nums[right]
                if three_sum < 0:
                    left += 1
                elif three_sum > 0:
                    right -= 1
                else:
                    res.append([nums[i], nums[left], nums[right]])
                    # find the last repeated left number and the first repeated right number
                    while left < right and nums[left] == nums[left+1]:
                        left += 1
                    while left < right and nums[right] == nums[right-1]:
                        right -=1
                    left += 1
                    right -= 1

        return res



s = [-1, 0, 1, 2, -1, -4]

solution = Solution()
result = solution.threeSum(s)
print result

'''
Complexity Analysis
Time complexity : O(n^2).

'''
