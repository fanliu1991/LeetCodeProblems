'''
Given an integer array nums,
find the contiguous subarray (containing at least one number)
which has the largest sum and return its sum.

Example:

Input: [-2,1,-3,4,-1,2,1,-5,4],
Output: 6
Explanation: [4,-1,2,1] has the largest sum = 6.

'''

import sys, optparse, os

class Solution(object):
    def maxSubArray(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        """
        Greedy algorithm
            There are 4 possible conditions for current_sum + num:
            1. positive + positive
            2. positive + negative
            3. negative + positive
            4. negative + negative

            In conditions 1, current_sum + num generate better result at num position.
            In conditions 2, current_sum + num generate worse result at num position,
        but it is possible to generate better result if we extend current_sum + sum later.
            In conditions 3 and 4, current_sum + num generate worse result at num position, 
        so we discard current_sum, and reset it to num.

        """

        if not nums:
            return 0
        elif len(nums) == 1:
            return nums[0]

        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(num, current_sum + num)
            max_sum = max(max_sum, current_sum)

        return max_sum


nums = [-2,1,-3,4,-1,2,1,-5,4]

solution = Solution()
result = solution.maxSubArray(nums)
print result


'''
Complexity Analysis
Time complexity : O(n). 

Space complexity : O(1).
'''
