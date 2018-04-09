'''
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases.

The function first discards as many whitespace characters as necessary until the first non-whitespace character is found.
Then, starting from this character, takes an optional initial plus or minus sign followed by as many numerical digits as possible, and interprets them as a numerical value.

The string can contain additional characters after those that form the integral number, which are ignored and have no effect on the behavior of this function.

If the first sequence of non-whitespace characters in str is not a valid integral number, or if no such sequence exists because either str is empty or it contains only whitespace characters, no conversion is performed.

If no valid conversion could be performed, a zero value is returned.
If the correct value is out of the range of representable values, INT_MAX (2147483647) or INT_MIN (-2147483648) is returned. 

'''
import sys, optparse, os

class Solution(object):
    def myAtoi(self, s):
        """
        :type str: str
        :rtype: int
        """

        i, num_value = 0, 0
        sign = 1

        if len(s) == 0:
            return 0

        while s[i] == " " and i < len(s):
            i += 1

        if s[i] == "+":
            i += 1
        elif s[i] == "-":
            sign = -1
            i += 1
        else:
            return 0

        while i < len(s):
            try:
                digit = int(s[i])
            except ValueError:
                print "String contains an invalid integral number."
                break

            num_value = 10 * num_value + digit
            if num_value > 2147483647 and sign == 1:
                return "INT_MAX"
            elif num_value > 2147483648 and sign == -1:
                return INT_MIN

            i += 1

        return sign * num_value



nums = "   -4678248"

solution = Solution()
integer = solution.myAtoi(nums)
print integer
