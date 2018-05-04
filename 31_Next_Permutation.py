'''
Rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Example:

Input -> Output:

1,2,3 -> 1,3,2  // because 132 is the next number that larger than 123
3,2,1 -> 1,2,3  // no numbers permutation is larger than 321, so return lowest number 123
1,1,5 -> 1,5,1  // because 151 is the next number that larger than 115
'''

import sys, optparse, os

class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void, Do not return anything, modify nums in-place instead.
        """

        """
        given numbers 1,2,3,4,5,6
        lower number is the one with ascending order, 123456
        highest number is the one with descending order, 654321

        e.g. if nums = 153642, then next number is 154236

        We need to find the first pair of two successive numbers from the end of list 
        such that nums[i-1] < nums[i], 
        then no rearrangements to the right of nums[i-1] can create a larger permutation since that subarray consists of numbers in descending order.
        we need to rearrange the numbers to the right of nums[i-1] including itself.

        To create the permutation just larger than the current one, 
        we need to replace the number nums[i-1] with the number which is just larger than itself among the numbers lying to its right section, say nums[j].
        
        We swap the numbers nums[i-1] and nums[j], we now have the correct number at index i-1.
        To get the smallest permutation that can be formed by using the numbers only to the right of nums[i-1], we need to place those numbers in ascending order.

        But, while scanning the numbers from the right, all numbers to the right of nums[i-1] were already sorted in descending order, 
        swapping nums[i-1] and nums[j] didn't change that order. 
        Therefore, we simply need to reverse the numbers following nums[i-1] to get the next smallest lexicographic permutation.

        """

        def reverse(nums, left):
            right = len(nums) - 1
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left +=1
                right -=1


        i = len(nums) - 1
        print("original nums:", nums)

        while i>0 and nums[i-1] >= nums[i]: # descending order at right of nums[i-1]
            i-=1

        if i>0:
            j = len(nums) - 1
            while j > i-1 and nums[j] <= nums[i-1]:
                j-=1
            nums[i-1], nums[j] = nums[j], nums[i-1]

        # reverse the numbers following nums[i-1]
        reverse(nums, i)
        print("next permutation nums:", nums)

        return "Done"




nums = [1,5,3,6,4,2]

solution = Solution()
result = solution.nextPermutation(nums)
print result

'''
Complexity Analysis
Time complexity : O(n).
    In worst case, only two scans of the whole array are needed.

Space complexity : O(1).
    No extra space is used. In place replacements are done.
'''