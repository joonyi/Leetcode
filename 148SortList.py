"""
Sort a linked list in O(n log n) time using constant space complexity.
"""
from linkedlist import *
class Solution(object):
    def sortList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head or not head.next:
            return head

        # cut the list into two halves
        prev = None
        slow = fast = head
        while fast and fast.next:
            prev = slow
            slow = slow.next
            fast = fast.next.next

        prev.next = None

        # sort each half
        l1 = self.sortList(head)
        l2 = self.sortList(slow)

        return self.mergeList(l1, l2)

    def mergeList(self, l1, l2):
        dummy = p = ListNode(None)
        while l1 and l2:
            if l1.val < l2.val:
                p.next = l1
                l1 = l1.next
            else:
                p.next = l2
                l2 = l2.next
            p = p.next

        if l1:
            p.next = l1
        elif l2:
            p.next = l2

        return dummy.next


A = createLinkedList([4,2,1,3])
# A = createLinkedList([-1,5,3,4,0])
printNode(Solution().sortList(A))