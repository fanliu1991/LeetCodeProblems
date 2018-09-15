'''
Given a binary tree where each node has a next pointer.
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

The given binary tree may be not perfect, 
ie, not all leaves are at the same level, and not every parent has two children

Initially, all next pointers are set to NULL.

Note:
1. You may only use constant extra space.
2. Recursive approach is fine, implicit stack space does not count as extra space for this problem.

Example:

Input: Given the following perfect binary tree,
     1
   /  \
  2    3
 / \    \
4   5    7

Output:
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \    \
4-> 5 -> 7 -> NULL

'''

import sys, optparse, os

# Definition for binary tree with next pointer.
# class TreeLinkNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
#         self.next = None

class Solution:(object)
    def connect(self, root):
        """
        :type s: TreeLinkNode
        :rtype: void. Do not return anything, modify root in-place instead.
        """

        if not root:
            return

        # Iterative solution
        # The algorithm is a BFS or level order traversal.

        level_start = root

        while(level_start != None):
            current_node = level_start
            level_start = None
            prev = None

            while (current_node != None):
                if current_node.left != None:
                    if prev == None:
                        level_start = current_node.left
                    else:
                        prev.next = current_node.left
                    prev = current_node.left

                if current_node.right != None:
                    if prev == None:
                        level_start = current_node.right
                    else:
                        prev.next = current_node.right
                    prev = current_node.right

                current_node = current_node.next



root = {1,2,2,3,3,3,3,4,4,4,4,4,4,null,null,5,5}

solution = Solution()
result = solution.connect(root)
print result

'''
Complexity Analysis
Time complexity: O(n)
    We traverse the entire input tree once, the total run time is O(n), 
    where n is the total number of nodes in the tree.

Space complexity: O(1)
    Input tree is modified in-place.

'''
