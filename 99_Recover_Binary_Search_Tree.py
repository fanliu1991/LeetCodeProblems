'''
Two elements of a binary search tree (BST) are swapped by mistake.
Recover the tree without changing its structure.

Example 1:

Input: [1,3,null,null,2]

   1
  /
 3
  \
   2

Output: [3,1,null,null,2]

   3
  /
 1
  \
   2

Example 2:

Input: [3,1,4,null,null,2]

  3
 / \
1   4
   /
  2

Output: [2,1,4,null,null,3]

  2
 / \
1   4
   /
  3

'''

import sys, optparse, os

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def recoverTree(self, root):
        """
        :type root: TreeNode
        :rtype: void Do not return anything, modify root in-place instead.
        """

        """
        Inorder traversal:
            result = []
            inorder_traversal(root):
                if (root == null)
                    return
                traverse(root.left)
                result.append(root.val)
                traverse(root.right)

        In case of a binary serach tree (BST),
        inorder traversal generates result list with sorted values.
        If two elements in BST are swapped,
        then by comparing each element with its previous one,
        we can find two previous elements that have larger values then current elements,
        thus, the first element and the next element of the second element are at wrong position.
        e.g.
        we have the following tree that is printed as in order traversal:
            6, 3, 4, 5, 2
        we can find out that 6 is the first element to swap because 6 > 3,
        and 2 is the second element to swap because 2 < 5.

        Therefore, the algorithm is comparing the current node and its previous node in the "in order traversal".
        """

        first_element = None
        second_element = None

        prev_element = TreeNode(float('-inf'))

        # def travel_tree(root):
        #     if root == None:
        #         return

        #     travel_tree(root.left)

        #     nonlocal first_element, second_element, prev_element

        #     # for example, a tree that is printed as in order traversal is as following.:
        #     # 1,2,3,4,5,6,7
        #     # swap two nodes to make them at wrong position:
        #     # 1,2,6,4,5,3,7

        #     # the first element at worng position is 
        #     # the previous element that larger than current root
        #     if first_element == None and prev_element.val > root.val:
        #         first_element = prev_element

        #     # the second element at worng position is 
        #     # the current root that less than previous element
        #     if first_element != None and root.val < prev_element.val:
        #         second_element = root

        #     prev_element = root

        #     travel_tree(root.right)

        # travel_tree(root)

        def Morris_Traversal(root):
            # Morris Traversal to travel through BST:
            # http://www.cnblogs.com/AnnieKim/archive/2013/06/15/morristraversal.html
            nonlocal first_element, second_element, prev_element

            current_node = root
            predecessor_node = None
            while(current_node != None):
                if current_node.left == None:
                    if first_element == None and prev_element.val > current_node.val:
                        first_element = prev_element
                    if first_element != None and current_node.val < prev_element.val:
                        second_element = current_node
                    prev_element = current_node

                    current_node = current_node.right
                else:
                    # predecessor node is the most right node in the current node left subtree
                    predecessor_node = current_node.left
                    while predecessor_node.right != None and predecessor_node.right != current_node:
                        predecessor_node = predecessor_node.right

                    if predecessor_node.right == None:
                        predecessor_node.right = current_node
                        current_node = current_node.left
                    else:
                        if first_element == None and prev_element.val > current_node.val:
                            first_element = prev_element
                        if first_element != None and current_node.val < prev_element.val:
                            second_element = current_node
                        prev_element = current_node

                        predecessor_node.right = None
                        current_node = current_node.right

        Morris_Traversal(root)

        first_element.val, second_element.val = second_element.val, first_element.val


root = [1,3,None,None,2]

solution = Solution()
result = solution.recoverTree(root)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We need to travel all nodes in the BST.

Space complexity :
    O(logN) with inorder traversal:
        We need to store the situation of each level when recursively travel logN levels.
    O(1) with Morris Traversal:
        Morris Traversal uses child node left and right to point to parent node.
'''

