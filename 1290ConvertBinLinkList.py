"""
Given head which is a reference node to a singly-linked list.
The value of each node in the linked list is either 0 or 1.
The linked list holds the binary representation of a number.

Return the decimal value of the number in the linked list.
"""


# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

from LinkedList import ListNode
class Solution:
    def getDecimalValue(self, head: ListNode) -> int:
        def traverse(curr):
            if not curr:
                return -1
            else:
                n = 1 + traverse(curr.next)
                if curr.val:
                    self.res += 2**n

                return n

        self.res = 0
        traverse(head)
        return self.res


    def getDecimalValue2(self, head: ListNode) -> int:
        num = head.val
        while head.next:
            num = num * 2 + head.next.val  # num = (num << 1) | head.next.val
            head = head.next
        return num

    def getDecimalValue3(self, head: ListNode) -> int:
        def traverse(head, n):
            if not head:
                return n
            else:
                return traverse(head.next, n * 2 + head.val)

        return traverse(head, 0)


A = [1,0,1]
# A = [0]
# A = [1]
# A = [1,0,0,1,0,0,1,1,1,0,0,0,0,0,0]
head = ListNode(None).createLinkedList(A)
print(Solution().getDecimalValue2(head))