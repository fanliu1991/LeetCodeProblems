'''
Given two binary trees,
write a function to check if they are the same or not.

Two binary trees are considered the same 
if they are structurally identical and the nodes have the same value.

Example 1:

Input:
           1         1
          / \       / \
         2   3     2   3

        [1,2,3],   [1,2,3]

Output: true

Example 2:

Input:
           1         1
          /           \
         2             2

        [1,2],     [1,null,2]

Output: false

Example 3:

Input:
           1         1
          / \       / \
         2   1     1   2

        [1,2,1],   [1,1,2]

Output: false

'''

import sys, optparse, os

class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """

        if p == None and q == None:
            return True
        elif p == None or q == None:
            return False
        else:
            ans = (p.val == q.val) and \
                  self.isSameTree(p.left, q.left) and \
                  self.isSameTree(p.right, q.right)

        return ans

p = [1,2]
q = [1,null,2]

solution = Solution()
result = solution.isSameTree(p, q)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the tree.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''

