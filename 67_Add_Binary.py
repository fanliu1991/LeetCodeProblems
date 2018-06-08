'''
Given two binary strings, return their sum (also a binary string).

The input strings are both non-empty and contains only characters 1 or 0.

Example 1:

Input: a = "11", b = "1"
Output: "100"

Example 2:

Input: a = "1010", b = "1011"
Output: "10101"

'''

import sys, optparse, os

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """

        a_index, b_index = len(a)-1, len(b)-1
        carry = 0
        sum_str = ""

        while a_index >= 0 or b_index >= 0:
            digit_sum = carry
            if a_index >= 0:
                digit_sum += int(a[a_index])
                a_index -= 1
            if b_index >= 0:
                digit_sum += int(b[b_index])
                b_index -= 1
            carry, remainder = divmod(digit_sum , 2)
            sum_str = str(remainder) + sum_str

        if carry:
            sum_str = str(carry) + sum_str

        return sum_str



a = "10101"
b =  "1011"

solution = Solution()
result = solution.addBinary(a, b)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one passes through the two binary strings.

Space complexity : O(n).
    At most n+1 extra space used to store result.
'''

