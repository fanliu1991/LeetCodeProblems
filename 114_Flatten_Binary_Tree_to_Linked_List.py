'''
Given a binary tree, flatten it to a linked list in-place.

Example:
Input: Given the following tree:
    1
   / \
  2   5
 / \   \
3   4   6

Output: The flattened tree:

1
 \
  2
   \
    3
     \
      4
       \
        5
         \
          6

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys, optparse, os

class Solution:
    def flatten(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        if not root:
            return
        
        if root.right != None:
            self.flatten(root.right)

        if root.left != None:
            self.flatten(root.left)

            last_node = root.left
            while last_node.right != None:
                print(last_node.val)
                last_node = last_node.right

            last_node.right = root.right
            root.right = root.left
            root.left = None


root = [1,2,5,3,4,null,6]

solution = Solution()
result = solution.flatten(root)
print result


'''
Complexity Analysis
Time complexity : O(n^2).
    We traverse the entire input tree once to modify each node's left subtree and right subtree,
    for each node, we traverse its left subtree to find the last node, 
    and connect it with nodes's right subtree.

Space complexity : O(1).
    Input tree is modified in-place.

'''

