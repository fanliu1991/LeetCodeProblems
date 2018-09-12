'''
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, 
a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
input: sorted array [-10,-3,0,5,9],

output: One possible answer is: [0,-3,9,-10,null,5], 
which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5

'''

import sys, optparse, os

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """

        if not nums:
            return None

        middle = len(nums) // 2

        root = TreeNode(nums[middle])
        root.left = self.sortedArrayToBST(nums[:middle])
        root.right = self.sortedArrayToBST(nums[middle+1:])

        return root


nums = [-10,-3,0,5,9]

solution = Solution()
result = solution.sortedArrayToBST(nums)
print result


'''
Complexity Analysis
Time complexity : O(n).
    T(n) = 2T(n/2) + O(1)
    We traverse the entire tree to insert every value in the sorted list, 
    the total run time is O(n), where n is the total number of values in the sorted list.

Space complexity : O(logN).
    The number of calls is bound by the height of the tree.
'''

