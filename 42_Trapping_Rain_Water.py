'''
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

'''

import sys, optparse, os

class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        total_trap = 0
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        
        '''
        if there is a larger bar at one end, the water trapped would be dependant on height of smaller bar
        
        as long as right_max[i]>left_max[i](from element 0 to 6),
        the water trapped depends upon the left_max,
        and similar is the case when left_max[i]>right_max[i](from element 8 to 11).
        
        So, if there is a larger bar at one end(say right),
        we are assured that the water trapped would be dependant on height of bar in current direction(from left to right).
        As soon as we find the bar at other end(right) is smaller,
        we start iterating in opposite direction(from right to left)
        
        trapped water is computed at each elevation
        '''

        while left < right:
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else: # height[left] < left_max
                    total_trap += left_max - height[left]
                left = left + 1
            else: # height[left] >= height[right]
                if height[right] >= right_max:
                    right_max = height[right]
                else: # height[right] < right_max
                    total_trap += right_max - height[right]
                right = right - 1
        
        return total_trap


height = [0,1,0,2,1,0,1,3,2,1,2,1]

solution = Solution()
result = solution.trap(height)
print result


'''
Complexity Analysis
Time complexity : O(n).
    Single iteration of O(n).

Space complexity : O(1).
    No extra space is used. Only constant space required for left, right, left_max and right_max.
'''
