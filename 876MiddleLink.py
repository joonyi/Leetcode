"""
Given a non-empty, singly linked list with head node head, return a middle node of linked list.

If there are two middle nodes, return the second middle node.
"""

from LinkedList import *
class Solution(object):
    def middleNode(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        # Get size then get middle
        node = head
        length = 0
        while node != None:
            length += 1
            node = node.next

        mid = length // 2 + 1 if length % 2 == 0 else length // 2 + 1
        cnt = 1
        node = head
        while node != None:
            if cnt == mid:
                return node
            node = node.next
            cnt += 1

    # Put into array for fast access
    def middleNode2(self, head):
        A = [head]
        while A[-1].next:
            A.append(A[-1].next)
        return A[len(A) // 2]

    # Fast and slow pointers
    def middleNode3(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        return slow


# A = [1,2,3,4,5] # node 3
A = [1,2,3,4,5,6] # node 4
head = createLinkedList(A)
print(Solution().middleNode2(head))


