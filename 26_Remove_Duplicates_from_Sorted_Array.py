'''
Given a sorted array, remove the duplicates in-place such that each element appear only once and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

Example:

Given nums = [1,1,2],

return length = 2, with the first two elements of nums being 1 and 2 respectively.
'''
import sys, optparse, os

class Solution(object):
    def removeDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        '''
        Since the array is already sorted, we can keep two pointers i and j, where i is the slow-runner while j is the fast-runner. 
        As long as nums[i] == nums[j], we increment j to skip the duplicate.

        When we encounter nums[j] != nums[i], the duplicate run has ended so we must copy its value to nums[i+1]. 
        i is then incremented and we repeat the same process again until j reaches the end of array.
        '''

        if len(nums) == 0:
            return 0

        slow_runner = 0

        for j in xrange(1, len(nums)):
            if nums[j] != nums[slow_runner]:
                slow_runner += 1
                nums[slow_runner] = nums[j]

        # print nums
        # print nums[:slow_runner+1]

        return slow_runner+1


nums = [1,2,2,3,4,5,5,5,6,7]

solution = Solution()
result = solution.removeDuplicates(nums)
print result

'''
Complexity Analysis
Time complexity : O(n)
    Assume that n is the length of array. Each of i and j traverses at most n steps.

Space complexity : O(1).
'''