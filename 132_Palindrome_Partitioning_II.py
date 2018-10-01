'''
Given a string s, 
partition s such that every substring of the partition is a palindrome.

Return the minimum cuts needed for a palindrome partitioning of s.

Example:
Input: "aab"
Output: 1

Explanation: The palindrome partitioning ["aa","b"] could be produced using 1 cut.

Possible palindrome partitioning:
[
    ["aa","b"],
    ["a","a","b"]
]
'''

import sys, optparse, os

class Solution:
    def minCut(self, s):
        """
        :type s: str
        :rtype: int
        """

        '''
        isPalindrome[left][right]: whether s[left:right+1] is a palindrome, 
        cut_num[right]: the minimum cuts needs for palindrome partitioning of s[:right+1]
        
        If s[left:right+1] is a palindrome and left == 0, then cut_num[right] = 0 
        since cut is not needed before s[right],
        else, one cut is needed between s[:left+1] and s[left:right+1], 
        therefore current cut number = 1 + cut_num[left],
        compare this number with cut_num[right] and take the smaller one.
        '''

        isPalindrome = [[False for _ in range(len(s))] for _ in range(len(s))]
        cut_num = [i for i in range(len(s))]
        
        # Brute force
        # for i in range(len(s)):
        #     for j in range(i, len(s)):
        #         if s[i:j] == s[j:i:-1]:
        #             if i == 0:
        #                 cut_num[j] = 0
        #             else:
        #                 cut_num[j] = min(cut_num[j], 1 + cut_num[i-1])
        '''
        Time complexity: O(n^3)
        Space complexity: O(n)
        '''

        for right in range(len(s)):
            isPalindrome[right][right] = True
            for left in range(right+1):
                if s[left] == s[right] and (right-left <= 1 or isPalindrome[left+1][right-1] == True):
                    isPalindrome[left][right] = True
                    if left == 0:
                        cut_num[right] = 0
                    else:
                        cut_num[right] = min(cut_num[right], 1 + cut_num[left-1])
                        
        return cut_num[-1]


# s = "aab"

# solution = Solution()
# result = solution.minCut(s)
# print result

'''
Complexity Analysis
Time complexity: O(n^2), where n is the length of s.
    Compute O(2^n) kind of partition configuration, 
    and each configuration takes O(1) to check isPalindrome.

Space complexity: O(n^2).
    Dynamic Programming Solution.
    Extra space is used to store partition configuration of s[left:right+1].
'''        
        
     