'''
Given two integers dividend and divisor, divide two integers without using multiplication, division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.

Example 1:

Input: dividend = 10, divisor = 3
Output: 3

Example 2:

Input: dividend = 7, divisor = -3
Output: -2

Note:

Both dividend and divisor will be 32-bit signed integers.
The divisor will never be 0.
Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [-2^31,  2^31 - 1]. For the purpose of this problem, assume that your function returns 2^31 - 1 when the division result overflows.
'''

import sys, optparse, os

class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """

        positive = (dividend < 0) is (divisor < 0)

        dividend, divisor = abs(dividend), abs(divisor)
        res = 0

        while dividend >= divisor:
            if dividend == divisor:
                res += 1
                break

            temp = divisor
            i = 1
            print("outer loop", temp, i)

            while dividend > temp:
                dividend -= temp
                res += i
                temp = temp << 1
                i = i << 1
                # a << b, move a bitwise to the left by b units.
                # For example, a = 3, in binary 11. Then a << 1 in binary is 110, which is 6 in decimal
                print("inner loop", res, temp, i)

        if not positive:
            res = -res

        return min(max(-2147483648, res), 2147483647)


dividend = 1
divisor = 1


solution = Solution()
result = solution.divide(dividend, divisor)
print result

'''
Complexity Analysis
Time complexity : O(n)

Space complexity : O(1).
'''