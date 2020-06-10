"""
Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

k is a positive integer and is less than or equal to the length of the linked list.
If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

Example:
Given this linked list: 1->2->3->4->5
For k = 2, you should return: 2->1->4->3->5
For k = 3, you should return: 3->2->1->4->5

Note:
Only constant extra memory is allowed.
You may not alter the values in the list's nodes, only nodes itself may be changed.
"""
from linkedlist import *
class Solution(object):
    def reverseKGroup(self, head, k):
        """
        :type head: ListNode
        :type k: int
        :rtype: ListNode
        """
        cur = head
        n = 0
        while cur: # count length
            cur = cur.next
            n += 1

        group = n // k
        dummy = connect = ListNode(None)
        while group:
            y = None # start reversing
            for _ in range(k):
                x = head.next
                head.next = y
                y = head
                head = x

            connect.next = y # connect to the result
            while connect.next: # prepare connect for the next result
                connect = connect.next

            group -= 1

        connect.next = head
        return dummy.next

    def reverseKGroup2(self, head, k):
        cur = head
        cnt = 0
        while cur and cnt != k: # find k + 1 node
            cur = cur.next
            cnt += 1
        if cnt == k:
            cur = self.reverseKGroup2(cur, k) # reverse list with k+1 node as head
            # head - head-pointer to direct part
            # cur - head-pointer to reversed part
            while cnt:
                tmp = head.next # tmp - next head in direct part
                head.next = cur # preappending "direct" head to the reversed list
                cur = head # move head of reversed part to a new node
                head = tmp # move "direct" head to the next node in direct part
                cnt -= 1
            head = cur
        return head

    def reverseKGroup3(self, head, k):
        if head == None:
            return None
        dummy = ListNode(-1)
        dummy.next = head

        tail = dummy
        while head:
            start = head
            count = 0
            while count < k and head:
                head = head.next
                count += 1
            if count == k:
                # reverse
                prv = None
                new_tail = start
                while count > 0:
                    nxt = start.next
                    start.next = prv
                    prv = start
                    start = nxt
                    count -= 1
                tail.next = prv
                tail = new_tail
            else:
                # no need to reverse
                tail.next = start

        return dummy.next



A, k = createLinkedList([1,2,3,4,5]), 2
# A, k = createLinkedList([1,2,3,4,5]), 3
printNode(Solution().reverseKGroup2(A, k))