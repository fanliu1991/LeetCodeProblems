'''
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

You may not alter the values in the nodes, only nodes itself may be changed.

Only constant memory is allowed.

For example,
Given this linked list: 1->2->3->4->5

For k = 2, you should return: 2->1->4->3->5

For k = 3, you should return: 3->2->1->4->5

'''
import sys, optparse, os

class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        if head == null or head.next == null or k<2:
            return head

        dummy = ListNode(0)
        temp = ListNode(0)

        dummy.next = head
        tail = prev = dummy

        count = 0
        while tail != null and count < k:
            tail = tail.next
            count +=1
        if tail == null:
            break

        while prev.next != tail:
            temp = prev.next
            prev.next = temp.next

            temp.next = tail.next
            tail.next = temp

        return prev.next


head = 1->2->3->4->5->6

solution = Solution()
result = solution.reverseKGroup(head, 4)
print result
