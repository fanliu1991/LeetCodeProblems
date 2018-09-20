'''
Given two words (beginWord and endWord), and a dictionary's word list, 
find the length of shortest transformation sequence from beginWord to endWord, such that:
1. Only one letter can be changed at a time.
2. Each transformed word must exist in the word list. Note that beginWord is not a transformed word.

Note:
1. Return 0 if there is no such transformation sequence.
2. All words have the same length.
3. All words contain only lowercase alphabetic characters.
4. You may assume no duplicates in the word list.
5. You may assume beginWord and endWord are non-empty and are not the same.

Example 1:

Input:
beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

Output: 5

Explanation: As one shortest transformation is "hit" -> "hot" -> "dot" -> "dog" -> "cog",
return its length 5.

Example 2:

Input:
beginWord = "hit"
endWord = "cog"
wordList = ["hot","dot","dog","lot","log"]

Output: 0

Explanation: The endWord "cog" is not in wordList, therefore no possible transformation.

'''

import sys, optparse, os

class Solution:
    def ladderLength(self, beginWord, endWord, wordList):
        """
        :type beginWord: str
        :type endWord: str
        :type wordList: List[str]
        :rtype: int
        """

        if endWord not in wordList:
            return 0

        front_transformed = {beginWord}
        # i.e.
        # front_transformed = set()
        # front_transformed.add(beginWord)
        back_transformed = {endWord}
        wordList = set(wordList)
        length = 1

        while front_transformed:
            length += 1
            next_transformed = set()

            for word in front_transformed:
                  for ch in "abcdefghijklmnopqrstuvwxyz":
                        for i in range(len(word)):
                            if ch != word[i]:
                                transformed_word = word[:i] + ch + word[i+1:]
                                if transformed_word in back_transformed:
                                    return length
                                if transformed_word in wordList:
                                    next_transformed.add(transformed_word)
                                    wordList.remove(transformed_word)

            front_transformed = next_transformed
            if len(back_transformed) < len(front_transformed):
                front_transformed, back_transformed = back_transformed, front_transformed

        """
        # works solution, but Time Limit Exceeded
        transformed_words = {beginWord}
        wordList = set(wordList)
        length = 1

        while transformed_words:
            length += 1
            next_transformed = set()
            left_wordList = set()

            for word in transformed_words:
                  for i in range(len(word)):
                    if word[:i] == endWord[:i] and word[i+1:] == endWord[i+1:]:
                        return length
                    for transformed_word in wordList:
                        if word[:i] == transformed_word[:i] and word[i+1:] == transformed_word[i+1:]:
                            next_transformed.add(transformed_word)
                        else:
                            left_wordList.add(transformed_word)

            transformed_words = next_transformed
            wordList = left_wordList
        """

        return 0

beginWord = "hit",
endWord = "cog",
wordList = ["hot","dot","dog","lot","log","cog"]

solution = Solution()
result = solution.ladderLength(beginWord, endWord, wordList)
print result

'''
Complexity Analysis
Time complexity: O(n^2), where n is the length of wordList.
    For each transformed word, we compare it with the words in the rest of wordList.
    and split wordList to new transformed words list and rest of them.

Space complexity : O(n).
    Extra space is used to store transformed words and rest of wordList.
'''
