"""
Given a linked list, return the node where the cycle begins.
If there is no cycle, return null.

Note: Do not modify the linked list.
"""

class ListNode(object):
    def __init__(self, x):
        self.val = x
        self.next = None

class Solution(object):
    def detectCycle(self, head):
        """
        :type head: ListNode
        :rtype: ListNode
        """
        slow = fast = head
        cycle = False
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
            if slow == fast:
                cycle = True
                break

        if cycle == False:
            return None
        else:
            slow = slow.next
            while head != slow:
                slow = slow.next
                head = head.next

            return head

    def detectCycle2(self, head):
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            if slow == fast:
                break
        else:
            return None
        
        fast = head
        while fast != slow:
            slow = slow.next
            fast = fast.next
        return slow


x = ListNode(1)
x.next = ListNode(2)
x.next.next = ListNode(None)
print(Solution().detectCycle(x))