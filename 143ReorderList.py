"""
Given a singly linked list L: L0→L1→…→Ln-1→Ln,
reorder it to: L0→Ln→L1→Ln-1→L2→Ln-2→…

You may not modify the values in the list's nodes, only nodes itself may be changed.
"""
from linkedlist import *
class Solution(object):
    def reorderList(self, head):
        """
        :type head: ListNode
        :rtype: None Do not return anything, modify head in-place instead.
        """
        p1 = head
        length = 0
        tail = None
        while p1:
            front = p1.next
            p1.next = tail  # reverse
            tail = p1
            p1 = front
            length += 1

        # return tail
        if length <= 2:
            return

        q = tail.next
        p1 = head
        p2 = head.next
        while p2 != q:
            p1.next = tail
            tail.next = p1
            p2 = p1.next
            tail = q
            q = q.next

    def reorderList2(self, head):
        x = head
        nodes = []
        while x:
            nodes.append(x)
            x = x.next

        i, j = 1, len(nodes) - 1
        while i < j:
            nodes[i], nodes[j] = nodes[j], nodes[i]
            i += 1
            j -= 1
        for k in range(len(nodes)-1):
            nodes[k].next = nodes[k+1]
        nodes[len(nodes)-1].next = None
        return head
Not working

A = [1,2,3,4,5]
head = createLinkedList(A)
printNode(head)
root = Solution().reorderList2(head)
printNode(root)