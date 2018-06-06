'''
Given a positive integer n,
generate a square matrix filled with elements from 1 to n^2 in spiral order.

Example:

Input: 3
Output:
[
    [ 1, 2, 3 ],
    [ 8, 9, 4 ],
    [ 7, 6, 5 ]
]

'''

import sys, optparse, os

class Solution(object):
    def generateMatrix(self, n):
        """
        :type n: int
        :rtype: List[List[int]]
        """

        def coordinate_generator(r1, r2, c1, c2):
            if r1 == r2 and c1 == c2:
                yield [r1, c1]
            else:
                for i in range(c1, c2+1):
                    yield [r1, i]
                for i in range(r1+1, r2):
                    yield [i, c2]
                for i in range(c2, c1-1, -1):
                    yield [r2, i]
                for i in range(r2-1, r1, -1):
                    yield [i, c1]


        if n == 0:
            return []
        if n == 1:
            return [[1]]

        result = [[0] * n for _ in range(n)]

        r1, r2 = 0, n-1
        c1, c2 = 0, n-1

        value = 1

        while r1 <= r2 and c1 <= c2:
            for [x, y] in coordinate_generator(r1, r2, c1, c2):
                result[x][y] = value
                value += 1
            r1 += 1
            r2 -= 1
            c1 += 1
            c2 -= 1

        return result


n = 3

solution = Solution()
result = solution.generateMatrix(n)
print result


'''
Complexity Analysis
Time complexity : O(n^2).

Space complexity : O(n^2).

'''

