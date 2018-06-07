'''
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

1. "123"
2. "132"
3. "213"
4. "231"
5. "312"
6. "321"

Given n and k, return the k-th permutation sequence.

Note:
Given n will be between 1 and 9 inclusive.
Given k will be between 1 and n! inclusive.


Example 1:

Input: n = 3, k = 3
Output: "213"

Example 2:

Input: n = 4, k = 9
Output: "2314"

'''

import sys, optparse, os

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """

        '''
        For permutations of n, the first (n-1)! permutations start with 1,
        next (n-1)! ones start with 2, ... and so on. 

        And in each group of (n-1)! permutations,
        the first (n-2)! permutations start with the smallest remaining number.

        e.g. n = 3
        The first 2 (that is, (3-1)!) permutations start with 1, next 2 start with 2 and last 2 start with 3. 

        For the first 2 permutations (123 and 132), the 1st one (1!) starts with 2,
        which is the smallest remaining number (2 and 3)

        So we can use a loop to check the region that the sequence number falls in and get the starting digit.
        Then we adjust the sequence number and continue.

        '''

        numbers = range(1, n+1)
        k = k - 1
        permutation = ""

        factorial = [1] * n
        for i in range(1, n):
            factorial[i] = factorial[i-1] * i

        while n > 0:
            n = n-1
            group_index, k = divmod(k, factorial[n])
            permutation += str(numbers[group_index])
            numbers.pop(group_index)

        return permutation


n = 4
k = 9

solution = Solution()
result = solution.getPermutation(n, k)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing n passes through the numbers array.

Space complexity : O(n).
    Extra space is used to store n factorial numbers.
'''

