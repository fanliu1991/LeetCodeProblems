'''
Given a binary tree containing digits from 0-9 only, 
each root-to-leaf path could represent a number.

For example, a root-to-leaf path 1->2->3 which represents the number 123.

Find the total sum of all root-to-leaf numbers.

Note: A leaf is a node with no children.

Example1:
Input: [1,2,3]
      1
     / \
    2   3

Output: 25

Explanation:
The root-to-leaf path 1->2 represents the number 12.
The root-to-leaf path 1->3 represents the number 13.
Therefore, sum = 12 + 13 = 25.


Example 2:
Input: [4,9,0,5,1]
        4
       / \
      9   0
     / \
    5   1

Output: 1026

Explanation:
The root-to-leaf path 4->9->5 represents the number 495.
The root-to-leaf path 4->9->1 represents the number 491.
The root-to-leaf path 4->0 represents the number 40.
Therefore, sum = 495 + 491 + 40 = 1026.
'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys, optparse, os

class Solution:
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """

        if not root:
            return 0

        def add_number(node, current):
            current = current * 10 + node.val

            nonlocal total
            if not node.left and not node.right:
                total += current
            if node.left:
                add_number(node.left, current)
            if node.right:
                add_number(node.right, current)

        total = 0
        add_number(root, 0)
        return total


root = [4,9,0,5,1]

solution = Solution()
result = solution.sumNumbers(root)
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

