'''
Given a string, s, and a list of words, words, that are all of the same length. 

Find all starting indices of substring(s) in s that is a concatenation of each word in words exactly once and without any intervening characters.

Example 1:

Input:
  s = "barfoothefoobarman",
  words = ["foo","bar"]

Output: [0,9]

Explanation: Substrings starting at index 0 and 9 are "barfoor" and "foobar" respectively.

Example 2:

Input:
  s = "wordgoodstudentgoodword",
  words = ["word","student"]

Output: []
'''

import sys, optparse, os

class Solution(object):
    def findSubstring(self, s, words):
        """
        :type s: str
        :type words: List[str]
        :rtype: List[int]
        """

        result = []

        if not words:
            return result
        
        words_num = len(words)
        word_len = len(words[0])
        total_words_len = word_len * words_num
        s_len = len(s)

        if s_len < total_words_len:
            return result

        word_dict = {}
        for word in words:
            word_dict[word] = word_dict.get(word, 0) + 1

        ''' Slow method
        for start in range(s_len - total_words_len + 1):
            substr_dict = {}
            right = start

            for left in range(start, start + total_words_len, word_len):
                temp_right = left + word_len
                substr_word = s[left:temp_right]

                if word_dict.get(substr_word):
                    substr_dict[substr_word] = substr_dict.get(substr_word, 0) + 1
                    if substr_dict[substr_word] > word_dict.get(substr_word):
                        break
                else:
                    break
                right = temp_right

            if right - start == total_words_len:
                result.append(start)
        '''

        ''' Fast method '''
        for start in range(word_len):
            left = start
            substr_dict = {}

            for word_left in range(start, s_len - word_len + 1, word_len):
                right = word_left + word_len
                substr_word = s[word_left:right]

                if word_dict.get(substr_word):
                    substr_dict[substr_word] = substr_dict.get(substr_word, 0) + 1
                    # if a word in the substr occurs more times than that word in the words list,
                    # then shrink the window from the most left word,
                    # until no more word occurs more times than in the words list
                    while substr_dict[substr_word] > word_dict[substr_word]:
                        substr_dict[s[left:left + word_len]] -= 1
                        left += word_len

                    # if the window length equals to result length
                    if right - left == total_words_len:
                        result.append(left)
                        # shrink the window by removing the most left word,
                        substr_dict[s[left:left + word_len]] -= 1
                        left += word_len
                else:
                    # if a word is not in the words list, then all its previous words and itself are shrinked
                    left = right
                    substr_dict = {}

        return result


s = "barfoothefoobarman"
words = ["foo","bar"]

# s = "wordgoodstudentgoodword"
# words = ["word","student"]

solution = Solution()
result = solution.findSubstring(s, words)
print result

'''
Complexity Analysis
Time complexity : 

Space complexity : 
'''