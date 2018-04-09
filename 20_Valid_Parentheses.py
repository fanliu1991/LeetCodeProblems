'''
Given a string containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

The brackets must close in the correct order, "()" and "()[]{}" are all valid but "(]" and "([)]" are not.

'''
import sys, optparse, os

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """

        stack = []
        char_pair = {"(":")", "{":"}", "[":"]"}

        if len(s) % 2 != 0:
            return False
        else:
            for char in s:
                if char in char_pair:
                    stack.append(char)
                elif stack == []:
                    return False
                elif char_pair[stack.pop()] != char:
                    return False
            return not stack


s = ")[)]"

solution = Solution()
result = solution.isValid(s)
print result

'''
Complexity Analysis
Time complexity : O(n).

'''