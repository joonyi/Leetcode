"""
Given a singly linked list, return a random node's value from the linked list.
Each node must have the same probability of being chosen.

Follow up:
What if the linked list is extremely large and its length is unknown to you?
Could you solve this efficiently without using extra space?
"""
import random
from LinkedList import ListNode
class Solution:
    def __init__(self, head: ListNode):
        """
        @param head The linked list's head.
        Note that the head is guaranteed to be not null, so it contains at least one node.
        """
        self.head = head

    def getRandom(self) -> int:
        """
        Returns a random node's value.
        """
        result, node, i = self.head, self.head.next, 1
        while node:
            if random.randint(0, i) == 0:
                result = node
            node = node.next
            i += 1
        return result.val

"""
First node, pick the head, probability 1
Second node, decide to take the new val with probability 1/2
Third node, decide to take the new val with probability 1/3 and so on
The math proves that if length is large or unknown, this algorithm gives result of 
each node with same probability 1/n
"""
# Your Solution object will be instantiated and called as such:
A = [1,2,3]
head = ListNode(None).createLinkedList(A)
# head.printNode()
obj = Solution(head)
print(obj.getRandom())
