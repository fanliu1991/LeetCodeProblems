'''
The count-and-say sequence is the sequence of integers with the first five terms as following:

1. 1
2. 11
3. 21
4. 1211
5. 111221

1 is read off as "one 1" or 11.
11 is read off as "two 1s" or 21.
21 is read off as "one 2, then one 1" or 1211.

Given an integer n, generate the n-th term of the count-and-say sequence.

Note: Each term of the sequence of integers will be represented as a string. 


Example 1:

Input: 1
Output: "1"

Example 2:

Input: 4
Output: "1211"

'''

import sys, optparse, os

class Solution(object):
    def countAndSay(self, n):
        """
        :type n: int
        :rtype: str
        """
        integer = "1"

        for _ in range(n-1):
            digit = integer[0]
            digit_count = 0
            output = ""
            for num in integer:
                if num == digit:
                    digit_count += 1
                else:
                    output = output + str(digit_count) + digit
                    digit = num
                    digit_count = 1

            integer = output + str(digit_count) + digit

        return integer


# n = 5

# solution = Solution()
# result = solution.countAndSay(n)
# print result

solution = Solution()
for n in range(1,6):
    result = solution.countAndSay(n)
    print(n, result)

'''
Complexity Analysis
Time complexity : O(logn).
    Binary search solution.

Space complexity : O(1).
    No extra space is used. Only two extra variables left and right are needed.
'''