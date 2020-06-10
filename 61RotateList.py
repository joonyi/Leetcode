"""
Given a linked list, rotate the list to the right by k places, where k is non-negative.
"""
from linkedlist import *
class Solution(object):
    def rotateRight(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        if not head or k == 0:
            return head

        p = q = head
        cnt = 0
        while p != None: # Find the length
            p = p.next
            cnt += 1

        pos = cnt - (k % cnt)
        if k % cnt == 0 or cnt == 1:
            return head

        prev = None
        cnt = 0
        while cnt < pos:
            prev = head
            head = head.next
            cnt += 1

        prev.next = None
        tail = head
        while tail != None:
            prev = tail
            tail = tail.next

        prev.next = q
        return head

    def rotateRight2(self, head, k):
        if not head or k == 0:
            return head
        p = head
        cnt = 1
        while p.next != None:
            p = p.next
            cnt += 1
        p.next = head # cycle back to 1, ex. 1->2->3->1..., so that can traverse back
        k %= cnt
        for i in range(cnt-k):
            p = p.next
        head = p.next
        p.next = None
        return head

A, k = [1,2,3,4,5], 2
# A, k = [0,1,2], 4
# A, k = [1,2], 1
# A, k = [1], 1
head = createLinkedList(A)
printNode(Solution().rotateRight2(head, k))
