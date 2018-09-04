'''
Given n non-negative integers representing the histogram's bar height,
where the width of each bar is 1,
find the area of largest rectangle in the histogram.


Example 1:
Input: [2,1,5,6,2,3]
Output: 10
'''

import sys, optparse, os

class Solution:
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """

        """
        For any bar i,
        let l = left_boundary[i] be the last coordinate of the bar to the left which height h[l+1] >= h[i],
        and r = right_boundary[i] be the last coordinate of the bar to the right with height h[r-1] >= h[i].

        To effectively calculate left_boundary and right_boundary arrays,
        we can reuse results of previous calculations and "jump" through indices in quick manner.

        Then for any bar i, its rectangle is height[i] * ( r - l - 1 )

        """

        if not heights:
            return 0

        left_boundary = [0] * len(heights)
        right_boundary = [0] * len(heights)

        left_boundary[0]  = -1
        right_boundary[-1] = len(heights)

        for i in range(1, len(heights)):
            left = i - 1
            while(left > -1 and heights[left] >= heights[i]):
                left = left_boundary[left]
            left_boundary[i] = left

        for i in range(len(heights) - 2, -1, -1):
            right = i + 1
            while(right < len(heights) and heights[i] <= heights[right]):
                right = right_boundary[right]
            right_boundary[i] = right

        max_area = 0
        for i in range(len(heights)):
            max_area = max(max_area, heights[i] * (right_boundary[i] - left_boundary[i] - 1))

        return max_area


heights = [1, 2, 1, 2, 1, 2, 1, 2]

solution = Solution()
result = solution.largestRectangleArea(heights)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We do some simple linear scans of the height array.

Space complexity : O(n).
    Extra space is used to store left_boundary and right_boundary.
'''

