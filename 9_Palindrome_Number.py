'''
Determine whether an integer is a palindrome. Do this without extra space.

'''
import sys, optparse, os

class Solution(object):
    def isPalindrome(self, x):
        """
        :type x: int
        :rtype: bool
        """
        

        '''
        All negative numbers are not palindrome.

        Now let's think about how to revert the last half of the number. For number 1221, if we do 1221 % 10, we get the last digit 1,
        to get the second to the last digit, we need to remove the last digit from 1221, we could do so by dividing it by 10, 1221 / 10 = 122.
        Then we can get the last digit again by doing a modulus by 10, 122 % 10 = 2, and if we multiply the last digit by 10 and add the second last digit, 1 * 10 + 2 = 12,
        it gives us the reverted number we want. Continuing this process would give us the reverted number with more digits.

        Since we divided the number by 10, and multiplied the reversed number by 10, when the original number is less than the reversed number,
        it means we've processed half of the number digits.

        '''

        if x<0 or (x%10 == 0 and x != 0):
            return False

        reverted_num = 0
        while(x > reverted_num):
            reverted_num = reverted_num * 10 + x % 10
            x = x/10

        # When the length is an odd number, we can get rid of the middle digit by revertedNumber/10
        # For example when the input is 12321, at the end of the while loop we get x = 12, revertedNumber = 123, 
        # since the middle digit doesn't matter in palidrome(it will always equal to itself), we can simply get rid of it.
        return x == reverted_num or x == reverted_num/10;


nums = -123321

solution = Solution()
result = solution.isPalindrome(nums)
print result

'''
Complexity Analysis
Time complexity : O(log10 n).
    We divided the input by 10 for every iteration, so the time complexity is O(log10 n).

Space complexity : O(1).
'''