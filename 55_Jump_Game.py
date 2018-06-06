'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.

Each element in the array represents your maximum jump length at that position.

Determine if you are able to reach the last index.

Example 1:

Input: [2,3,1,1,4]
Output: true
Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.

Example 2:

Input: [3,2,1,0,4]
Output: false
Explanation: You will always arrive at index 3 no matter what. 
             Its maximum jump length is 0, which makes it impossible to reach the last index.

'''

import sys, optparse, os

class Solution(object):
    def canJump(self, nums):
        """
        :type nums: List[int]
        :rtype: bool
        """

        '''
        The element in the array represents maximum jump length at that position,
        it is possible to jump less length than that number.

        We find the furthest position, furthest_jump, that each element can reach in the list,
        if the furthest jump is located at a position with jump length == 0,
        then it is impossible to move forward and reach the last index,
        if the furthest jump is further than the last index,
        then the last index is reached

        '''

        if not nums:
            return False
        if len(nums) == 1:
            return True
        
        furthest_jump = 0
        
        for i in range(len(nums) - 1):
            furthest_jump = max(furthest_jump, i + nums[i])
            if i == furthest_jump and nums[i] == 0:
                return False
            if furthest_jump >= len(nums) - 1:
                return True


nums = [9, 4, 2, 1, 0, 2, 0]

solution = Solution()
result = solution.canJump(nums)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing a single pass through the nums array, hence n steps,
    where n is the length of array nums.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''

