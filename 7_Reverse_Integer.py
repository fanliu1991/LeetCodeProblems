'''
Given a 32-bit signed integer, reverse digits of an integer.

Example 1:

Input: 123
Output:  321

Example 2:

Input: -123
Output: -321

Example 3:

Input: 120
Output: 21

'''
import sys, optparse, os

class Solution(object):
    def reverse(self, x):
        """
        :type x: int
        :rtype: int
        """

        # # method 1
        # signal = cmp(x, 0)
        # value = int(str(abs(x))[::-1])
        # '''
        # Sequence[start:end:step]
        #     step is positive or negative decsides direction of scanning
        #     if step is positive, scan from left to right,
        #     if step is negative, scan from right to left.
        # '''

        # n = signal * value

        # if n.bit_length() < 32:
        #     return n
        # else:
        #     return 0

        # method 2
        int_value = abs(x)
        int_length = len(str(int_value))
        n = 0
        while int_value:
            tail = len(str(int_value)) - 1
            divison, int_value = divmod(int_value, 10**tail)
            n += divison * (10 ** (int_length - tail - 1))

        return cmp(x, 0) * n * (n < 2**31)



# s = 1234560
s = 6000

solution = Solution()
result = solution.reverse(s)
print result

"""
Complexity Analysis

"""
