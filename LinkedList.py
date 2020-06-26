class RandomPointerNode(object):
    def __init__(self, val, next, random):
        self.val = val
        self.next = next
        self.random = random


class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

    def printNode(self):
        """
        :type node: ListNode
        :rtype: integer
        """
        node = self
        while node:
            print(node.val, end=" ")
            node = node.next
        print()

    def createLinkedList(self, val):
        """
        :type val: list
        :rtype: ListNode
        """
        head = tail = ListNode(val[0])
        for i in range(1,len(val)):
            tail.next = ListNode(val[i])
            tail = tail.next
        return head