'''
Reverse a linked list from position m to n. Do it in one-pass.

Note: 1 <= m <= n <= length of list.

Example:

Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL

'''


import sys, optparse, os

class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """

        if head == None or m >= n:
            return head

        dummy = ListNode(0)
        dummy.next = head
        temp = dummy

        for i in range(m-1):
            temp = temp.next

        unchanged_end = temp
        reverse_head = temp.next

        prev = reverse_head
        current = reverse_head.next
        next = reverse_head.next.next

        for i in range(n-m-1):
            current.next = prev
            prev = current
            current = next
            next = current.next

        current.next = prev

        unchanged_end.next = current
        reverse_head.next = next

        return dummy.next

        """
        position = 0

        while temp != None:
            if position + 1 == m:
                temp_end = temp
                reverse_end = temp.next
            elif position == n:
                temp_head = temp.next
                reverse_head = temp

            if position == m:
                prev = temp
                temp = temp.next
                position += 1
            elif position == n:
                temp.next = prev
                break
            elif m < position < n:
                next = temp.next
                temp.next = prev
                prev = temp
                temp = next
                position += 1
            else:
                temp = temp.next
                position += 1

        temp_end.next = reverse_head
        reverse_end.next = temp_head

        return dummy.next
        """


head = 1->2->3->4->5->6->NULL
m = 2
n = 5

solution = Solution()
result = solution.reverseBetween(head, m, n)
print result

'''
Complexity Analysis
Time complexity : O(n).
    We are doing one pass through the linked list.

Space complexity : O(1).
    No extra space is used. Only extra variables are needed.
'''

