"""
Given a singly linked list, determine if it is a palindrome.
Input: 1->2
Output: false

Input: 1->2->2->1
Output: true
Follow up:
Could you do it in O(n) time and O(1) space?
"""
# The idea is to construct on list from begin to middle
# another from end to middle, then compare those two lists
from linkedlist import *
class Solution(object):
    def isPalindrome(self, head):
        slow = fast = head
        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        prev = None
        while slow:
            temp = slow.next
            slow.next = prev
            prev = slow
            slow = temp
        while head and prev:
            if head.val == prev.val:
                head = head.next
                prev = prev.next
            else:
                return False
        return True

val = [1,2,2,1]
ls = createLinkedList(val)
print(Solution().isPalindrome(ls))