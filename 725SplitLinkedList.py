"""
Given a (singly) linked list with head node root, write a function to split the linked list
into k consecutive linked list "parts".

The length of each part should be as equal as possible: no two parts should have a size differing
by more than 1. This may lead to some parts being null.

The parts should be in order of occurrence in the input list, and parts occurring earlier should
always have a size greater than or equal parts occurring later.

Return a List of ListNode's representing the linked list parts that are formed.
Examples 1->2->3->4, k = 5 // 5 equal parts [ [1], [2], [3], [4], null ]
"""
from linkedlist import *
class Solution(object):
    def splitListToParts(self, root, k):
        """
        :type root: ListNode
        :type k: int
        :rtype: List[ListNode]
        """
        res = []
        head = root
        cnt = 0
        while head != None:
            cnt += 1
            head = head.next

        size, extra_one = cnt // k, cnt % k # divmod
        for _ in range(extra_one):
            head = prev = root
            for _ in range(size + 1):
                prev, root = root, root.next
            if prev:
                prev.next = None
                res.append(head)
            else:
                res.append(None)

        for _ in range(k - extra_one):
            head = prev = root
            for _ in range(size):
                prev, root = root, root.next
            if prev:
                prev.next = None
                res.append(head)
            else:
                res.append(None)

        return res

    def splitListToParts2(self, root, k):
        cur = root
        cnt = 0
        while cur != None:
            cur = cur.next
            cnt += 1
        width, remainder = divmod(cnt, k)

        res = []
        cur = root
        for i in range(k):
            head = cur
            size = width + (i < remainder) - 1 # False - 1 = -1
            for j in range(size):
                if cur: cur = cur.next
            if cur:
                cur.next, cur = None, cur.next # cut the link in one shot
            res.append(head)
        return res


# A, k = [1,2,3], 5
A, k = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10], 3
# A, k = [1,2,3,4], 5
root = createLinkedList(A)
print(Solution().splitListToParts2(root, k))