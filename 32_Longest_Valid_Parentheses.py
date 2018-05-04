'''
Given a string containing just the characters '(' and ')',
find the length of the longest valid (well-formed) parentheses substring.

Example 1:

Input: "(()"
Output: 2
Explanation: The longest valid parentheses substring is "()"

Example 2:

Input: ")()())"
Output: 4
Explanation: The longest valid parentheses substring is "())"

'''

import sys, optparse, os

class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        we start traversing the string from the left towards the right,
        for every '(' encountered, we increment the leftleftleft counter,
        for every ')' encountered, we increment the rightrightright counter.

        Whenever left becomes equal to right, we calculate the length of the current valid string,
        and keep track of maximum length substring found so far.

        If right becomes greater than left, we reset left and right to 0.

        Next, we start traversing the string from right to left and similar procedure is applied.
        """

        longest_len = 0

        # from the left towards the right
        left, right = 0, 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right +=1

            if left == right:
                longest_len = max(longest_len, right * 2)
            if right > left:
                left, right = 0, 0

        # from the right towards the left
        left, right = 0, 0
        for i in range(len(s)-1, -1, -1):
            if s[i] == ")":
                right += 1
            else:
                left +=1

            if left == right:
                longest_len = max(longest_len, left * 2)
            if left > right:
                left, right = 0, 0

        return longest_len

s = "()((())"

solution = Solution()
result = solution.longestValidParentheses(s)
print result

'''
Complexity Analysis
Time complexity : O(n).
    Two traversals of the string.

Space complexity : O(1).
    No extra space is used. Only two extra variables left and right are needed.
'''