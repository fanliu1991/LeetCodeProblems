'''
Implement strStr().

Return the index of the first occurrence of needle in haystack, or -1 if needle is not part of haystack. 

Example 1:

Input: haystack = "hello", needle = "ll"
Output: 2

Example 2:

Input: haystack = "aaaaa", needle = "bba"
Output: -1

'''

import sys, optparse, os

class Solution(object):
    def strStr(self, haystack, needle):
        """
        :type haystack: str
        :type needle: str
        :rtype: int
        """

        if len(needle) == 0:
            return 0

        if len(needle) > len(haystack):
            return -1

        for i in xrange(len(haystack) - len(needle) + 1):
            # if haystack[i] == needle[0]:
            #     needle_index = i
            #     for j in xrange(len(needle)):
            #         if haystack[needle_index] == needle[j]:
            #             needle_index +=1
            #         else:
            #             break
            #     if needle_index - i == len(needle):
            #         return i

            if haystack[i:i+len(needle)] == needle:
                return i

        return -1

# haystack = "hello"
# needle = "ll"

haystack = "a"
needle = "a"


solution = Solution()
result = solution.strStr(haystack, needle)
print result

'''
Complexity Analysis
Time complexity : O(n)

Space complexity : O(1).
'''