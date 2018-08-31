'''
Given a linked list, rotate the list to the right by k places, where k is non-negative.

Example 1:

Input: 1->2->3->4->5->NULL, k = 2
Output: 4->5->1->2->3->NULL
Explanation: 
    rotate 1 steps to the right: 5->1->2->3->4->NULL
    rotate 2 steps to the right: 4->5->1->2->3->NULL

Example 2:

Input: 0->1->2->NULL, k = 4
Output: 2->0->1->NULL
Explanation:
rotate 1 steps to the right: 2->0->1->NULL
rotate 2 steps to the right: 1->2->0->NULL
rotate 3 steps to the right: 0->1->2->NULL
rotate 4 steps to the right: 2->0->1->NULL

'''

import sys, optparse, os

class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """

        '''
        First, count the length of list while going through the list to find the end of it.
        rotate_times = mod(k, length) saves the unnecessary moves,
        because rotate a list with length = n by x*n times doesn't change the list at all.

        If there are k places to rotate in list 
        [old_head, 2, 3,..., new_tail, new_tail+1,..., old_tail], where old_tail = new_tail + k,

        then new_tail + 1 becomes new_head, and linked list after rotate become
        [new_head,..., old_tail, old_head, 2, 3,..., new_tail]

        '''

        if not head or head.next == None or k == 0:
            return head

        dummy = ListNode(0)
        dummy.next = head
        old_tail = dummy

        length = 0
        while old_tail.next != None:
            length += 1
            old_tail = old_tail.next

        rotate_times = k % length
        if rotate_times == 0:
            return head

        new_tail = dummy
        for _ in range(length - rotate_times):
            new_tail = new_tail.next

        new_head = new_tail.next

        dummy.next = new_head
        old_tail.next = head
        new_tail.next = None

        return dummy.next



head = 1->2->3->4->5->NULL
k = 2

solution = Solution()
result = solution.rotateRight(head, k)
print result


'''
Complexity Analysis
Time complexity : O(n).
    We are doing two passes through the linked list,
    one for the length of linked list, and one for rotate.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''

