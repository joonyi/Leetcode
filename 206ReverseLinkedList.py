"""
Reverse a singly linked list.
"""
from LinkedList import *
class Solution(object):
    def reverseList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        y = None
        while head:
            x = head.next
            head.next = y
            y = head
            head = x
        return y

    def reverseList2(self, head):
        prev = None
        while head:
            front = head.next
            head.next = prev # reverse
            prev = head
            head = front

        return prev

A = [1, 2, 3, 4, 5]
head = createLinkedList(A)
printNode(head)
head = Solution().reverseList(head)
printNode(head)