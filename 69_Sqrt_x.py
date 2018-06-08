'''
Implement int sqrt(int x).

Compute and return the square root of x,
where x is guaranteed to be a non-negative integer.

Since the return type is an integer,
the decimal digits are truncated
and only the integer part of the result is returned.

Example 1:

Input: 4
Output: 2

Example 2:

Input: 8
Output: 2
Explanation: The square root of 8 is 2.82842..., and since 
             the decimal part is truncated, 2 is returned.

'''

import sys, optparse, os

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        """

        if x == 0 or x == 1:
            return x
        else:
            left = 0
            right = x

            while left < right:
                median = (left + right) / 2
                if median ** 2 == x:
                    return median
                elif median ** 2 < x:
                    left = median + 1
                else:
                    right = median

            return left - 1


x = 99

solution = Solution()
result = solution.mySqrt(x)
print result

'''
Complexity Analysis
Time complexity : O(logn).
    Binary Search Solution.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''
