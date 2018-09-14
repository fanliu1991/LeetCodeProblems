'''
Given a binary tree and a sum, 
determine if the tree has a root-to-leaf path 
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Input: Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1

Output: true, 
as there exist a root-to-leaf path 5->4->11->2 which sum is 22.

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys, optparse, os

class Solution:
    def hasPathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: bool
        """

        if not root:
            return False

        if root.val == sum and root.left == None and root.right == None :
            return True
        else:
            left_subtree = self.hasPathSum(root.left, sum - root.val)
            right_subtree = self.hasPathSum(root.right, sum - root.val)
            return left_subtree or right_subtree


root = [3,9,20,null,null,15,7]
sum = 30

solution = Solution()
result = solution.hasPathSum(root, sum)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We traverse the entire input tree once in the worst case, the total run time is O(n), 
    where n is the total number of nodes in the tree.

Space complexity : O(logN).
    The number of calls is bound by the height of the tree.
    But in the worst case, the tree is linear, i.e. each node has only one child.
    Therefore, the height of tree is in O(n), 
    space complexity due to recursive calls on the stack is O(n) in the worst case.

'''

