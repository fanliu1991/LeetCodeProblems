'''
Given an array of non-negative integers, you are initially positioned at the first index of the array.
Each element in the array represents your maximum jump length at that position.
Your goal is to reach the last index in the minimum number of jumps.

Note:
You can assume that you can always reach the last index.

Example:

Input: [2,3,1,1,4]
Output: 2
Explanation: The minimum number of jumps to reach the last index is 2.
             Jump 1 step from index 0 to 1, then 3 steps to the last index.

'''

import sys, optparse, os

class Solution(object):
    def jump(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        The element in the array represents maximum jump length at that position,
        it is possible to jump less length than that number.

        From current position i, we find the furthest position we can reach in current jump,
        current_jump_furthest

        Among the positions in the range from current position to furthest position,
        we want to find a position A that able to reach furthest in next jump, i.e. i + nums[i].

        When we reach the end of current jump range, we have to jump, so jumps_count ++.
        The jump starts from A, and the furthest position that A can reach become current_jump_furthest

        Repeat this until the second last element in the nums.
        '''

        jumps_count = 0
        next_jump_furthest = 0
        current_jump_furthest = 0
               
        for i in range(len(nums) - 1):
            next_jump_furthest = max(next_jump_furthest, i + nums[i])
            if i == current_jump_furthest:
                jumps_count += 1 
                current_jump_furthest = next_jump_furthest
            # print i, jumps_count, current_jump_furthest, next_jump_furthest
        return jumps_count


nums = [2,4,1,1,4]
# inde=[0,1,2,3,4,5,6,7,8,9,10,11,12]
# nums=[5,8,1,1,2,2,1,1,1,1, 0, 0, 0]

solution = Solution()
result = solution.jump(nums)
print result


'''
Complexity Analysis
Time complexity : O(n).
    One iteration of nums array is needed.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''
