'''
Given a non-empty binary tree, find the maximum path sum.

For this problem, a path is defined as any sequence of nodes 
from some starting node to any node in the tree along the parent-child connections.

The path must contain at least one node and does not need to go through the root.

Example 1:
Input: [1,2,3]
       1
      / \
     2   3

Output: 6 = 2+1+3

Example 2:
Input: [-10,9,20,null,null,15,7]
   -10
   / \
  9  20
    /  \
   15   7

Output: 42 = 15+20+7

'''

import sys, optparse, os

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        max_path_sum = float("-inf")

        def currentNode_maxSum(node):
            if not node:
                return 0
            left_max_sum = max(0, currentNode_maxSum(node.left))
            right_max_sum = max(0, currentNode_maxSum(node.right))
            nonlocal max_path_sum
            # maximum path sum consists of current node, its left subtree and right subtree
            max_path_sum = max(max_path_sum, left_max_sum + node.val + right_max_sum)
            # or maximum path sum consists of current node, one of its subtree, and its ancestor nodes
            return node.val + max(left_max_sum, right_max_sum)

        currentNode_maxSum(root)

        return max_path_sum


root = [-10,9,20,null,null,15,7]

solution = Solution()
result = solution.maxPathSum(root)
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
