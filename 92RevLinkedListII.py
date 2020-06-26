"""
Reverse a linked list from position m to n. Do it in one-pass.
Note: 1 ≤ m ≤ n ≤ length of list.

Example:
Input: 1->2->3->4->5->NULL, m = 2, n = 4
Output: 1->4->3->2->5->NULL
"""
from LinkedList import *
class Solution(object):
    def reverseBetween(self, head, m, n):
        """
        :type head: ListNode
        :type m: int
        :type n: int
        :rtype: ListNode
        """
        if m == n:
            return head

        cnt = 1
        tail = head
        prev = None
        while cnt < m:
            prev = tail
            tail = tail.next
            cnt += 1

        start = prev
        while cnt <= n:
            tmp = tail.next
            tail.next = prev  # reverse
            prev = tail
            tail = tmp
            cnt += 1

        # Four cases
        # 1. Reverse in the middle, 2.reverse the whole list
        # 3. Reverse at the head, 4. reverse at the tail
        if start and tail:
            start.next.next = tail
            start.next = prev
        elif not start and not tail:
            head = prev
        elif not start and tail:
            head.next = tail
            head = prev
        else:
            start.next.next = tail
            start.next = prev

        return head

    def reverseBetween2(self, head, m, n):
        if not head:
            return None

        left, right = head, head
        stop = False
        def recurseAndReverse(right, m, n):
            nonlocal left, stop
            if n == 1:
                return
            # Keep moving the right pointer one step forward until (n == 1)
            right = right.next

            # Keep moving left pointer to the right until we reach the proper node
            # from where the reversal is to start.
            if m > 1:
                left = left.next

            # Recurse with m and n reduced.
            recurseAndReverse(right, m - 1, n - 1)

            # In case both the pointers cross each other or become equal, we
            # stop i.e. don't swap data any further. We are done reversing at this
            # point.
            if left == right or right.next == left:
                stop = True

            # Until the boolean stop is false, swap data between the two pointers
            if not stop:
                left.val, right.val = right.val, left.val

                # Move left one step to the right.
                # The right pointer moves one step back via backtracking.
                left = left.next

        recurseAndReverse(right, m, n)
        return head

# A, m, n = [1,2,3,4,5], 2, 4
# A, m, n = [5], 1, 1
# A, m, n = [3,5], 1, 1
# A, m, n = [3,5], 1, 2
# A, m, n = [1,2,3], 1, 2
A, m, n = [1,2,3,4,5], 4, 5
head = createLinkedList(A)
printNode(Solution().reverseBetween2(head, m, n))