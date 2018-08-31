'''
Validate if a given string is numeric.

Examples:
"0" => true
" 0.1 " => true
"abc" => false
"1 a" => false
"2e10" => true
'''

import sys, optparse, os

class Solution(object):
    def isNumber(self, s):
        """
        :type s: str
        :rtype: bool
        """

        s = s.strip()

        if not s:
            return False

        if len(s) == 1 and (s[0] == "." or s[0] == "e"):
            return False

        numbers = [str(i) for i in range(10)]

        state = [
            # begining state, stat 0
            {"digit": 1, "sign": 2, "dot":3},
            # stat 1, possible char following a digit
            {'digit':1, 'ten_power':4, "dot": 5},
            # stat 2, possible char following +/-
            {'digit':1, 'dot':3},
            # stat 3, possible char following a "."
            {'digit':5},
            # stat 4, possible char following "e"
            {'digit':7, 'sign':6},
            # stat 5, possible char following a digit or "e"
            {'digit':5, 'ten_power':4},
            # stat 6, possible char following +/-
            {'digit':7},
            # stat 7, possible char following a digit
            {'digit':7}
        ]

        current_state = 0

        for char in s:
            char_type = ""
            if char in numbers:
                char_type = "digit"
            if char == ".":
                char_type = "dot"
            if char in ["+", "-"]:
                char_type = "sign"
            if char == "e":
                char_type = "ten_power"
            
            if char_type not in state[current_state].keys():
                return False
            current_state = state[current_state][char_type]

        if current_state not in [1, 5, 7]:
            return False

        return True


s = "-.55"

solution = Solution()
result = solution.isNumber(s)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one passes through the string,

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''
