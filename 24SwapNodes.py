"""
Given a linked list, swap every two adjacent nodes and return its head.
You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
from linkedlist import *
class Solution(object):
    def swapPairs(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        prev = ListNode(None)
        prev.next = head
        p = head
        head = head.next
        while p and p.next:
            q = p.next
            prev.next = q
            p.next = q.next
            q.next = p
            prev = p
            p = p.next

        return head

    def swapPairs2(self, head):
        pre, pre.next = self, head
        while pre.next and pre.next.next:
            a = pre.next
            b = a.next
            pre.next, b.next, a.next = b, a, b.next # Excellent, can change them at once
            pre = a
        return self.next

    # Recursively
    def swapPairs3(self, head):
        if head and head.next:
            tmp = head.next
            head.next = self.swapPairs3(tmp.next)
            tmp.next = head
            return tmp
        return head

A = [1,2,3,4]

head = createLinkedList(A)
printNode(Solution().swapPairs3(head))
