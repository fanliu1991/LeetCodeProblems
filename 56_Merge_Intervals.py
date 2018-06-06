'''
Given a collection of intervals, merge all overlapping intervals.

Example 1:

Input: [[1,3],[2,6],[8,10],[15,18]]
Output: [[1,6],[8,10],[15,18]]
Explanation: Since intervals [1,3] and [2,6] overlaps, merge them into [1,6].

Example 2:

Input: [[1,4],[4,5]]
Output: [[1,5]]
Explanation: Intervals [1,4] and [4,5] are considerred overlapping.

'''

import sys, optparse, os

class Solution(object):
    def merge(self, intervals):
        """
        :type intervals: List[Interval]
        :rtype: List[Interval]
        """

        '''
        First, we sort the list by their start value.

        Then, we insert the first interval into our merged list and continue considering each interval in turn as follows:
            If the current interval begins after the previous interval ends, 
        then they do not overlap and we can append the current interval to merged.
            Otherwise, they do overlap, 
        and we merge them by updating the end of the previous interval if it is less than the end of the current interval.
        e.g. [(1, 8), (2, 6)]

        '''

        if not intervals:
            return []
        if len(intervals) == 1:
            return intervals

        intervals.sort(key=lambda x: x.start)
        merged = [intervals[0]]

        for interval in intervals:
            if merged[-1].end < interval.start:
                merged.append(interval)
            else:
                merged[-1].end = max(merged[-1].end, interval.end)

        return merged



nums = [(1, 9), (2, 5), (19, 20), (10, 11), (12, 20), (0, 3), (0, 1), (0, 2)]
# after sort:
# nums = [(0, 3), (0, 1), (0, 2), (1, 9), (2, 5), (10, 11), (12, 20), (19, 20)]

solution = Solution()
result = solution.merge(nums)
print result


'''
Complexity Analysis
Time complexity : O(nlogn).
    Other than the sort invocation, we do a simple linear scan of the list,
    so the runtime is dominated by the O(nlogn) complexity of sorting.

Space complexity : O(1) (or O(n)).
    If we can sort intervals in place, we do not need more than constant additional space.
    Otherwise, we must allocate linear space to store a copy of intervals and sort that.
'''

