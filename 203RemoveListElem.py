"""
Remove all elements from a linked list of integers that have value val.
"""
from linkedlist import *
class Solution(object):
    def removeElements(self, head, val):
        """
        :type head: ListNode
        :type val: int
        :rtype: ListNode
        """
        if head == None:
            return None

        while head.val == val:
            head = head.next
            if head == None:
                return None

        y = head
        x = head.next
        while y:
            if y.val == val:
                x.next = y.next
            else:
                x = y
            y = y.next
        return head

A = [1, 2, 6, 3, 4, 5, 6,6]
head = createLinkedList(A)
printNode(head)
head = Solution().removeElements(head, 6)
printNode(head)