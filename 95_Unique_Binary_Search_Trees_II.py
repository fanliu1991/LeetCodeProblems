'''
Given an integer n, 
generate all structurally unique BST's (binary search trees) that store values 1 ... n.

Example:

Input: 3
Output:
[
  [1,null,3,2],
  [3,2,null,1],
  [3,1,null,null,2],
  [2,1,3],
  [1,null,2,null,3]
]
Explanation:
The above output corresponds to the 5 unique BST's shown below:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

import sys, optparse, os

class Solution:
    def generateTrees(self, n):
        """
        :type n: int
        :rtype: List[TreeNode]
        """

        """
        This problem is a variant of the problem of 95. Unique Binary Search Trees.
        """

        if n == 0:
            return []

        def generate_subtree(start, end):
            if start > end:
                return [None]

            # this result contains a list of root TreeNode
            result = []
            for i in range(start, end+1):
                left_subtree = generate_subtree(start, i-1)
                right_subtree = generate_subtree(i+1, end)
                for l in left_subtree:
                    for r in right_subtree:
                        node = TreeNode(i)
                        node.left, node.right  = l, r
                        result.append(node)
            return result

        return generate_subtree(1, n)


n = 5

solution = Solution()
result = solution.generateTrees(n)
print result


'''
Complexity Analysis
Time complexity : O(n^2).

Space complexity : O(n).

'''

