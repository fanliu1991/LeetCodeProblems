'''
Given a roman numeral, convert it to an integer.
I(1), V(5), X(10), L(50), C(100), D(500) and M(1000)
Input is guaranteed to be within the range from 1 to 3999.

'''
import sys, optparse, os

class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """

        # M = ["", "M", "MM", "MMM"]
        # C = ["", "C", "CC", "CCC", "CD", "D", "DC", "DCC", "DCCC", "CM"]
        # X = ["", "X", "XX", "XXX", "XL", "L", "LX", "LXX", "LXXX", "XC"]
        # I = ["", "I", "II", "III", "IV", "V", "VI", "VII", "VIII", "IX"]

        roman = {'I':1, 'V':5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000}
        res = 0
        for i in range(len(s)):
            curr, nxt = s[i], s[i+1:i+2]
            if nxt and roman[curr] < roman[nxt]:
                res -= roman[curr]
            else:
                res += roman[curr]
        return res


roman ="MCDLIX"
#  1459
solution = Solution()
integer = solution.romanToInt(roman)
print integer
