'''
Implement pow(x, n), which calculates x raised to the power n(x^n).

Note:
-100.0 < x < 100.0
n is a 32-bit signed integer, within the range [-2^31, 2^31 - 1]



Example 1:

Input: 2.00000, 10
Output: 1024.00000

Example 2:

Input: 2.10000, 3
Output: 9.26100

Example 3:

Input: 2.00000, -2
Output: 0.25000
Explanation: 2^(-2) = 1/(2^2) = 1/4 = 0.25

'''

import sys, optparse, os

class Solution(object):
    def myPow(self, x, n):
        """
        :type x: float
        :type n: int
        :rtype: float
        """

        if n == 0:
            return 1

        if x == 0:
            return 0

        if n < 0:
            x = 1.0 / x
            n = -1 * n

        if n%2 == 0:
            return self.myPow(x*x, n/2)
        else:
            return x * self.myPow(x*x, n/2)


x = 2.0000
n = -5

solution = Solution()
result = solution.myPow(x,n)
print result


'''
Complexity Analysis
Time complexity : O(n). 
    Recursive algorithm by double x.

Space complexity : O(n).
    The total information content stored for double x and half n.
'''
