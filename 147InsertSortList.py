"""
Insertion sort iterates, consuming one input element each repetition, and growing a sorted output list.
At each iteration, insertion sort removes one element from the input data, finds the location it belongs within the sorted list, and inserts it there.
It repeats until no input elements remain.
"""
from LinkedList import *
class Solution(object):
    def insertionSortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head: return head
        dummy = ListNode(None)
        dummy.next = head
        head = head.next
        dummy.next.next = None
        while head:
            tail = dummy.next
            if head.val <= tail.val: # insert at the front
                tmp = head.next
                dummy.next = head
                head.next = tail
                while tail.next:
                    tail = tail.next
                tail.next = None
                head = tmp
            else:
                while tail and head.val > tail.val:
                    prev = tail
                    tail = tail.next

                if prev.next: # insert at the middle
                    tmp = head.next
                    prev.next = head
                    head.next = tail
                    while tail.next:
                        tail = tail.next
                    tail.next = None
                    head = tmp
                else: # insert at the back
                    tmp = head.next
                    prev.next = head
                    head.next = tail
                    head = tmp

        return dummy.next

    def insertionSortList2(self, head):
        if not head: return head

        dummy = ListNode(None)
        cur = head
        while cur:
            pre = dummy
            tmp = cur.next # keep the next node
            while pre.next and pre.next.val < cur.val:
                pre = pre.next
            cur.next = pre.next # insert between pre and pre.next
            pre.next = cur
            cur = tmp
        return dummy.next


# A = [4,2,1,3]
A = [-1,5,3,4,0]
head = createLinkedList(A)
printNode(Solution().insertionSortList2(head))