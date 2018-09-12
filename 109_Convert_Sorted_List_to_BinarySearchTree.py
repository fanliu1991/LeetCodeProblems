'''
Given an singly linked list where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, 
a height-balanced binary tree is defined as a binary tree 
in which the depth of the two subtrees of every node never differ by more than 1.

Example:
input: sorted array [-10,-3,0,5,9],

output: One possible answer is: [0,-3,9,-10,null,5], 
which represents the following height balanced BST:
      0
     / \
   -3   9
   /   /
 -10  5

'''

import sys, optparse, os

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    def sortedListToBST(self, head):
        """
        :type head: ListNode
        :rtype: TreeNode
        """

        if not head:
            return None

        """
        For odd case, [-10,-3,0,5,9], 
        head = -10, tail = None => slow = 0, fast = 9
        left = subtree(-10, 0), root = 0, right = subtree(5, None)

        For even case, [-10,-3,0,5,9,10], 
        head = -10, tail = None => slow = 5, fast = None
        left = subtree(-10, 5), root = 5, right = subtree(9, None)
        """

        # recursive solution
        def subtree(head, tail):
            if head == tail:
                return None

            slow, fast = head, head
            while fast != tail and fast.next != tail:
                slow = slow.next
                fast = fast.next.next

            root = TreeNode(slow.val)
            root.left = subtree(head, slow)
            root.right = subtree(slow.next, tail)

            return root

        root = subtree(head, None)

        # inorder traversal
        # inorder traversal generates a sorted list
        """
        length = 0
        current = head

        while current != None:
            length += 1
            current = current.next

        # low and high are used to control the number of times that
        # inorder traversal performed in subtree
        def inorder_subtree(low, high):
            if low > high:
                return None

            middle = (low + high) // 2
            left_subtree = inorder_subtree(low, middle - 1)
            root = TreeNode(self.current_root.val)
            self.current_root = self.current_root.next
            root.left = left_subtree
            root.right = inorder_subtree(middle + 1, high)

            return root

        self.current_root = head
        root = inorder_subtree(1, length)
        """

        return root


head = [-10,-3,0,5,9]

solution = Solution()
result = solution.sortedListToBST(head)
print result


'''
Complexity Analysis
Time complexity :
    Recursive solution: O(N*logN).
    At every level, recursive algorithm is traversing the full list (in parts), 
    and there are log(n) levels in balanced tree

    Inorder traversal: O(n).
    We traverse the entire input linked list, the total run time is O(n), 
    where n is the total number of elements in the linked list.

Space complexity : O(logN).
    The number of calls is bound by the height of the tree.

'''

