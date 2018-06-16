'''
Given a linked list and a value x, partition it 
such that all nodes less than x come before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:

Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5

'''

import sys, optparse, os

class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """

        if head == None or head.next == None:
            return head

        less_head = less_tail = ListNode(0)
        greater_head = greater_tail = ListNode(0)

        current = head

        while current != None:
            if current.val < x:
                less_tail.next = current
                less_tail = less_tail.next
            else:
                greater_tail.next = current
                greater_tail = greater_tail.next
            current = current.next
        greater_tail.next = None
        less_tail.next = greater_head.next

        return less_head.next


head = 1->4->3->2->5->2
x = 3

solution = Solution()
result = solution.partition(head, x)
print result

'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the linked list

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
