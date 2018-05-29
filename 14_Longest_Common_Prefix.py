'''
Write a function to find the longest common prefix string amongst an array of strings. 

Example:

Given strs = {"leets, leetcode", "leet", "leeds"},

return "lee".

'''
import sys, optparse, os

class Solution(object):
    def longestCommonPrefix(self, strs):
        """
        :type strs: List[str]
        :rtype: str
        """

        if len(strs) == 0:
            return ""

        shortest_str = min(strs, key=len)

        '''
        Vertical scanning:
            compare characters from top to bottom on the same column (same character index of the strings) before moving on to the next column.

        '''

        # for i in xrange(len(shortest_str)):
        #     current_char = shortest_str[i]
        #     for string in strs:
        #         if i == len(string) or string[i] != current_char:
        #             return shortest_str[:i]

        # return shortest_str

        '''
        Binary search:
        '''

        def isCommonPrefix(strs, lcp_string, lcp_index):
            lcp = lcp_string[:lcp_index]
            for string in strs:
                if string[:lcp_index] != lcp:
                    return False
            return True

        low, high = 0, len(shortest_str)

        while(low < high):
            middle = (low + high) / 2
            if isCommonPrefix(strs, shortest_str, middle+1):
                low = middle+1
            else:
                high = middle
        return shortest_str[:low]


strs = {"leets, leetcode", "leet", "leeds", "lee"}

solution = Solution()
lcp = solution.longestCommonPrefix(strs)
print lcp

'''
Complexity Analysis
Time complexity : O(S), where S is the sum of all characters in all strings
    In the worst case there will be n equal strings with length m and the algorithm performs S = m*n character comparisons.
    in the best case there are at most n*minLen comparisons where minLen is the length of the shortest string in the array.

Space complexity : O(1).
    We only used constant extra space.
'''
