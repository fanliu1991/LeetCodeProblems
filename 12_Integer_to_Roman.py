'''
Given an integer, convert it to a roman numeral.
I(1), V(5), X(10), L(50), C(100), D(500) and M(1000)
Input is guaranteed to be within the range from 1 to 3999.

'''
import sys, optparse, os

class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """

        # M = ["", "M", "MM", "MMM"]
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        # roman_numeral = M[num/1000] + C[(num%1000)/100] + X[(num%100)/10] + I[num%10]
        # return roman_numeral

        strs = ['M', 'CM', 'D', 'CD', 'C', 'XC', 'L', 'XL', 'X', 'IX', 'V', 'IV', 'I']
        nums = [1000, 900, 500, 400, 100, 90, 50, 40, 10, 9, 5, 4, 1]
        roman_numeral = ""
        for i, j in enumerate(nums):
            while num >= j:
                roman_numeral += strs[i]
                num -= j
            if num == 0:
                return roman_numeral


number = 3998
# MMMCMXCVIII
solution = Solution()
roman = solution.intToRoman(number)
print roman
