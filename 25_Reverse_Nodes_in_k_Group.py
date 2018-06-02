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

        if not head or not head.next or k<2:
            return head
        
        dummy = ListNode(0)
        dummy.next = head
        prev = dummy
        
        '''
        k = 3
        dummy(prev, tail) -> 1 -> 2 -> 3 -> 4 -> 5 -> 6 -> 7
        dummy(prev) -> 1(start, head) -> 2 -> 3(tail) -> 4 -> 5 -> 6 -> 7
        dummy(prev) -> 2(head) -> 3(tail) -> 1(start) -> 4 -> 5 -> 6 -> 7
        dummy(prev) -> 3(tail, head) -> 2 -> 1(start) -> 4 -> 5 -> 6 -> 7
        
        dummy -> 3 -> 2 -> 1(prev, tail) -> 4 -> 5 -> 6 -> 7
        dummy -> 3 -> 2 -> 1(prev) -> 4(start, head) -> 5 -> 6(tail) -> 7
        dummy -> 3 -> 2 -> 1(prev) -> 5(head) -> 6(tail) -> 4(start) -> 7
        dummy -> 3 -> 2 -> 1(prev) -> 6(tail,head) -> 5 -> 4(start) -> 7
        
        dummy -> 3 -> 2 -> 1 -> 6 -> 5 -> 4(prev, tail) -> 7
        '''
        
        while True:
            count = 0
            tail = prev
            while tail.next and count < k: # check if next k ListNode are valid or not
                tail = tail.next
                count += 1
            if count == k:
                start = head = prev.next
                for _ in range(k-1):
                    prev.next= head.next
                    head.next = tail.next
                    tail.next = head

                    head = prev.next
                prev = start
            else:
                return dummy.next


head = 1->2->3->4->5->6

solution = Solution()
result = solution.reverseKGroup(head, 4)
print result
