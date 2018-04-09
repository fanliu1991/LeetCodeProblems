'''
Merge two sorted linked lists and return it as a new list.
The new list should be made by splicing together the nodes of the first two lists.

Example:

Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4

'''
import sys, optparse, os

class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

        '''
            First, we set up a false "head" node that allows us to easily return the head of the merged list later. 
        We also maintain a current pointer, which points to the current node for which we are considering adjusting its next pointer.
        Then, we do the following until at least one of l1 and l2 points to null: if the value at l1 is less than or equal to the value at l2, then we connect l1 to the previous node and increment l1.
        Otherwise, we do the same, but for l2. 
        Then, regardless of which list we connected, we increment current to keep it one step behind one of our list heads.

            After the loop terminates, at most one of l1 and l2 is non-null.
        Therefore (because the input lists were in sorted order), if either list is non-null, it contains only elements greater than all of the previously-merged elements.
        This means that we can simply connect the non-null list to the merged list and return it.
        '''

        if l1 is None:
            return l2
        elif l2 is None:
            return l1

        head = ListNode(0)
        current = head

        while l1 and l2:
            if l1.val <= l2.val:
                current.next = l1
                l1 = l1.next
            else:
                current.next = l2
                l2 = l2.next
            current = current.next

        # exactly one of l1 and l2 can be non-null at this point,
        # so connect the non-null list to the end of the merged list.
        if l1 is None:
            current.next = l2
        else:
            current.next = l1

        return head.next

l1 = 1->2->3->4->5
l2 = 1->3->4

solution = Solution()
result = solution.mergeTwoLists(l1, l2)
print result

'''
Complexity Analysis
Time complexity : O(n+m).
    Because exactly one of l1 and l2 is incremented on each loop iteration,
    the while loop runs for a number of iterations equal to the sum of the lengths of the two lists.
    All other work is constant, so the overall complexity is linear.

Space complexity : O(1).
    The iterative approach only allocates a few pointers, so it has a constant overall memory footprint.
'''