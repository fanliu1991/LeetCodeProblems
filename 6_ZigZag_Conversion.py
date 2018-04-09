'''
Given a string s, write the code that will take a string and make zigzag conversion given a number of rows.

Zigzag conversion:

 1                           2n-1                         4n-3
 2                     2n-2  2n                    4n-4   4n-2
 3               2n-3        2n+1              4n-5       .
 .           .               .               .            .
 .       n+2                 .           3n               .
 n-1 n+1                     3n-3    3n-1                 5n-5
 n                           3n-2                         5n-4

 0                                 2n-2                                   4n-4
 1                           2n-3  2n-1                             4n-5  4n-3
 2                     2n-4        2n                         4n-6        4n-2
 3               2n-5              2n+1                 4n-7              .
 .           .                     .                 .                    .
  .      n+1                       .           3n-1                       .
 n-2  n                            3n-4  3n-2                             5n-6
 n-1                               3n-3                                   5n-5

Example 1:

Input: "PAYPALISHIRING"

P   A   H   N
A P L S I I G
Y   I   R

Output: "PAHNAPLSIIGYIR"

'''
import sys, optparse, os

class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """

        if numRows == 1 or numRows >= len(s):
            return s

        row_strings = [""] * numRows  # return ["", "", "", ..., ""]
        row_index, step = 0, 1

        for letter in s:
            row_strings[row_index] += letter
            if row_index == numRows - 1:  # at the end of column, change dircetion
                step = -1
            elif row_index == 0:  # at the head of column, change direction
                step = 1
            row_index += step

        return "".join(row_strings)


s = "PAYPALISHIRING"

solution = Solution()
result = solution.convert(s, 3)
print result

"""
Complexity Analysis
Time complexity : O(n).
"""
