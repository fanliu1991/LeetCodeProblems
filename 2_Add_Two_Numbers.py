'''
You are given two non-empty linked lists representing two non-negative integers. The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Example:

Input: (2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 0 -> 8
Explanation: 342 + 465 = 807.

'''
import sys, optparse, os

class Solution:
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """

    '''
    Algorithm

    Just like how you would sum two numbers on a piece of paper, we begin by summing the least-significant digits, which is the head of l1 and l2. Since each digit is in the range of 0…9, summing two digits may "overflow". For example 5+7=12. In this case, we set the current digit to 2 and bring over the carry=1 to the next iteration. carry must be either 0 or 1 because the largest possible sum of two digits (including the carry) is 9+9+1=19.

    The pseudocode is as following:

        --- Initialize current node to dummy head of the returning list.
        --- Initialize carry to 000.
        --- Initialize ppp and qqq to head of l1l1l1 and l2l2l2 respectively.
        --- Loop through lists l1l1l1 and l2l2l2 until you reach both ends.
            * Set xxx to node ppp's value. If ppp has reached the end of l1l1l1, set to 000.
            * Set yyy to node qqq's value. If qqq has reached the end of l2l2l2, set to 000.
            * Set sum=x+y+carrysum = x + y + carrysum=x+y+carry.
            * Update carry=sum/10carry = sum / 10carry=sum/10.
            * Create a new node with the digit value of (summod10)(sum \bmod 10)(summod10) and set it to current node's next, then advance current node to next.
            * Advance both ppp and qqq.
        --- Check if carry=1carry = 1carry=1, if so append a new node with digit 111 to the returning list.
        --- Return dummy head's next node.

    Note that we use a dummy head to simplify the code. Without a dummy head, you would have to write extra conditional statements to initialize the head's value.

    Take extra caution of the following cases:
    // l1=[0,1],
       l2=[0,1,2]
       When one list is longer than the other.

    //l1=[]
      l2=[0,1]
      When one list is null, which means an empty list.

    //l1=[9,9]
      l2=[1]
      The sum could have an extra carry of one at the end, which is easy to forget.

    '''


        carry = 0
        root = n = ListNode(0) # means first root = ListNode(0) then n point to the same address, which means point to root
        while l1 or l2 or carry:
            v1, v2 = 0, 0
            if l1:
                v1 = l1.val
                l1 = l1.next
            if l2:
                v2 = l2.val
                l2 = l2.next
            carry, node_val = divmod(v1 + v2 + carry, 10)
            n.next = ListNode(node_val)
            n = n.next

        # ****** Without using v1 and v2 ******
        # while l1 or l2 or carry:
        #     if l1:
        #         carry += l1.val
        #         l1 = l1.next
        #     if l2:
        #         carry += l2.val
        #         l2 = l2.next
        #     carry, val = divmod(carry, 10)
        #     n.next = n = ListNode(val)
        return root.next


l1 = LinkedList([2, 4, 3])
l2 = LinkedList([5, 6, 4])

solution = Solution()
result = solution.addTwoNumbers(nums, target)
print result

        '''
        Complexity Analysis
        Time complexity : O(max(m,n)).
            Assume that m and n represents the length of l1 and l2 respectively, the algorithm above iterates at most max(m,n) times.

        Space complexity : O(max(m,n)).
            The length of the new list is at most max(m,n)+1.
        '''