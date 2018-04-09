'''
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.

'''
import sys, optparse, os

class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """

        '''
        Merge with Divide And Conquer:
        1.Pair up k lists and merge each pair.
        2.After the first pairing, k\text{k}k lists are merged into k/2 lists with average 2N/k length, then k/4, k/8 and so on.
        3.Repeat this procedure until we get the final sorted linked list.

        Thus, we'll traverse almost N nodes per pairing and merging, and repeat this procedure about log_{2}{k} times.

        '''

        # Because Python has no linked list structure, list of lists is used for experiment
        lists_len = len(lists)
        print lists_len

        if lists_len <=1:
            return lists[0]
        elif lists_len == 2:
            ans = []
            l1, l2 = lists[0], lists[1]
            i, j = 0, 0
            while i<len(l1) and j<len(l2):
                if l1[i] <= l2[j]:
                    ans.append(l1[i])
                    i+=1
                else:
                    ans.append(l2[j])
                    j+=1

            if i==len(l1):
                ans = ans + l2[j:]
            elif j==len(l2):
                ans = ans + l1[i:]

            return ans
        else:
            left = self.mergeKLists(lists[:lists_len/2])
            print "left", left
            right = self.mergeKLists(lists[lists_len/2:])
            print "right", right

            ans = self.mergeKLists([left, right])
            return ans

    # linked list method:
    '''
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l2.next
            point = point.next
        
        if not l1:
            point.next=l2
        else:
            point.next=l1
        return head.next
    '''


lists = [[1, 3, 5, 7, 9, 11], [0, 2, 4, 6, 8, 10], [-5, -4, -3, -2, -1, 12, 13, 14, 15, 16], [0.5, 1.5, 2.5, 3.5]]

solution = Solution()
result = solution.mergeKLists(lists)
print result

'''
Complexity Analysis
Time complexity : O(n*log_{2}{k}), where k is the number of linked lists.
    We can merge two sorted linked list in O(n) time where n is the total number of nodes in two lists.
    Sum up the merge process and we can get O(n*log_{2}{k})

Space complexity : O(1).
    We can merge two sorted linked lists in O(1) space.
'''