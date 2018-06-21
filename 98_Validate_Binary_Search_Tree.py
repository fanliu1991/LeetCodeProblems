'''
Given a binary tree,
determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.


Example 1:

Input:
      2
     / \
    1   3

Output: true


Example 2:

        5
       / \
      1   4
         / \
        3   6

Output: false

Explanation:
The input is: [5,1,4,null,null,3,6].
The root node's value is 5 but its right child's value is 4.


'''

import sys, optparse, os

class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        '''
        method 1:
            Use recursion.
            Pass down two parameters:
            1. lessThan
                which means that all nodes in the the current subtree must be smaller than this value.
            2. largerThan
                which means that all nodes in the the current subtree must be larger than this value.

            Compare root of the current subtree with these two values.
            Then, recursively check the left and right subtree of the current root.
            Take care of the values passed down.
        '''

        def isValidSubtree(node, less_than, larger_than):
            if node == None:
                return True
            elif node.val >= less_than or node.val <= larger_than:
                return False
            else:
                return isValidSubtree(node.left, node.val, larger_than) and \
                       isValidSubtree(node.right, less_than, node.val)

        if root == None:
            return True

        ans = isValidSubtree(root.left, root.val, float('-inf')) and \
                 isValidSubtree(root.right, float('inf'), root.val)

        return ans


        '''
        method 2:
            Use inorder traversal to travel all nodes and save eacn node's value.
            The nodes' values should be in ascending order
        '''

        # node_value = []

        # def inorder_traversal(node):
        #     if node != None:
        #         inorder_traversal(node.left)
        #         node_value.append(node.val)
        #         inorder_traversal(node.right)

        # inorder_traversal(root)

        # for i in range(1, len(node_value)):
        #     if node_value[i-1] >= node_value[i]:
        #         return False

        # return True


root = [5,1,4,None,None,3,6]

solution = Solution()
result = solution.isValidBST(root)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the tree.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''

