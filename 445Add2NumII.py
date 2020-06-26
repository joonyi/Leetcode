"""
You are given two non-empty linked lists representing two non-negative integers.
The most significant digit comes first and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.

Follow up:
What if you cannot modify the input lists? In other words, reversing the lists is not allowed.
"""
from LinkedList import *
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        n1 = 0
        while l1:
            n1 = (n1 * 10) + l1.val
            l1 = l1.next

        n2 = 0
        while l2:
            n2 = (n2 * 10) + l2.val
            l2 = l2.next

        val = list(str(n1 + n2))
        head = tail = ListNode(val[0])
        for i in range(1, len(val)):
            tail.next = ListNode(val[i])
            tail = tail.next

        return head


A, B = [7,2,4,3], [5,6,4]
l1 = createLinkedList(A)
l2 = createLinkedList(B)
print(Solution().addTwoNumbers(l1, l2))