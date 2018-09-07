'''
Given s1, s2, s3, find whether s3 is formed by the interleaving of s1 and s2.

Example 1:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbcbcac"
Output: true
Example 2:

Input: s1 = "aabcc", s2 = "dbbca", s3 = "aadbbbaccc"
Output: false

'''

import sys, optparse, os

class Solution:
    def isInterleave(self, s1, s2, s3):
        """
        :type s1: str
        :type s2: str
        :type s3: str
        :rtype: bool
        """

        s1_len = len(s1)
        s2_len = len(s2)
        s3_len = len(s3)
        
        if s1_len + s2_len != s3_len:
            return False

        if not s1 and not s2 and not s3:
            return True

        if not s1 and s3_len != 0:
            if s2 == s3:
                return True
            else:
                return False

        if not s2 and s3_len != 0:
            if s1 == s3:
                return True
            else:
                return False

        if s1[0] != s3[0] and s2[0] != s3[0]:
            return False

        # Dynamic Programming solution
        dp = [[True for _ in range(s2_len + 1)] for _ in range(s1_len + 1)]

        for i in range(1, s1_len + 1):
            dp[i][0] = dp[i-1][0] and s1[i-1] == s3[i-1]

        for j in range(1, s2_len + 1):
            dp[0][j] = dp[0][j-1] and s2[j-1] == s3[j-1]


        for i in range(1, s1_len + 1):
            for j in range(1, s2_len + 1):
                dp[i][j] = (dp[i-1][j] and s1[i-1] == s3[i+j-1]) or (dp[i][j-1] and s2[j-1] == s3[i+j-1])

        return dp[-1][-1]

        # Revursive solution
        # res1, res2 = False, False
        # i = 0
        # if s1[0] == s3[0]:
        #     res1 = self.isInterleave(s1[1:], s2, s3[1:])

        # j=0
        # if s2[0] == s3[0]:
        #     res2 = self.isInterleave(s1, s2[1:], s3[1:])

        # return res1 or res2


s1 = "aa"
s2 = "ab"
s3 = "aaba"

solution = Solution()
result = solution.isInterleave(s1, s2, s3)
print result


'''
Complexity Analysis
Time complexity : O(m*n).
    dp array of size m * n is filled.

Space complexity : O(m * n).
    2D dp of size (m+1) * (n+1) is required.
    m and n are the lengths of strings s1 and s2 respectively.
'''

