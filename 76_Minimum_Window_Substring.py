'''
Given a string S and a string T,
find the minimum window in S which will contain all the characters in T in complexity O(n).

Note:
1. If there is no such window in S that covers all characters in T, return the empty string "".
2. If there is such window, there will always be only one unique minimum window in S.

Example 1:
Input: S = "ADOBECODEBANC", T = "ABC"
Output: "BANC"

'''

import sys, optparse, os, collections

class Solution:
    def minWindow(self, s, t):
        """
        :type s: str
        :type t: str
        :rtype: str
        """

        """
        We can use a simple sliding window approach to solve this problem.
        
        In any sliding window based problem we have two pointers.
        One right pointer whose job is to expand the current window,
        and one left pointer whose job is to contract a given window.
        At any point in time only one of these pointers move and the other one remains fixed.

        Algorithm:

        1. We start with left pointers whick initially pointing to the first element of the string S.
        2. We use the right pointer to expand the window until we get a desirable window, 
           i.e. a window that contains all of the characters of T.
        3. Once we have a window with all the characters, we can move the left pointer ahead one by one.
           If the window is still a desirable one, we keep on updating the minimum window size.
        4. If the window is not desirable any more, we repeat step2 onwards.

        """

        # hash table that stores char frequency in T
        needed_char = collections.Counter(t)
        # a Counter is an unordered collection where elements are stored as dictionary keys and their counts are stored as dictionary values
        missing = len(t)
        left = 0

        start, end = 0, 0

        # sliding window pointer right starts from 1
        for right, char in enumerate(s, 1):
            # a char not existing in the Counter has default value 0
            if needed_char[char] > 0:
                missing -= 1
            needed_char[char] -= 1

            if missing == 0:
                # remove chars that not in T, or chars in T but more than needed,
                # to find the real left pointer
                while needed_char[s[left]] < 0:
                    needed_char[s[left]] += 1
                    left += 1

                if end == 0 or right - left < end - start:
                    start, end = left, right

                # now s[left] is a char in T and needed_char[s[left]] == 0
                needed_char[s[left]] += 1
                missing += 1
                left += 1

        return s[start:end]


S = "ADOBECODEBANC"
T = "ABC"

solution = Solution()
result = solution.minWindow(S, T)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We do a simple linear scan of the string S.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''

