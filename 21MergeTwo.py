"""
Merge two sorted linked lists and return it as a new list. The new list should be made by
splicing together the nodes of the first two lists.

Example:
Input: 1->2->4, 1->3->4
Output: 1->1->2->3->4->4
"""
from LinkedList import *
class Solution(object):
    def mergeTwoLists(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        head = tail = ListNode(None)

        while l1 or l2:
            if l1 == None:
                tail.next = l2
                break
            elif l2 == None:
                tail.next = l1
                break
            elif l1.val < l2.val:
                tail.next = l1
                l1 = l1.next
            else:
                tail.next = l2
                l2 = l2.next

            tail = tail.next

        return head.next

    def mergeTwoLists2(self, l1, l2):
        if not l1 or not l2:
            return l1 or l2
        if l1.val < l2.val:
            l1.next = self.mergeTwoLists(l1.next, l2)
            return l1
        else:
            l2.next = self.mergeTwoLists(l1, l2.next)
            return l2


l1 = createLinkedList([1,2,4])
l2 = createLinkedList([1,3,4])
printNode(Solution().mergeTwoLists2(l1, l2))