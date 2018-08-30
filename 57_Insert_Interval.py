'''
Given a set of non-overlapping intervals, 
insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.

Example 1:

Input: intervals = [[1,3],[6,9]], newInterval = [2,5]
Output: [[1,5],[6,9]]

Example 2:

Input: intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]], newInterval = [4,8]
Output: [[1,2],[3,10],[12,16]]
Explanation: Because the new interval [4,8] overlaps with [3,5],[6,7],[8,10].

'''

import sys, optparse, os

class Solution:
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[Interval]
        :type newInterval: Interval
        :rtype: List[Interval]
        """

        '''
        First, collect the intervals strictly left or right of the new interval, 
        then merge the new one with the middle ones (if any),
        finally insert it between left and right ones
        '''

        s, e = newInterval.start, newInterval.end

        left = [i for i in intervals if i.end < s]
        right = [i for i in intervals if i.start > e]

        if left + right != intervals:
            s = min(s, intervals[len(left)].start)
            e = max(e, intervals[-len(right)-1].end)

        return left + [Interval(s, e)] + right



intervals = [[1,2],[3,5],[6,7],[8,10],[12,16]]
newInterval = [4,8]

solution = Solution()
result = solution.insert(intervals, newInterval):
print result


'''
Complexity Analysis
Time complexity : O(n).
    We do a simple linear scan of the list

Space complexity : O(n).
    We must allocate linear space to store two copies of part of intervals.
'''
