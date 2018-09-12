'''
Given a binary tree, return the bottom-up level order traversal of its nodes' values. 
(ie, from left to right, level by level from leaf to root).

Example:
input: binary tree [3,9,20,null,null,15,7],
    3
   / \
  9  20
    /  \
   15   7

output: its bottom-up level order traversal as:
[
  [15,7],
  [9,20],
  [3]
]

'''

import sys, optparse, os

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def levelOrderBottom(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[int]]
        """

        if root == None:
            return []

        result = []

        current_level_nodes = [root]

        while current_level_nodes:
            current_level_values = []
            next_level_nodes = []
            for node in current_level_nodes:
                current_level_values.append(node.val)
                if node.left != None:
                    next_level_nodes.append(node.left)
                if node.right != None:
                    next_level_nodes.append(node.right)

            result.insert(0, current_level_values)
            current_level_nodes = next_level_nodes

        # DFS recursively
        """
        def  dfs(root, level):
            if not root:
                return
            else:
                nonlocal result
                if len(result) <= level:
                    result.insert(0, [])
                result[-(level+1)].append(root.val)
                dfs(root.left, level+1)
                dfs(root.right, level+1)

        dfs(root, 0)
        """

        return result


root = [3,9,20,null,null,15,7]

solution = Solution()
result = solution.levelOrderBottom(root)
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

