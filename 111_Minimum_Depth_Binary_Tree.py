'''
Given a binary tree, find its minimum depth.
The minimum depth is the number of nodes along the shortest path 
from the root node down to the nearest leaf node.

Note: A leaf is a node with no children.

Example:
Input: Given binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

Output: its minimum depth = 2.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys, optparse, os

class Solution:
    def minDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        """
        Given [1,2] as below,
                    1
                   /
                  2
        its minimum depth = 2 since 2 is a left node that with no children.
        Therefore, if a node has only one child, its depth = child depth + 1, 
        but not 1 + min(0, child depth) = 1.
        """

        if root == None:
            return 0

        left_height = self.minDepth(root.left)
        right_hight = self.minDepth(root.right)
        
        if not left_height or not right_hight:
            return left_height + right_hight + 1
        else:
            return 1 + min(left_height, right_hight)


root = [3,9,20,null,null,15,7]

solution = Solution()
result = solution.minDepth(root)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We traverse the entire input tree once, the total run time is O(n), 
    where n is the total number of nodes in the tree.

Space complexity : O(logN).
    The number of calls is bound by the height of the tree.
    But in the worst case, the tree is linear, i.e. each node has only one child.
    Therefore, the height of tree is in O(n), 
    space complexity due to recursive calls on the stack is O(n) in the worst case.

'''

