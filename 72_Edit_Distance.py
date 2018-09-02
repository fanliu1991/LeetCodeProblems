'''
Given two words word1 and word2,
find the minimum number of operations required to convert word1 to word2.

You have the following 3 operations permitted on a word:
1. Insert a character
2. Delete a character
3. Replace a character

Example 1:
Input: word1 = "horse", word2 = "ros"
Output: 3

Explanation: 
horse -> rorse (replace 'h' with 'r')
rorse -> rose (remove 'r')
rose -> ros (remove 'e')

Example 2:
Input: word1 = "intention", word2 = "execution"
Output: 5

Explanation: 
intention -> inention (remove 't')
inention -> enention (replace 'i' with 'e')
enention -> exention (replace 'n' with 'x')
exention -> exection (replace 'n' with 'c')
exection -> execution (insert 'u')

'''

import sys, optparse, os

class Solution:
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        word1_len = len(word1) + 1
        word2_len = len(word2) + 1

        matrix = [[0] * word1_len for _ in range(word2_len)]

        # situation when word2 = ""
        for j in range(word1_len):
            matrix[0][j] = j

        # situation when word1 = ""
        for i in range(word2_len):
            matrix[i][0] = i

        for i in range(1, word2_len):
            for j in range(1, word1_len):
                matrix[i][j] = min(matrix[i-1][j] + 1, matrix[i][j-1] + 1, matrix[i-1][j-1] + (word2[i-1] != word1[j-1]))

        return matrix[-1][-1]


word1 = "horsero"
word2 = "roso"

solution = Solution()
result = solution.minDistance(word1, word2)
print result


'''
Complexity Analysis
Time complexity : O(m*n), where m = length of word1, n = length of word2.
    Dynamic programming, We compare each letter in word2 with each letter in word1.

Space complexity : O(m*n).
    Extra space is used to store dp result.
    But could be O(n) since only two row in the matrix are needed to store result.
'''

