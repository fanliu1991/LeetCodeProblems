'''
Given a binary tree, check whether it is a mirror of itself (ie, symmetric around its center).

Example 1:
input: binary tree [1,2,2,3,4,4,3]
output: True

    1
   / \
  2   2
 / \ / \
3  4 4  3

Example 2:
input: binary tree [1,2,2,null,3,null,3]
output: False

    1
   / \
  2   2
   \   \
   3    3
'''

import sys, optparse, os

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        # recursive solution
        def isMirror(left_subtree, right_subtree):
            if left_subtree == None and right_subtree == None:
                return True
            elif left_subtree == None or right_subtree == None:
                return False

            if left_subtree.val != right_subtree.val:
                return False
            else:
                ans = isMirror(left_subtree.left, right_subtree.right) and \
                isMirror(left_subtree.right, right_subtree.left)

                return ans

        if root == None:
            return True
        else:
            res = isMirror(root.left, root.right)

        return res

        # iterative solution
        '''
        stack = []

        if root == None:
            return True

        stack.append((root.left, root.right))

        while stack:
            subtrees = stack.pop()
            left_subtree = subtrees[0]
            right_subtree = subtrees[1]

            if left_subtree == None and right_subtree == None:
                continue
            elif left_subtree == None or right_subtree == None:
                return False

            if left_subtree.val != right_subtree.val:
                return False
            else:
                stack.append((left_subtree.left, right_subtree.right))
                stack.append((left_subtree.right, right_subtree.left))

        return True
        '''


root = [1,2,2,3,4,4,3]

solution = Solution()
result = solution.isSymmetric(root)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We traverse the entire input tree once, the total run time is O(n), 
    where n is the total number of nodes in the tree.

Space complexity : 
    recursive method: O(logN).
        The number of recursive calls is bound by the height of the tree.
        But in the worst case, the tree is linear, i.e. each node has only one child.
        Therefore, the height of tree is in O(n), 
        space complexity due to recursive calls on the stack is O(n) in the worst case.

    iterative method: O(n).
        There is additional space required for the search queue.
        In the worst case, we have to insert O(n) nodes in the queue.
        Therefore, space complexity is O(n).

'''

