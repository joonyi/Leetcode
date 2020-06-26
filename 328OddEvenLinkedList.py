"""
Given a singly linked list, group all odd nodes together followed by the even nodes.
Please note here we are talking about the node number and not the value in the nodes.

You should try to do it in place. The program should run in O(1) space complexity and O(nodes)
time complexity.
"""
from LinkedList import *
class Solution(object):
    def oddEvenList(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        if not head:
            return head

        odd = head
        even = cur = head.next
        while cur and cur.next:
            odd.next = cur.next
            odd = odd.next
            cur.next = odd.next
            cur = cur.next
        odd.next = even
        return head


A = [1,2,3,4,5]
A = [2,1,3,5,6,4,7]
head = createLinkedList(A)
printNode(Solution().oddEvenList(head))