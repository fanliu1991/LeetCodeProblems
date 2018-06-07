'''
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:

Input: "Hello World"
Output: 5

'''

import sys, optparse, os

class Solution(object):
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        if not s:
            return 0

        s_list = s.rstrip(" ").split(" ")
        return len(s_list[-1])


s = "a "

solution = Solution()
result = solution.lengthOfLastWord(s)
print result


'''
Complexity Analysis
Time complexity : O(n). 

Space complexity : O(1).
'''
