'''
Given preorder and inorder traversal of a tree, construct the binary tree.

Note:
You may assume that duplicates do not exist in the tree.

Example:
input: 
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

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
    def buildTree(self, preorder, inorder):
        """
        :type preorder: List[int]
        :type inorder: List[int]
        :rtype: TreeNode
        """

        """
        Traversal of a tree:
            Preorder (Root, Left, Right)
            Inorder (Left, Root, Right)
            Postorder (Left, Right, Root)

        In the preorder list, 
        the first value represents root, 
        then folllowing by all left substree values and all right substree values.

        Thus, we don't need to slice the preorder list, 
        when we are done with the left subtree, 
        the left half of the preorder list should already be empty.

        So we can split the inorder list with root value to get
        left substree values and right substree values,
        and recursively build each left and right subtree.

        """

        if not preorder or not inorder:
            return None

        root_val = preorder.pop(0)
        root = TreeNode(root_val)

        root_index = inorder.index(root_val)

        root.left = self.buildTree(preorder, inorder[:root_index])
        root.right = self.buildTree(preorder, inorder[root_index+1:])

        return root


        
preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]

solution = Solution()
result = solution.buildTree(preorder, inorder)
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

