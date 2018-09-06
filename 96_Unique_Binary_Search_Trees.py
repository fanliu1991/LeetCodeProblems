'''
Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example 1:
Input: 3
Output: 5

Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3

'''

import sys, optparse, os

class Solution:
    def numTrees(self, n):
        """
        :type n: int
        :rtype: int
        """

        """
        Given a sequence 1 ... n, to construct a Binary Search Tree (BST) out of the sequence,
        we could enumerate each number i in the sequence, and use the number as the root.
        Naturally, the subsequence 1 ... (i-1) on its left side would lay on the left branch of the root,
        and the right subsequence (i+1) ... n lay on the right branch of the root.

        We then can construct the subtree from the subsequence recursively.
        Through the above approach, we could ensure that the BST that we construct are all unique,
        since they have unique roots.

        G(n): the number of unique BST for a sequence of length n.
        F(i, n), 1 <= i <= n: the number of unique BST, where the number i is the root of BST, and the sequence ranges from 1 to n.
        Thus, G(n) is the actual function we need to calculate, and it can be derived from F(i, n).

        Given the above definitions, the total number of unique BST G(n) is the sum of BST F(i) using each number i as a root.
        i.e. G(n) = F(1, n) + F(2, n) + ... + F(n, n). 
        The bottom cases is a BST constructed out of a sequence of length 1 (only a root) and 0 (empty tree).
        i.e. G(0)=1, G(1)=1.

        Given a sequence 1 ... n, we pick a number i out of the sequence as the root,
        then the number of unique BST is the cartesian product of the number of BST for its left and right subtrees.
        e.g.
        To construct an unique BST out of the entire sequence [1, 2, 3, 4, 5, 6, 7] with 3 as the root,
        we need to construct an unique BST out of its left subsequence [1, 2] and another BST out of the right subsequence [4, 5, 6, 7],
        and then combine them together by cartesian product, F(3,7) = G(2) * G(4).

        In general, F(i, n) = G(i-1) * G(n-i)   1 <= i <= n
        the recursive formula for G(n) = G(0) * G(n-1) + G(1) * G(n-2) + ... + G(n-1) * G(0) 

        """

        G = [0 for _ in range(n+1)]

        G[0] = 1
        G[1] = 1

        for k in range(2, n+1):
            for i in range(1, k+1):
                G[k] += G[i-1] * G[k-i]

        return G[n]


n = 5

solution = Solution()
result = solution.numTrees(n)
print result


'''
Complexity Analysis
Time complexity : O(n^2).
    We need to calculate G[k] for each k from 1 to n to get G[n],
    and for each k, we calculate F(j, k) for each i from 1 to k.

Space complexity : O(n).
    Extra space is used to store G[k].
'''

