'''
Given a binary tree,
return the inorder traversal of its nodes' values.

Example:

Input: [1,null,2,3]
       1
        \
         2
        /
       3

Output: [1,3,2]

'''

import sys, optparse, os

class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """

        '''
        Depth First Traversals:
        (a) Inorder (Left, Root, Right)
        (b) Preorder (Root, Left, Right)
        (c) Postorder (Left, Right, Root)
        '''

        result, stack = [], []
        while True:
            while root != None:
                stack.append(root)
                root = root.left
            if stack == []:
                return result
            node = stack.pop()
            result.append(node.val)
            root = node.right


root = [1,null,2,3]

solution = Solution()
result = solution.inorderTraversal(root)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the tree.

Space complexity : O(n).
    Eextra space is used to store nodes value.

'''

