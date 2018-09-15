'''
Given a binary tree where each node has a next pointer.
Populate each next pointer to point to its next right node.
If there is no next right node, the next pointer should be set to NULL.

Initially, all next pointers are set to NULL.

Note:
1. You may only use constant extra space.
2. Recursive approach is fine, implicit stack space does not count as extra space for this problem.
3. You may assume that it is a perfect binary tree
(ie, all leaves are at the same level, and every parent has two children).

Example:

Input: Given the following perfect binary tree,
     1
   /  \
  2    3
 / \  / \
4  5  6  7

Output:
     1 -> NULL
   /  \
  2 -> 3 -> NULL
 / \  / \
4->5->6->7 -> NULL

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

        # Recursive solution
        if root.left != None and root.right != None:
            root.left.next = root.right

        if root.right != None and root.next != None:
            root.right.next = root.next.left

        self.connect(root.left)
        self.connect(root.right)

        # Iterative solution
        '''
        level_start = root

        while(level_start != None):
            current_node = level_start

            while (current_node != None):
                if current_node.left != None and current_node.right != None:
                    current_node.left.next = current_node.right

                if current_node.right != None and current_node.next != None:
                    current_node.right.next = current_node.next.left

                current_node = current_node.next

            level_start = level_start.left
        '''



root = {-1,0,1,2,3,4,5,6,7,8,9,10,11,12,13}

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
