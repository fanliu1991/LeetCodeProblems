'''
Given a binary tree and a sum, 
find all root-to-leaf paths where each path's sum equals the given sum.

Note: A leaf is a node with no children.

Example:
Input: Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1

Output: 
[
   [5,4,11,2],
   [5,8,4,5]
]

'''

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

import sys, optparse, os

class Solution:
    def pathSum(self, root, sum):
        """
        :type root: TreeNode
        :type sum: int
        :rtype: List[List[int]]
        """

        if not root:
            return []

        result = []

        def dfs(node, target, current_path):
            if not node:
                return

            if node.val == target and node.left == None and node.right == None :
                nonlocal result
                result.append(current_path + [node.val])
                return
            else:
                left_subtree = dfs(node.left, target - node.val, current_path + [node.val])
                right_subtree = dfs(node.right, target - node.val, current_path + [node.val])
                return

        dfs(root, sum, [])
        return result


root = [3,9,20,null,18,15,7]
sum = 30

solution = Solution()
result = solution.pathSum(root, sum)
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

