'''
Given a string s, find the longest palindromic substring in s. You may assume that the maximum length of s is 1000.

Example 1:

Input: "babad"
Output: "bab"
Note: "aba" is also a valid answer.

Example 2:

Input: "cbbd"
Output: "bb"

'''
import sys, optparse, os

class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: str
        """

        """
        Expand Around Center:
            We observe that a palindrome mirrors around its center.
            Therefore, a palindrome can be expanded from its center, and there are only 2*n - 1 such centers.
            (n 1-letter centers, n-1 2-letters centers)

            Using Dynamic Programming, define P(i, j) as following:

            P(i, j) = true,    if the substring S_i .... S_j is a palindrome.
                      false,    otherwise.

            Therefore, P(i, j) = P(i+1, j-1) and S_i == S_j
            The base cases are:
                    1-letter center: P(i,i) = true
                    2-letter center: P(i,i+1) = true if S_i == S_i+1

            This yields a straight forward DP solution, which we first initialize the one and two letters palindromes, and work our way up finding all three letters palindromes, and so on...

        """

        palindromic_string = ""

        for i in xrange(len(s)):
            one_letter_center = self.expandAroundCenter(s, i, i)
            two_letters_center = self.expandAroundCenter(s, i, i+1)
            palindromic_string = max(palindromic_string, one_letter_center, two_letters_center, key=len)

        return palindromic_string

    def expandAroundCenter(self, s, left, right):
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return s[left + 1:right]



s = "babad"

solution = Solution()
result = solution.longestPalindrome(s)
print result

"""
Complexity Analysis
Time complexity : O(n^2).
    Since expanding a palindrome around its center could take O(n) time, the overall complexity is O(n^2).

Space complexity : O(1).
"""
