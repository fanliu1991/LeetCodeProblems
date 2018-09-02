'''
Given an array of words and a width maxWidth,
format the text such that each line has exactly maxWidth characters and is fully justified.

Words are packed as many as possible in in each line.

Pad extra spaces ' ' when necessary so that each line has exactly maxWidth characters.
Extra spaces between words should be distributed as evenly as possible.
If the number of spaces on a line do not divide evenly between words,
the empty slots on the left will be assigned more spaces than the slots on the right.

For the last line of text, it should be left justified and no extra space is inserted between words.

Note:
Each word's length is guaranteed to be greater than 0 and not exceed maxWidth.
The input array words contains at least one word.

Example 1:
Input:
words = ["This", "is", "an", "example", "of", "text", "justification."]
maxWidth = 16

Output:
[
   "This    is    an",
   "example  of text",
   "justification.  "
]

Example 2:
Input:
words = ["What","must","be","acknowledgment","shall","be"]
maxWidth = 16

Output:
[
  "What   must   be",
  "acknowledgment  ",
  "shall be        "
]

Explanation: Note that the second line is left-justified becase it contains only one word.

'''

import sys, optparse, os

class Solution:
    def fullJustify(self, words, maxWidth):
        """
        :type words: List[str]
        :type maxWidth: int
        :rtype: List[str]
        """

        res = []
        current_string = []
        current_len = 0

        for word in words:
            if current_len + len(current_string) + len(word) > maxWidth:
                total_space = maxWidth - current_len
                if len(current_string) == 1:
                    current_string[0] += " " * total_space
                else:
                    avg_space, left_space = divmod(total_space, len(current_string) - 1)
                    for i in range(len(current_string) - 1):
                        current_string[i] += " " * avg_space
                        if i < left_space:
                            current_string[i] += " "
                res.append("".join(current_string))
                current_string = []
                current_len = 0

            current_string.append(word)
            current_len += len(word)

        # last line is left justified, all extra spaces are inserted to right side
        last_line = " ".join(current_string) + " " * (maxWidth - current_len - (len(current_string) - 1))

        return res + [last_line]


words = ["Science","is","what","we","understand","well","enough","to","explain",
         "to","a","computer.","Art","is","everything","else","we","do"]
maxWidth = 20

solution = Solution()
result = solution.fullJustify(words, maxWidth)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We do a simple linear scan of the array of words.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''

