'''
It takes n steps to climbe a stair and reach to the top.

Each time you can either climb 1 or 2 steps. 
In how many distinct ways can you climb to the top?

Note: Given n will be a positive integer.

Example 1:

Input: 1
Output: 1
Explanation: There is only one way to climb to the top.
1. 1 step

Example 2:

Input: 2
Output: 2
Explanation: There are two ways to climb to the top.
1. 1 step + 1 step
2. 2 steps

Example 3:

Input: 3
Output: 3
Explanation: There are three ways to climb to the top.
1. 1 step + 2 steps
2. 1 step + 1 step + 1 step
3. 2 steps + 1 step

'''

import sys, optparse, os

class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        """

        '''
        The problem seems to be a dynamic programming one.

        Base cases:
        if n <= 0, then the number of ways should be zero.
        if n == 1, then there is only way to climb the stair.
        if n == 2, then there are two ways to climb the stairs. 
            One solution is one step by another; the other one is two steps at one time.

        So given a number of stairs n, 
        if we know the number ways to get to the points [n-1] and [n-2] respectively,
        denoted as n1 and n2, then the total ways to get to the point [n] is n1 + n2.

        Because from the [n-1] point, we can take one single step to reach [n],
        and from the [n-2] point, we could take two steps to get there.

        There is NO overlapping between these two solution sets,
        because we differ in the final step.

        It is clear that this is basically a fibonacci number,
        with the starting numbers as 1 and 2.

        '''

        if n == 0 or n == 1:
            return n

        res = [0 for _ in range(n)]

        res[0] = 1 # n == 1
        res[1] = 2 # n == 2

        for i in range(2, n):
            res[i] = res[i-1] + res[i-2]

        return res[-1]


n = 99

solution = Solution()
result = solution.climbStairs(n)
print result

'''
Complexity Analysis
Time complexity : O(n).
    Dynamic Programming Solution.

Space complexity : O(n).
    Extra space is used to store res list with n elements.
'''
