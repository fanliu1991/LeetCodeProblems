'''
Given a sorted linked list,
all duplicates such that each element appear only once.

Example 1:

Input: 1->1->2
Output: 1->2

Example 2:

Input: 1->1->2->3->3
Output: 1->2->3


'''

import sys, optparse, os

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        dummy = ListNode(0)
        dummy.next = head

        current = head

        while current.next != None:
            if current.val == current.next.val:
                current.next = current.next.next
            else:
                current = current.next

        return dummy.next


head = 1->1->2->3->3

solution = Solution()
result = solution.deleteDuplicates(head)
print result

'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the linked list

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.

'''
