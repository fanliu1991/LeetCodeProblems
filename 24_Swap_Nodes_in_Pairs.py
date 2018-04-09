'''
Given a linked list, swap every two adjacent nodes and return its head.

For example,
Given 1->2->3->4, return the list as 2->1->4->3.

Your algorithm should use only constant space. You may not modify the values in the list, only nodes itself can be changed. 
'''
import sys, optparse, os

class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """

        '''
        Merge with Divide And Conquer:
        1.Pair up k lists and merge each pair.
        2.After the first pairing, k\text{k}k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
        3.Repeat this procedure until we get the final sorted linked list.

        Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about log_{2}{k} times.

        '''

        if head == None or head.next == None:
            return head

        dummy = ListNode(0)
        dummy.next = head

        prev_node = dummy
        current_node = head
        next_node = head.next

        while next_node != None:
            prev_node.next = next_node
            current_node.next = next_node.next
            next_node.next = current_node

            prev_node = current_node
            current_node = current_node.next

            if current_node == None:
                break
            else:
                next_node = current_node.next

        return dummy.next


head = 1->2->3->4

solution = Solution()
result = solution.swapPairs(head)
print result

'''
Complexity Analysis
Time complexity : O(n)

Space complexity : O(n).
'''