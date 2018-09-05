'''
Given a string s1, we may represent it as a binary tree
by partitioning it to two non-empty substrings recursively.

Below is one possible representation of s1 = "great":

    great
   /    \
  gr    eat
 / \    /  \
g   r  e   at
           / \
          a   t

To scramble the string, we may choose any non-leaf node and swap its two children.

For example, if we choose the node "gr" and swap its two children,
it produces a scrambled string "rgeat".

    rgeat
   /    \
  rg    eat
 / \    /  \
r   g  e   at
           / \
          a   t
We say that "rgeat" is a scrambled string of "great".

Similarly, if we continue to swap the children of nodes "eat" and "at",
it produces a scrambled string "rgtae".

    rgtae
   /    \
  rg    tae
 / \    /  \
r   g  ta  e
       / \
      t   a
We say that "rgtae" is a scrambled string of "great".

Given two strings s1 and s2 of the same length, determine if s2 is a scrambled string of s1.


Example 1:
Input: s1 = "great", s2 = "rgeat"
Output: true

Example 2:
Input: s1 = "abcde", s2 = "caebd"
Output: false

'''

import sys, optparse, os

class Solution:
    def isScramble(self, s1, s2):
        """
        :type s1: str
        :type s2: str
        :rtype: bool
        """

        """
        Dynamic programming
        """

        m = len(s1)
        n = len(s2)

        if s1 == s2:
            return True

        if m != n or sorted(s1) != sorted(s2):
            return False

        if m <= 2:
            return True

        for i in range(1, m):
            if self.isScramble(s1[:i], s2[:i]) == True and self.isScramble(s1[i:], s2[i:]) == True:
                return True

            if self.isScramble(s1[:i], s2[-i:]) == True and self.isScramble(s1[i:], s2[:-i]) == True:
                return True

        return False



s1 = "great"
s2 = "rgtae"

solution = Solution()
result = solution.isScramble(s1, s2)
print result


'''
Complexity Analysis
Time complexity : O(n^2).

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''

