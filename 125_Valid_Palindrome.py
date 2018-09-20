'''
Given a string, determine if it is a palindrome, 
considering only alphanumeric characters and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.

Example 1:

Input: "A man, a plan, a canal: Panama"
Output: true

Example 2:

Input: "race a car"
Output: false
'''

import sys, optparse, os

class Solution:
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """

        if not s:
            return True

        s = s.lower()
        left = 0
        right = len(s) - 1

        while left < right:
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left] != s[right]:
                return False
            else:
                left += 1
                right -= 1

        return True


s = "A man, a plan, a canal: Panama"

solution = Solution()
result = solution.isPalindrome(s)
print result

'''
Complexity Analysis
Time complexity: O(n).
    We are doing a single pass through the string, hence n steps,
    where n is the length of price array.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''
