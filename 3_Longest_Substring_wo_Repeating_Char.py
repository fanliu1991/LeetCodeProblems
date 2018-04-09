'''
Given a string, find the length of the longest substring without repeating characters.

Example:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring.

'''
import sys, optparse, os

class Solution(object):
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """

        """
        Sliding Window:
            A window is a range of elements in the array/string which usually defined by the start and end indices, i.e. [i,j).
            A sliding window is a window "slides" its two boundaries to the certain direction.

        We use HashSet to store the characters in current window [i,j) (j=i initially). Then we slide the index j to the right. If it is not in the HashSet, we slide j further. Doing so until s[j] is already in the HashSet. At this point, we found the maximum size of substrings without duplicate characters start with index i. If we do this for all i, we get our answer.
        We could define a mapping of the characters to its index. Then we can skip the characters immediately when we found a repeated character.
        The reason is that if s[j] have a duplicate in the range [i,j) with index j_, we don't need to increase i little by little. We can skip all the elements in the range [i,j_] and let i to be j_+1 directly.
        """

        start = 0
        max_length = 0
        used_char = {}

        for i, char in enumerate(s):
            if char in used_char and start <= used_char[char]:
                start = used_char[char] + 1
            else:
                max_length = max(max_length, i-start+1)

            used_char[char] = i

        return max_length


s = "pwwkew"

solution = Solution()
length = solution.lengthOfLongestSubstring(s)
print length

"""
Complexity Analysis
Time complexity : O(n).
    We traverse the list containing nnn elements only once. Each look up in the table costs only O(1)O(1)O(1) time.

Space complexity : O(n).
    The extra space required depends on the number of items stored in the hash table, which stores at most nnn elements.
"""
