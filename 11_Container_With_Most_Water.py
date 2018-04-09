'''
Given n non-negative integers a1, a2, ..., an, where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

You may not slant the container and n is at least 2.

'''
import sys, optparse, os

class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """

        '''
        Two Pointer Approach:
            The intuition behind this approach is that the area formed between the lines will always be limited by the height of the shorter line.
        Further, the farther the lines, the more will be the area obtained.

            We take two pointers, one at the beginning and one at the end of the array constituting the length of the lines.
        Futher, we maintain a variable maxareamaxareamaxarea to store the maximum area obtained till now.
        At every step, we find out the area formed between them, update maxarea and move the pointer pointing to the shorter line towards the other end by one step.

        To maximize the area, we need to consider the area between the lines of larger lengths.
        If we try to move the pointer at the longer line inwards, we won't gain any increase in area, since it is limited by the shorter line.
        But moving the shorter line's pointer could turn out to be beneficial, as per the same argument, despite the reduction in the width.
        This is done since a relatively longer line obtained by moving the shorter line's pointer might overcome the reduction in area caused by the width reduction.
        '''

        current_area, max_area = 0, 0
        left_line = 0
        right_line = len(height) - 1

        while left_line < right_line:
            current_area = min(height(left_line), height(right_line)) * (right_line - left_line)
            max_area = max(max_area, current_area)
            if height(left_line) < height(height[right_line]):
                left_line += 1
            else:
                right_line += 1

        return max_area


nums = [2, 7, 11, 15, 19]

solution = Solution()
indices = solution.maxArea(nums)
print indices

'''
Complexity Analysis
Time complexity : O(n).
    Single pass.

Space complexity : O(1).
    Constant space is used.
'''
