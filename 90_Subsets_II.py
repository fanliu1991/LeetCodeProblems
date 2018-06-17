'''
Given a collection of integers that might contain duplicates, nums,
return all possible subsets (the power set).

Note:
The solution set must not contain duplicate subsets.
This is a modified question of 78_Subsets

Example:

Input: [1,2,2]

Output:
[
  [2],
  [1],
  [1,2,2],
  [2,2],
  [1,2],
  []
]

'''

import sys, optparse, os

class Solution(object):
    def subsetsWithDup(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        """
        if nums[i] != nums[i-1],
        then adding nums[i] to each element of current result will not generate duplicates

        if nums[i] == nums[i-1],
        then adding nums[i] to the result of nums[:n-1] is equivalent to that of adding nums[i-1],
        so skip this part, but only adding nums[i] to the result of nums[:n-1] + nums[n-1]

        e.g. nums = [1,2,2]
        for nums = 1, result = [[], [1]],
        for nums = 1, 2, result = [[], [1], [2], [1,2]],

        but adding nums[2] = 2 to [[], [1]] is equivalent to that of adding nums[1] = 2,
        so skip this part, but only adding nums[2] = 2 to [[2], [1,2]],
        result = [[], [1], [2], [1,2], [2,2], [1,2,2]]

        """

        nums.sort()
        result = [[]]

        for i in range(len(nums)):
            if i == 0 or nums[i] != nums[i-1]:
                no_duplicate_length = len(result)
                start_without_duplicate = 0
            else:
                start_without_duplicate = len(result) - no_duplicate_length

            for j in range(start_without_duplicate, len(result)):
                result.append(result[j] + [nums[i]])

        return result


nums = [4,4,4,1,4]

solution = Solution()
result = solution.subsetsWithDup(nums)
print result

'''
Complexity Analysis
Time complexity : O(2^n).
    We are doing one pass through the result list for each number in nums.

Space complexity : O(2^n).
    Extra space is used to store subsets in the result.

'''
