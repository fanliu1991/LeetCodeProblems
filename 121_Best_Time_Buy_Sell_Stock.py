'''
Given an array for which the ith element is the price of a given stock on day i.
Design an algorithm to find the maximum profit by completing at most one transaction, 
i.e. buy one and sell one share of the stock.

Note: you cannot sell a stock before you buy one.

Example 1:

Input: [7,1,5,3,6,4]
Output: 5
Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
             Not 7-1 = 6, as selling stock needs to be after buying it.

Example 2:

Input: [7,6,4,3,1]
Output: 0
Explanation: In this case, no transaction is done, i.e. max profit = 0.
'''

import sys, optparse, os

class Solution:
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """

        if not prices:
            return 0

        profit = 0
        min_price = float("inf")

        for day in range(len(prices)):
            if prices[day] <= min_price:
                min_price = prices[day]
            elif prices[day] - min_price >= profit:
                profit = prices[day] - min_price

        return profit



prices = [2,4,1]

solution = Solution()
result = solution.maxProfit(prices)
print result

'''
Complexity Analysis
Time complexity: O(n).
    We are doing a single pass through the price array, hence n steps,
    where n is the length of price array.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''
