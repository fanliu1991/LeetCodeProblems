'''
Given an unsorted integer array, find the smallest missing positive integer.

Note:
Your algorithm should run in O(n) time and uses constant extra space.

Example 1:

Input: [1,2,0]
Output: 3

Example 2:

Input: [3,4,-1,1]
Output: 2

Example 3:

Input: [7,8,9,11,12]
Output: 1

'''

import sys, optparse, os

class Solution(object):
    def firstMissingPositive(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        if not nums:
            return 1

        i, n = 0, len(nums)

        while i < n:
            # If the current value is in the range of (0,length) and it's not at its correct position, 
            # swap it to its correct position.
            if nums[i] >= 0 and nums[i] < n and nums[nums[i]] != nums[i]:
                position_i_value = nums[i]
                position_num_i_value = nums[nums[i]]
                nums[i] = position_num_i_value
                nums[position_i_value] = position_i_value
            else: # else continue to next value
                i += 1

        index = 1

        # Check from index=1 to see whether each index and value can be corresponding.
        while index < n and nums[index] == index:
            index += 1

        # If it breaks before reaching the end. then index must be the first missing number.
        # The positions of nums list is 0, ..., n-1
        if index < n:
            return index
        else: # Now index = n, and positions 1, ..., n-1 have values 1, ..., n-1
            if nums[0] == index:
                return index+1
            else:
                return index


nums = [1,2,0]

solution = Solution()
result = solution.firstMissingPositive(nums)
print result


'''
Complexity Analysis
Time complexity : O(n).

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''
