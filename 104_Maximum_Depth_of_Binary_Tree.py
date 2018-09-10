'''
Given a binary tree, find its maximum depth.
The maximum depth is the number of nodes along the longest path 
from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
input: binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7

output: 3

'''

import sys, optparse, os

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def maxDepth(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if root == None:
            return 0

        def dfs(root, current_depth):
            if root == None:
                return current_depth
            else:
                left_depth = dfs(root.left, current_depth + 1)
                right_depth = dfs(root.right, current_depth + 1)
                return max(left_depth, right_depth)

        left_subtree_depth = dfs(root.left, 1)
        right_subtree_depth = dfs(root.right, 1)

        return max(left_subtree_depth, right_subtree_depth)



root = [3,9,20,null,null,15,7]

solution = Solution()
result = solution.maxDepth(root)
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

