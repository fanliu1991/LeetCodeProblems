'''
Given a sorted linked list,
delete all nodes that have duplicate numbers,
leaving only distinct numbers from the original list.


Example 1:

Input: 1->2->3->3->4->4->5
Output: 1->2->5

Example 2:

Input: 1->1->1->2->3
Output: 2->3


'''

import sys, optparse, os

class Solution(object):
    def deleteDuplicates(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        if not head or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        slow, fast = dummy, head

        while fast != None and fast.next != None:
            fast = fast.next
            if fast.val != slow.next.val:
                slow = slow.next
            else:
                while fast != None and fast.val == slow.next.val:
                    fast = fast.next
                slow.next = fast

        return dummy.next


# head = 1->2->3->3->4->4->5
head = 1->1

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
