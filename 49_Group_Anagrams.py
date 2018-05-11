'''
Given an array of strings, group anagrams together.

Note:
All inputs will be in lowercase.
The order of your output does not matter.


Example:

Input: ["eat", "tea", "tan", "ate", "nat", "bat"],
Output: 
[
    ["ate","eat","tea"],
    ["nat","tan"],
    ["bat"]
]

'''

import sys, optparse, os
import collections

class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """

        '''
        Approach #1: Categorize by Sorted String [Accepted]

        Two strings are anagrams if and only if their sorted strings are equal.

        Maintain a dictionary with (String: List) as key-value pairs,
        where each key K is a sorted string, 
        and each value is the list of strings from the initial input that when sorted, are equal to K.

        In Python, we will store the key as a hashable tuple, eg. ('c', 'o', 'd', 'e').

        Complexity Analysis
        Time complexity : O(n*k*log(k)).
            where n is the length of strs, and k is the maximum length of a string in strs.
            The outer loop has complexity O(n) as we iterate through each string.
            Then, we sort each string in O(k*logk) time.

        Space complexity : O(n*k).
            The total information content stored in ans.

        '''

        # ans = collections.defaultdict(list)
        # for s in strs:
        #     ans[tuple(sorted(s))].append(s)
        # return ans.values()

        '''
        Approach #2: Categorize by Count

        We can transform each string s into a character count, count,
        consisting of 26 non-negative integers representing the number of a's, b's, c's, etc. 
        We use these counts as the basis for our hash map.

        In python, the representation will be a tuple of the counts.
        For example, abbccc will be (1, 2, 3, 0, 0, ..., 0), where again there are 26 entries total.

        ord(c):
            Given a string of length one, return an integer representing the Unicode code point of the character
        when the argument is a unicode object, or the value of the byte when the argument is an 8-bit string.
        e.g.
            ord('a') returns the integer 97, 
            ord(u'\u2020') returns 8224
        '''

        anagrams_group_dic = collections.defaultdict(list)

        for word in strs:
            char_count = [0] * 26
            for character in word:
                char_index = ord(character) - ord("a")
                char_count[char_index] += 1
            anagrams_group_dic[tuple(char_count)].append(word)

        return anagrams_group_dic.values()



strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

solution = Solution()
result = solution.groupAnagrams(strs)
print result


'''
Complexity Analysis
Time complexity : O(n*k). 
    Where n is the length of strs, and k is the maximum length of a string in strs.
    Counting each string is linear in the size of the string, and we count every string.

Space complexity : O(n*k).
    The total information content stored in dictionary.
'''
