"""
We are given head, the head node of a linked list containing unique integer values.

We are also given the list G, a subset of the values in the linked list.

Return the number of connected components in G, where two values are connected if they appear
consecutively in the linked list.
"""

from linkedlist import *
class Solution(object):
    def numComponents(self, head, G):
        """
        :type head: ListNode
        :type G: List[int]
        :rtype: int
        """
        Gset = set(G)
        ans = 0
        while head:
            if head.val in Gset and (head.next == None or head.next.val not in Gset):
                ans += 1
            head = head.next

        return ans

    def numComponents2(self, head, G):
        Gset = set(G)
        ans = 0
        while head:
            if (head.val in Gset and getattr(head.next, 'val', None) not in Gset):
                ans += 1
            head = head.next

        return ans

# A, G = createLinkedList([0,1,2,3]), [0,1,3] # 2
A, G = createLinkedList([0,1,2,3,4,5,6,7]), [0,2,3,5,7] # 4
print(Solution().numComponents(A, G))
