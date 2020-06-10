"""
Given a linked list and a value x, partition it such that all nodes less than x come
before nodes greater than or equal to x.

You should preserve the original relative order of the nodes in each of the two partitions.

Example:
Input: head = 1->4->3->2->5->2, x = 3
Output: 1->2->2->4->3->5
"""
from linkedlist import *
class Solution(object):
    def partition(self, head, x):
        """
        :type head: ListNode
        :type x: int
        :rtype: ListNode
        """
        lessHead = less = ListNode(None)
        greatHead = great = ListNode(None)
        while head:
            if head.val < x:
                less.next = head
                less = less.next
            else:
                great.next = head
                great = great.next

            head = head.next

        great.next = None
        less.next = greatHead.next
        return lessHead.next


A, x = [1,4,3,2,5,2], 3
head = createLinkedList(A)
printNode(Solution().partition(head, x))