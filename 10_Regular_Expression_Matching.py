 #!/usr/bin/python
 # -*- coding: utf-8 -*-
'''
Implement regular expression matching with support for "." and "*"

'.' Matches any single character.
'*' Matches zero or more of the preceding element.

The matching should cover the entire input string (not partial).

The function prototype should be:
bool isMatch(const char *s, const char *p)

Some examples:
isMatch("aa","a") -> false
isMatch("aa","aa") -> true
isMatch("aaa","aa") -> false
isMatch("aa", "a*") -> true
isMatch("aa", ".*") -> true
isMatch("ab", ".*") -> true, ".*" means "zero or more (*) of any character (.)".
isMatch("aab", "c*a*b") -> true

'''
import sys, optparse, os

class Solution(object):
    def isMatch(self, text, pattern):
        """
        :type s: str
        :type p: str
        :rtype: bool
        """

        memo = {}
        def dp(i, j):
            if (i, j) not in memo:
                if j == len(pattern):
                    ans = i == len(text)
                else:
                    first_match = i < len(text) and pattern[j] in {text[i], '.'}
                    if j+1 < len(pattern) and pattern[j+1] == '*':
                        ans = dp(i, j+2) or first_match and dp(i+1, j)
                        # dp(i, j+2): '*' represents 0 character, then we may ignore this part of the pattern
                        # first_match and dp(i+1, j): '*' represents 1 or more characters, then we delete a matching character in the text
                        '''
                        dp(i, j+2) or first_match and dp(i+1, j) 
                            is equivalent to 
                        dp(i, j+2) or ( first_match and dp(i+1, j) )
                        Python uses short circuiting when evaluating expressions involving the and or or operators. When using those operators, Python does not evaluate the second operand unless it is necessary to resolve the result.
                        Therefore, if first_match == False, dp(i+1, j) is not evaluated anymore.

                        lowest to highest precedence:
                        Lambda  #运算优先级最低
                        逻辑运算符: or
                        逻辑运算符: and
                        逻辑运算符:not
                        成员测试: in, not in
                        同一性测试: is, is not
                        比较: <,<=,>,>=,!=,==
                        按位或: |
                        按位异或: ^
                        按位与: &
                        移位: << ,>>
                        加法与减法: + ,-
                        乘法、除法与取余: *, / ,%
                        正负号: +x,-x
                        '''
                    else: # there is no '*', so we simply check from left to right if each character of the text matches the pattern.
                        ans = first_match and dp(i+1, j+1)

                memo[i, j] = ans
            return memo[i, j]

        return dp(0, 0)



s = "aaa"
p = "aa"

solution = Solution()
result = solution.isMatch(s, p)
print result

'''
Complexity Analysis
Time complexity : O(n).
    Let T,P be the lengths of the text and the pattern respectively. The work for every call to dp(i, j) for i=0,...,T; j=0,...,P is done once, and it is O(1) work.
    Hence, the time complexity is O(TP).

Space complexity : O(n).
    The only memory we use is the O(TP) boolean entries in our cache. Hence, the space complexity is O(TP).
'''
