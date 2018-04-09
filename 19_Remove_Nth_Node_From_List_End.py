'''
Given a linked list, remove the n-th node from the end of list and return its head.

Example:

Given Given linked list: 1->2->3->4->5, and n = 2.

After removing the second node from the end, the linked list becomes 1->2->3->5.

Note:
Given n will always be valid.
Try to do this in one pass. 

'''
import sys, optparse, os

class Solution(object):
    def removeNthFromEnd(self, head, n):
        """
        :type head: ListNode
        :type n: int
        :rtype: ListNode
        """

        '''
        Two-pass Approach:
            We notice that the problem could be simply reduced to another one : Remove the (L−n+1)th node from the beginning in the list , where L is the list length.
        This problem is easy to solve once we found list length L.

            First we will add an auxiliary "dummy" node, which points to the list head. The "dummy" node is used to simplify some corner cases such as a list with only one node, or removing the head of the list.
        On the first pass, we find the list length L. Then we set a pointer to the dummy node and start to move it through the list till it comes to the (L−n)th node.
        We relink next pointer of the (L−n)th node to the (L−n+2)th node and we are done.
        '''

        '''
        One-pass Approach:
            Instead of one pointer, we could use two pointers.
        The first pointer advances the list by n+1 steps from the beginning, while the second pointer starts from the beginning of the list. Now, both pointers are exactly separated by n nodes apart.
        We maintain this constant gap by advancing both pointers together until the first pointer arrives past the last node.
        The second pointer will be pointing at the nth node counting from the last. We relink the next pointer of the node referenced by the second pointer to point to the node's next next node.

        '''

        dummy = ListNode(0)
        dummy.next = head
        first = dummy
        second = dummy
        gap = 0

        while gap < n+1:
            first = first.next
            gap += 1

        while first != Null:
            first = first.next
            second = second.next

        second.next = second.next.next
        return dummy.next

head = 1->2->3->4->5
n = 2

solution = Solution()
res = solution.removeNthFromEnd(head, n)
print res

'''
Complexity Analysis
Time complexity : O(L).
    The algorithm makes one traversal of the list of L nodes.

Space complexity : O(1).
    We only used constant extra space.
'''