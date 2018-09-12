'''
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Input: Given binary tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7

Output: true

Example 2:
Input: Given binary tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4

Output: false

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys, optparse, os

class Solution:
    def isBalanced(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        if root == None:
            return True

        def subtree_depth(node):
            if node == None:
                return 0
            left_height = subtree_depth(node.left)
            right_hight = subtree_depth(node.right)

            if left_height == -1 or right_hight == -1 or abs(left_height - right_hight) > 1:
                return -1
            else:
                return 1 + max(left_height, right_hight)

        if subtree_depth(root) == -1:
            return False
        else:
            return True


root = [1,2,2,3,3,null,null,4,4]

solution = Solution()
result = solution.isBalanced(root)
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

