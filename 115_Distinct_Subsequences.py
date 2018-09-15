'''
Given a string S and a string T, 
count the number of distinct subsequences of S which equals T.

A subsequence of a string is a new string which is formed from the original string 
by deleting some (can be none) of the characters 
without disturbing the relative positions of the remaining characters.
(ie, "ACE" is a subsequence of "ABCDE" while "AEC" is not).

Example 1:

Input: S = "rabbbit", T = "rabbit"
Output: 3
Explanation:

As shown below, there are 3 ways you can generate "rabbit" from S.
(The caret symbol ^ means the chosen letters)

rabbbit
^^^^ ^^
rabbbit
^^ ^^^^
rabbbit
^^^ ^^^

Example 2:

Input: S = "babgbag", T = "bag"
Output: 5
Explanation:

As shown below, there are 5 ways you can generate "bag" from S.
(The caret symbol ^ means the chosen letters)

babgbag
^^ ^
babgbag
^^    ^
babgbag
^    ^^
babgbag
  ^  ^^
babgbag
    ^^^
'''

import sys, optparse, os

class Solution(object):
    def numDistinct(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: int
        """

        if len(s) < len(t):
            return 0

        dp = [[0 for _ in range(len(s))] for _ in range(len(t))]

        if s[0] == t[0]:
            dp[0][0] = 1

        for j in range(1, len(s)):
            if s[j] == t[0]:
                dp[0][j] = dp[0][j-1] + 1
            else:
                dp[0][j] = dp[0][j-1]

        print dp


        for i in range(1, len(t)):
            for j in range(i, len(s)):
                if s[j] == t[i]:
                    dp[i][j] = dp[i-1][j-1] + dp[i][j-1]
                else:
                    dp[i][j] = dp[i][j-1]

            print dp


        return dp[-1][-1]



# s = "rabbbit"
# t = "rabbit"

s = "babgbag"
t = "bag"

solution = Solution()
result = solution.numDistinct(s, t)
print result

'''
Complexity Analysis
Time complexity: O(m*n), where m = length of s, n = length of t.
    Dynamic programming, We compare each letter in s with each letter in t.


Space complexity: O(m * n)
    Extra space is used to store dp result.
    But could be O(n) since only two row in the matrix are needed to store result.

'''
