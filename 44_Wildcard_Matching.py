'''
Given an input string (s) and a pattern (p), implement wildcard pattern matching with support for '?' and '*'.

'?' Matches any single character.
'*' Matches any sequence of characters (including the empty sequence).

The matching should cover the entire input string (not partial).

Note:
s could be empty and contains only lowercase letters a-z.
p could be empty and contains only lowercase letters a-z, and characters like ? or *.


Example 1:

Input: 
s = "aa"
p = "a"

Output: false
Explanation: "a" does not match the entire string "aa".

Example 2:

Input: 
s = "aa"
p = "*"

Output: true
Explanation: '*' matches any sequence.

Example 3:

Input:
s = "cb"
p = "?a"

Output: false
Explanation: '?' matches 'c', but the second letter is 'a', which does not match 'b'.

Example 4:

Input:
s = "adceb"
p = "*a*b"

Output: true
Explanation: The first '*' matches the empty sequence, while the second '*' matches the substring "dce".

Example 5:

Input:
s = "acdcb"
p = "a*c?b"

Output: false


'''

import sys, optparse, os

class Solution(object):
    def isMatch(self, s, p):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        '''
        For a 2d table, table[i][j] would mean whether sub-string s[:i] matches sub-pattern p[:j].

                    *   a   *
                0   1   2   3   p
            s
            0   T   T   F   F
        b   1   F   T   F   F
        a   2   F   T   T   T
        a   3   F   T   T   T
        a   4   F   T   T   T

        '''

        if not p:
            return not s

        res = [[None for _ in range(len(p) + 1)] for _ in range(len(s) + 1)]
        res[0][0] = True

        # whether p[:i] matches an empty s
        for i in range(1, len(p) + 1):
            if p[i - 1] == '*':
                res[0][i] = res[0][i - 1]
            else:
                res[0][i] = False

        # whether an empty p matches s[:i]
        for i in range(1, len(s) + 1):
            res[i][0] = False

        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == '?' or p[j - 1] == s[i - 1]:
                    res[i][j] = res[i - 1][j - 1]
                elif p[j - 1] == '*':
                    res[i][j] = res[i - 1][j] or res[i][j - 1]
                    # res[i - 1][j] :
                    #   whether p[:j] + "*" mathes s[:i-1], if yes, the "*" will represent one more character s[i]
                    #   e.g. e1

                    # res[i][j - 1] : 
                    #   whether p[:j] mathes s[:i], if yes, p[:j] extend with "*" also matches s[:i],
                    #   where "*" represent empty sequence
                    #   e.g. e2
                else:
                    res[i][j] = False
        
        return res[len(s)][len(p)]

        '''
                    a   b   *   c   d   ?   i   *   d   e
                0   1   2   3   4   5   6   7   8   9   10  p
            s
            0   T   F   F   F   F   F   F   F   F   F   F
        a   1   F   T   F   F   F   F   F   F   F   F   F
        b   2   F   F   T   T-e2F   F   F   F   F   F   F
        e   3   F   F   F   T   F   F   F   F   F   F   F
        f   4   F   T   T   T-e1F   F   F   F   F   F   F
        c   5   F   F   F   T-e1T   F   F   F   F   F   F
        d   6   F   F   F   T   F   T   F   F   F   F   F
        g   7   F   F   F   T   F   F   T   F   F   F   F
        i   8   F   F   F   T   F   F   F   T   T-e2F   F
        e   9   F   F   F   T   F   F   F   F   T   F   F
        s   10  F   F   F   T   F   F   F   F   T   F   F
        c   11  F   F   F   T   T   F   F   F   T   F   F
        d   12  F   F   F   T   F   T   F   F   T   T   F
        f   13  F   F   F   T   F   F   T   F   T   F   F
        i   14  F   F   F   T   F   F   F   T   T   F   F
        m   15  F   F   F   T   F   F   F   F   T   F   F
        d   16  F   F   F   T   F   F   F   F   T   T   F
        e   17  F   F   F   T   F   F   F   F   T   F   T

        '''

# s = "abefcdgiescdfimde"
# p = "ab*cd?i*de"

# s="aaaa"
# p="***a"

# s = "c"
# p = "*?*" # True
# p ="?*?" # False

s="baaa"
p="*a*"

solution = Solution()
result = solution.isMatch(s, p)
print result


'''
Complexity Analysis
Time complexity : O(n^2).
    A iteration of p is needed for each character in s.


Space complexity : O(n^2).
    Extra space for matrix is used. 
'''
