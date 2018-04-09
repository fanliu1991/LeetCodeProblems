'''
There are two sorted arrays A and B of size m and n respectively.
Find the median of the two sorted arrays. The overall run time complexity should be O(log (m+n)).

Example 1:

A = [1, 3]
B = [2]

The median is 2.0


Example 2:

A = [1, 2]
B = [3, 4]

The median is (2 + 3)/2 = 2.5


'''
import sys, optparse, os

class Solution(object):
    def findMedianSortedArrays(self, A, B):
        """
        :type A: List[int]
        :type B: List[int]
        :rtype: float
        """

        '''
            left_part          |        right_part
        A[0], A[1], ..., A[i-1]  |  A[i], A[i+1], ..., A[m-1]
        B[0], B[1], ..., B[j-1]  |  B[j], B[j+1], ..., B[n-1]

        If we can ensure:
        1. len(left_part) = len(right_part)
        2. max(left_part) <= min(right_part)
        then we divide all elements in {A,B} into two parts with equal length, and one part is always greater than the other. Then
            median = [max(left_part) + min(right_part)] / 2

        To ensure these two conditions, we just need to ensure:
        1. i+j = m-i+n-j (or: m-i+n-j+1)
        2. B[j-1] <= A[i] and A[i-1] <= B[j]

        '''

        m, n= len(A), len(B)
        if m > n:
            # A, B = B, A
            # m, n= len(A), len(B)
            A, B, m, n = B, A, n, m

        imin, imax, half_len = 0, m, (m+n+1)/2

        while imin <= imax:
            i = (imin + imax) / 2
            j = half_len - i
            if i < m and A[i] < B[j-1]:
                # i is too small, must increase it
                imin = i + 1
            elif i > 0 and A[i-1] > B[j]:
                # i is too big, must decrease it
                imax = i - 1
            else:
                # i is perfect

                if i == 0:
                    max_of_left = B[j-1]
                elif j == 0:
                    max_of_left = A[i-1]
                else:
                    max_of_left = max(A[i-1], B[j-1])

                if (m + n) % 2 == 1:
                    return max_of_left

                if i == m:
                    min_of_right = B[j]
                elif j == n:
                    min_of_right = A[i]
                else:
                    min_of_right = min(A[i], B[j])

                return (max_of_left + min_of_right) / 2.0

A = [1, 3, 5]
B = [2, 4]

solution = Solution()
median = solution.findMedianSortedArrays(A, B)
print median

'''
Complexity Analysis
Time complexity : O(log(min(m, n))).
    At first, the searching range is [0,m]. And the length of this searching range will be reduced by half after each loop. So, we only need log(m) loops.
    Since we do constant operations in each loop, so the time complexity is O(log(m)), Since m <= n, so the time complexity is O(log(min(m, n)))

Space complexity : O(1).
    We only need constant memory to store 9 local variables, so the space complexity is O(1).
'''