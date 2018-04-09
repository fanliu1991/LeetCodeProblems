'''
Given an array S of n integers, are there elements a, b, c and d in S such that a + b + c + d = target?
Find all unique quadruplets in the array which gives the sum of target.

Note: The solution set must not contain duplicate quadruplets.

Example:

Given array S = [1, 0, -1, 0, -2, 2], and target = 0.

A solution set is:
[
  [-1,  0, 0, 1],
  [-2, -1, 1, 2],
  [-2,  0, 0, 2]
]

'''
import sys, optparse, os

class Solution(object):
    def fourSum(self, nums, target):
        """
        :type nums: List[int]
        :type target: int
        :rtype: List[List[int]]
        """


        results = []
        nums.sort()

        def findNum(nums, target, N, result, results):
            if len(nums) < N or N < 2 or target < nums[0]*N or target > nums[-1]*N:
                return

            if N == 2: # solve 2-sum base case
                left, right = 0, len(nums) - 1
                while left < right:
                    two_sum = nums[left] + nums[right]
                    if two_sum < target:
                        left += 1
                    elif two_sum > target:
                        right -= 1
                    else:
                        results.append(result + [nums[left], nums[right]])
                        left += 1
                        right -= 1
                        if nums[left] == nums[left-1]:
                            left += 1
                        if nums[right] == nums[right+1]:
                            right -=1
            else:
                for i in xrange(len(nums) - N + 1):  # recursively reduce N
                    if i == 0 or (i > 0 and nums[i] != nums[i-1]):
                        findNum(nums[i+1:], target-nums[i], N-1, result+[nums[i]], results)

        findNum(nums, target, 4, [], results)
        return results



s = [1, 0, -1, 0, -2, 2]
target = 0

solution = Solution()
result = solution.fourSum(s, target)
print result

'''
Complexity Analysis
Time complexity : O(n^3).

'''