'''
A message containing letters from A-Z is being encoded to numbers using the following mapping:

'A' -> 1
'B' -> 2
...
'Z' -> 26

Given a non-empty string containing only digits, determine the total number of ways to decode it.


Example 1:

Input: "12"
Output: 2
Explanation: It could be decoded as "AB" (1 2) or "L" (12).

Example 2:

Input: "226"
Output: 3
Explanation: It could be decoded as "BZ" (2 26), "VF" (22 6), or "BBF" (2 2 6).
'''


import sys, optparse, os

class Solution(object):
    def numDecodings(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        Dynamic Programming:

        dp[0] means the way to decode s[0], and dp[1] means the way to decode s[0] + s[1].
        then for s[0] + s[1] + s[2], dp[2] checks one digit, s[2], and two digit combination s[1] + s[2],
        and save the results along the way.

        In the end, dp[n] will be the end result.
        """

        if s == "":
            return 0

        dp = [0 for x in range(len(s))]

        if s[0] == "0":
            return 0
        else:
            dp[0] = 1
            if len(s) >= 2:
                if s[1] == "0":
                    if s[0:2] < "27": # e.g. "30"
                        dp[1] = 1
                    else:
                        dp[1] = 0
                else:
                    if s[0:2] < "27":
                        dp[1] = 2 # e.g. "24"
                    else:
                        dp[1] = 1 # e.g. "28"

        for i in range(2, len(s)):
            if s[i] != "0":
                dp[i] += dp[i-1]
            if s[i-1:i+1] > "09" and s[i-1:i+1] < "27":
                dp[i] += dp[i-2]
            # in case of "101", dp[2] = dp[1], but can not add dp[0]
        return dp[-1]


s = "110"

solution = Solution()
result = solution.numDecodings(s)
print result

'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the string.

Space complexity : O(n).
    Extra space is used to store dp result.
'''

