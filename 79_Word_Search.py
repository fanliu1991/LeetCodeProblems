'''
Given a 2D board and a word,
find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell,
where "adjacent" cells are those horizontally or vertically neighboring.

The same letter cell may not be used more than once.


Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.

'''

import sys, optparse, os

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """

        if word == "":
            return True

        if not board or board[0] == []:
            return False

        row = len(board)
        column = len(board[0])

        def word_search_at(i, j, word):
            if word == "":
                return True

            if i < 0 or i >= row or j < 0 or j>= column:
                return False

            if word[0] != board[i][j]:
                return False
            else:
                tmp = board[i][j]
                # set the matched cell to "#" to avoid be searched again
                board[i][j] = "#"

                result = word_search_at(i-1, j, word[1:]) \
                or word_search_at(i+1, j, word[1:]) \
                or word_search_at(i, j-1, word[1:]) \
                or word_search_at(i, j+1, word[1:])

                # since list is mutable,
                # current modified cell need to be changed back to original value 
                # to avoid affect following search
                board[i][j] = tmp
                return result

        for i in range(row):
            for j in range(column):
                if word_search_at(i, j, word) == True:
                    return True

        return False



board = [
    ["C","A","A"],
    ["A","A","A"],
    ["B","C","D"]
]

word = "AAB"

solution = Solution()
result = solution.exist(board, word)
print result

'''
Complexity Analysis
Time complexity : 
    Depth First Search solution, the worst time complexity is O(n * m * 4^(word_length)).

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
