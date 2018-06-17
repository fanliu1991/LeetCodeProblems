'''
The gray code is a binary numeral system where two successive values differ in only one bit.

Given a non-negative integer n representing the total number of bits in the code,
print the sequence of gray code. A gray code sequence must begin with 0.

For example, given n = 2, return [0,1,3,2]. Its gray code sequence is:
00 - 0
01 - 1
11 - 3
10 - 2

Note:
For a given n, a gray code sequence is not uniquely defined.
For example, [0,2,3,1] is also a valid gray code sequence according to the above definition.


'''

import sys, optparse, os

class Solution(object):
    def grayCode(self, n):
        """
        :type n: int
        :rtype: List[int]
        """

        """
        n = 0,  0 = 0

        n = 1,  0 = 0
                1 = 1

        n = 2,  00 = 0
                01 = 1
                11 = 3
                10 = 2

        n = 3,  000 = 0
                001 = 1
                011 = 3
                010 = 2

                110 = 6
                111 = 7
                101 = 5
                100 = 4

        for n bits sequence,
        add 2^(n-1) to each value in the reversed sequence of n-1 bits,
        i.e. replace the first bit of n-bit number from 0 to 1,
        will generate the sequence of n bits

        """

        if n == 0:
            return [0]
        # spical case, which should be [], but accepted answer is [0]

        result = [0]

        for i in range(n):
            result = result + [value + 2**i for value in reversed(result)]

        return result


n = 4

solution = Solution()
result = solution.grayCode(n)
print result

'''
Complexity Analysis
Time complexity : O(2^n).
    We are doing one pass through each of the list
    with length 2, 4, 8, ..., 2^(n-1).

Space complexity : O(2^n).
    Extra space is used to store 2^n values of n bits sequence.

'''
