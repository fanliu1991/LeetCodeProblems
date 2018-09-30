'''
Given two words (beginWord and endWord), and a dictionary's word list, 
find all shortest transformation sequence(s) from beginWord to endWord, such that:
1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
1. Return an empty list if there is no such transformation sequence.
2. All words have the same length.
3. All words contain only lowercase alphabetic characters.
4. You may assume no duplicates in the word list.
5. You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 
[
    ["hit","hot","dot","dog","cog"],
    ["hit","hot","lot","log","cog"]
]

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: []

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''

import sys, optparse, os
import collections

class Solution:
    def findLadders(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: List[List[str]]
        """

        if endWord not in wordList:
            return []

        wordList = set(wordList)
        parent_words = collections.defaultdict(set)
        current_words = [beginWord]
        # i.e.
        # front_transformed = set()
        # front_transformed.add(beginWord)

        while current_words and (endWord not in parent_words):
            current_words_parent = collections.defaultdict(set)
            for word in current_words:
                for i in range(len(word)):
                    for ch in "abcdefghijklmnopqrstuvwxyz":
                        if ch != word[i]:
                            child_word = word[:i] + ch + word[i+1:]
                            if child_word in wordList and (child_word not in parent_words):
                                current_words_parent[child_word].add(word)

            current_words = current_words_parent.keys()
            parent_words.update(current_words_parent)


        result = [[endWord]]
        while result and result[0][0] != beginWord:
            extended_seq = []
            for sequence in result:
                head_word = sequence[0]
                for parent in parent_words[head_word]:
                    extended_seq.append([parent]+sequence)

            result = extended_seq
            # extended_seq could be empty if endWord doesn't have parent word in the wordList.
            # e.g.
            #     beginWord = "hot"
            #     endWord = "dog"
            #     wordList = ["hot","dog"]

        return result

beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log","cog"]

solution = Solution()
result = solution.findLadders(beginWord, endWord, wordList)
print result

'''
Complexity Analysis
Time complexity: O(n * k), where n is the length of wordList, and k is the length of word.
    For each word in the wordList, we find its parent words by replacing each letter in the word,
    Once endWord's parent words are found, we could recursively find transformation sequence to beginWord.

Space complexity : O(n).
    Extra space is used to store all parent words of each word in the wordList.
'''
