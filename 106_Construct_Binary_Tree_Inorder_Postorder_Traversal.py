'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Example:
input: 
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

output:
    3
   / \
  9  20
    /  \
   15   7
'''

import sys, optparse, os

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def buildTree(self, inorder, postorder):
        """
        :type inorder: List[int]
        :type postorder: List[int]
        :rtype: TreeNode
        """

        """
        Traversal of a tree:
            Preorder (Root, Left, Right)
            Inorder (Left, Root, Right)
            Postorder (Left, Right, Root)

        The postorder list consiste of all right substree values, all left substree values, 
        and the root value which is the last element in the postorder list.

        Thus, when we are done with the right subtree, 
        the right half of the postorder list should already be empty.

        So we can split the inorder list with root value to get
        left substree values and right substree values,
        and recursively build each left and right subtree.

        """

        if not inorder or not postorder:
            return None

        root_val = postorder.pop()
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        root.right = self.buildTree(inorder[root_index+1:], postorder)
        root.left = self.buildTree(inorder[:root_index], postorder)

        return root

  
inorder = [9,3,15,20,7]
postorder = [9,15,7,20,3]

solution = Solution()
result = solution.buildTree(inorder, postorder)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We traverse the entire tree to construct it, the total run time is O(n), 
    where n is the total number of nodes in the tree.

Space complexity : O(logN).
    The number of calls is bound by the height of the tree.
    But in the worst case, the tree is linear, i.e. each node has only one child.
    Therefore, the height of tree is in O(n), 
    space complexity due to recursive calls on the stack is O(n) in the worst case.

'''        

