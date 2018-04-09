'''
Given an array and a value, remove all instances of that value in-place and return the new length.

Do not allocate extra space for another array, you must do this by modifying the input array in-place with O(1) extra memory.

The order of elements can be changed. It doesn't matter what you leave beyond the new length.

Example:

Given nums = [3,2,2,3], val = 3,

length = 2, with the first two elements of nums being 2.
'''

import sys, optparse, os

class Solution(object):
    def removeElement(self, nums, val):
        """
        :type nums: List[int]
        :type val: int
        :rtype: int
        """

        '''
        Method 1:
            When nums[j] equals to the given value, skip this element by incrementing j.
            As long as nums[j] != val, we copy nums[j] to nums[i] and increment both indexes at the same time.
            Repeat the process until j reaches the end of the array and the new length is i.
        '''

        # if len(nums) == 0:
        #     return 0

        # i = 0

        # for j in xrange(len(nums)):
        #     if nums[j] != val:
        #         nums[slow_runner] = nums[j]
        #         slow_runner += 1

        # print nums
        # print nums[:slow_runner]

        # return slow_runner

        '''
        Method 2: (when elements to remove are rare)
            When we encounter nums[i] == val, we can swap the current element out with the last element and dispose the last one.
        This essentially reduces the array's size by 1.

            Note that the last element that was swapped in could be the value you want to remove itself. 
        But don't worry, in the next iteration we will still check this element.
        '''

        if len(nums) == 0:
            return 0

        i = 0
        n= len(nums)

        while i < n:
            if nums[i] == val:
                nums[i] = nums[n-1]
                # reduce array size by one
                n -=1
            else:
                i +=1

        print nums
        print nums[:n]

        return n


nums = [1,2,2,3,4,5,5,5,6,7]
val = 2

solution = Solution()
result = solution.removeElement(nums, val)
print result

'''
Complexity Analysis
Time complexity : O(n)
    Method 1:
        Assume that n is the length of array. Each of i and j traverses at most n steps.
    Method 2:
        Both i and n traverse at most n steps. In this approach, the number of assignment operation is equal to the number of elements to remove.
    So it is more efficient if elements to remove are rare.

Space complexity : O(1).
'''