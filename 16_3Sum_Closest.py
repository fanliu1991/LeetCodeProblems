'''
Given an array S of n integers, find three integers in S such that the sum is closest to a given number, target.
Return the sum of the three integers. 

You may assume that each input would have exactly one solution.

Example:

Given array S = [-1, 2, 1, -4], and target = 1.

The sum that is closest to the target is 2. (-1 + 2 + 1 = 2).

'''
import sys, optparse, os

class Solution(object):
    def threeSumClosest(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: int
        """

        '''
        Algorithm:
            To find the combinations of 3 numbers, we iterate through the list with the first pointer, and then trying to find two extra numbers to get their sum.
            Since the list is ordered after sorting, the right pointer will always be higher than the left pointer. 
            So if the sum is too large (target < sum), we can move the right pointer back one. On the other hand, if the sum is too small (target > current_sum), then move the left pointer up one.

        '''


        nums.sort()
        sum_result = nums[0] + nums[1] + nums[2]
        min_diff = abs(target - sum_result)
        for i in xrange(len(nums) - 2):
            left = i+1
            right = len(nums)-1
            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum
                elif abs(target - current_sum) < abs(target - sum_result):
                    sum_result = current_sum

                if target < current_sum:
                    right -= 1
                else:
                    left += 1

        return sum_result



s = [-1, 2, 1, -4]
target = 1

# s = [1, 3, 4, 7, 9, 10, 12]
# target = 20

solution = Solution()
result = solution.threeSumClosest(s, target)
print result

'''
Complexity Analysis
Time complexity : O(n^2).

'''