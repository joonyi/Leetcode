"""
You are given two non-empty linked lists representing two non-negative integers.
The digits are stored in reverse order and each of their nodes contain a single digit.
Add the two numbers and return it as a linked list.

You may assume the two numbers do not contain any leading zero, except the number 0 itself.
"""

from LinkedList import *
class Solution(object):
    def addTwoNumbers(self, l1, l2):
        """
        :type l1: ListNode
        :type l2: ListNode
        :rtype: ListNode
        """
        carry = 0
        head = ListNode(None)
        x = ListNode(None)
        head.next = x

        while l1 or l2:
            x.next = ListNode(None)
            x = x.next
            if l1 and l2:
                add = l1.val + l2.val + carry
                l1 = l1.next
                l2 = l2.next
            elif l1:
                add = l1.val + carry
                l1 = l1.next
            elif l2:
                add = l2.val + carry
                l2 = l2.next

            carry = add // 10
            x.val = add % 10

        if carry:
            x.next = ListNode(carry)

        return head.next.next

    # Concise solution
    def addTwoNumbers2(self, l1, l2):
        dummy = cur = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            if l1:
                carry += l1.val
                l1 = l1.next
            if l2:
                carry += l2.val
                l2 = l2.next
            cur.next = ListNode(carry % 10)
            cur = cur.next
            carry //= 10
        return dummy.next

a = [2,4,3]
b = [5,6,4]
# a = [5]
# b = [5]
l1 = createLinkedList(a)
l2 = createLinkedList(b)
printNode(l1)
printNode(l2)
head = Solution().addTwoNumbers(l1, l2)
printNode(head)