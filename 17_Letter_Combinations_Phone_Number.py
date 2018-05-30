'''
Given a digit string, return all possible letter combinations that the number could represent.
A mapping of digit to letters (just like on the telephone buttons) is given below.
1:
2: a, b, c
3: d, e, f
4: g, h, i
5: j, k, l
6: m, n, o
7: p, q, r, s
8: t, u, v
9: w, x, y, z

Example:

Input:Digit string "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].

'''
import sys, optparse, os

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        if digits == "":
            return []

        digit_letter_map = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        letters = []
        for num in digits:
            letters.append(digit_letter_map[num])
        
        combination = reduce(lambda x, y: [c1 + c2 for c1 in x for c2 in y], letters, [""])
        
        return combination

# reduce(function, iterable[, initializer])
# Apply function of two arguments cumulatively to the items of iterable, from left to right, so as to reduce the iterable to a single value.
# For example, reduce(lambda x, y: x+y, [1, 2, 3, 4, 5]) calculates ((((1+2)+3)+4)+5)
# The left argument, x, is the accumulated value and the right argument, y, is the update value from the iterable.

digits = "456"

solution = Solution()
result = solution.letterCombinations(digits)
print result

"""
Complexity Analysis

"""
