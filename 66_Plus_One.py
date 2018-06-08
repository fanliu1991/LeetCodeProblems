'''
Given a non-empty array of digits representing a non-negative integer, 
plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list,
and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

'''

import sys, optparse, os

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """

        digit_index = len(digits) - 1
        carry = 1 # This is the "1" that to be plused to the integer

        while digit_index >= 0:
            carry, remainder = divmod(digits[digit_index] + carry, 10)
            digits[digit_index] = remainder
            if carry == 0:
                break
            else:
                digit_index -= 1

        if carry:
            digits.insert(0, carry)

        return digits


digits = [9,9,9]

solution = Solution()
result = solution.plusOne(digits)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one passes through the numbers array.

Space complexity : O(1).
    In place calculation, no extra space used.
'''

