'''
Given two non-negative integers num1 and num2 represented as strings, return the product of num1 and num2, also represented as a string.

Note:

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.


Example 1:

Input: num1 = "2", num2 = "3"
Output: "6"

Example 2:

Input: num1 = "123", num2 = "456"
Output: "56088"

'''

import sys, optparse, os

class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """

        '''
            num2        4   5   6
            num1        1   2   3
            ----------------------
n1=3, n2=6                  1   8
n1=3, n2=5              1   5
n1=3, n2=4          1   2
n1=2, n2=6              1   2
n1=2, n2=5          1   0
n1=2, n2=4          8
n1=1, n2=6              6
n1=1, n2=5          5
n1=1, n2=6      4
            ----------------------
            0   5   6   0   8   8

        '''

        product = [0] * (len(num1) + len(num2))
        product_start_position = len(product) - 1

        for n1 in reversed(num1):
            digit_position = product_start_position
            for n2 in reversed(num2):
                temp_result = int(n1) * int(n2) + product[digit_position]
                product[digit_position] = temp_result % 10
                product[digit_position-1] += temp_result / 10
                digit_position = digit_position - 1
            product_start_position = product_start_position - 1

        leading_number_position = 0
        for i in range(0, len(product)-1):
            if product[i] == 0:
                leading_number_position += 1
            else:
                break

        leading_number_product = "".join([str(digit) for digit in product[leading_number_position:]])
        return leading_number_product


num1 = "123"
num2 = "456"

solution = Solution()
result = solution.multiply(num1, num2)
print result


'''
Complexity Analysis
Time complexity : O(n^2).
    A iteration of num2 is needed for each digit in num1.


Space complexity : O(n).
    Extra space len(num1) + len(num2) is used. 
'''
