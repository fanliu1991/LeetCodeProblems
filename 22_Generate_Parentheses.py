'''
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]

'''
import sys, optparse, os

class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """

        '''
            To generate all sequences, we use a recursion.
        All sequences of length n is just '(' plus all sequences of length n-1, and then ')' plus all sequences of length n-1.

            Instead of adding '(' or ')' every time, let's only add them when we know it will remain a valid sequence. 
        We can do this by keeping track of the number of opening and closing brackets we have placed so far.
        We can start an opening bracket if we still have one (of n) left to place. And we can start a closing bracket if it would not exceed the number of opening brackets.
        '''

        ans = []
        def backtrack(S, left, right):
            if len(S) == 2 * n:
                # print "hit", S, left, right
                ans.append(S)
                return
            if left < n:
                # print "1", S+'(', left+1, right
                backtrack(S+'(', left+1, right)
            if right < left:
                # print "2", S+')', left, right+1
                backtrack(S+')', left, right+1)

        S = ''
        left, right = 0, 0

        backtrack(S, left, right)
        return ans


parentheses_num = 2

solution = Solution()
result = solution.generateParenthesis(parentheses_num)
print "==========================="
print result
print len(result)

'''
Complexity Analysis
Time complexity : O(n+m).
    it turns out this is the n-th Catalan number 1/(n+1) * (2n n), which is bounded asymptotically by 4^n/ sqrt(n).
    O(4^n/ sqrt(n)). Each valid sequence has at most n steps during the backtracking procedure.

Space complexity : O(1).
    O(4^n/ sqrt(n)), as described above, and using O(n) space to store the sequence.
'''