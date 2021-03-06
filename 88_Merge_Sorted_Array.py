'''
Given two sorted integer arrays nums1 and nums2,
merge nums2 into nums1 as one sorted array.

The number of elements initialized in nums1 and nums2 are m and n respectively.
You may assume that nums1 has enough space (size that is greater or equal to m + n) 
to hold additional elements from nums2.


Example:

Input:
nums1 = [1,2,3,0,0,0], m = 3
nums2 = [2,5,6],       n = 3

Output: [1,2,2,3,5,6]

'''

import sys, optparse, os

class Solution(object):
    def merge(self, nums1, m, nums2, n):
        """
        :type nums1: List[int]
        :type m: int
        :type nums2: List[int]
        :type n: int
        :rtype: void Do not return anything, modify nums1 in-place instead.
        """

        i = m - 1
        j = n - 1
        current = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[current] = nums1[i]
                i -= 1
            else:
                nums1[current] = nums2[j]
                j -= 1
            current -= 1

        if j >= 0: # all elements in nums1 are used
            nums1[:current+1] = nums2[:j+1]
        else: # all elements in nums2 are used
            nums1[:current+1] = nums1[:i+1]

        return nums1


nums1 = [1]
nums2 = []

solution = Solution()
result = solution.merge(nums1, 1, nums2, 0)
print result

'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the linked list

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
