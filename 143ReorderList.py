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
        # TLE
        if not head:
            return head

        tail = head
        cnt = 0
        while tail.next != None:
            cnt += 1
            tail = tail.next

        start = head
        while start.next != tail and start != tail:
            tail.next = start.next
            start.next = tail
            cur = tail.next
            while cur.next != tail:
                cur = cur.next
            start = tail.next
            tail = cur

        tail.next = None

        return head

    def reorderList2(self, head):
        # Failed in python2.7
        # Splits in place a list in two halves, the first half is >= in size than the second.
        # @return A tuple containing the heads of the two halves
        def _splitList(head):
            fast = head
            slow = head
            while fast and fast.next:
                slow = slow.next
                fast = fast.next
                fast = fast.next

            middle = slow.next
            slow.next = None

            return head, middle

        # Reverses in place a list.
        # @return Returns the head of the new reversed list
        def _reverseList(head):

            last = None
            currentNode = head

            while currentNode:
                nextNode = currentNode.next
                currentNode.next = last
                last = currentNode
                currentNode = nextNode

            return last

        # Merges in place two lists
        # @return The newly merged list.
        def _mergeLists(a, b):

            tail = a
            head = a

            a = a.next
            while b:
                tail.next = b
                tail = tail.next
                b = b.next
                if a:
                    a, b = b, a

            return head

        if not head or not head.next:
            return

        a, b = _splitList(head)
        b = _reverseList(b)
        head = _mergeLists(a, b)
        return head

    def reorderList3(self, head):
        if not head:
            return head

        pi = pj = head

        while pj.next and pj.next.next:  # j goes as twice as i.
            pi, pj = pi.next, pj.next.next

        cur = pi.next  # start from 2nd half.
        node = pi.next = None
        while cur:  # reverse 2nd half.
            next = cur.next
            cur.next = node
            node = cur
            cur = next

        cur1, cur2 = head, node
        while cur2:  # insert
            next1, next2 = cur1.next, cur2.next
            cur1.next, cur2.next = cur2, next1
            cur1, cur2 = next1, next2


A = [1,2,3,4]
# A = [1,2,3,4,5]
head = createLinkedList(A)
printNode(Solution().reorderList2(head))