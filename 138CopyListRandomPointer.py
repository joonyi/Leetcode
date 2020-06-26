"""
A linked list is given such that each node contains an additional random pointer which could point
to any node in the list or null.

Return a deep copy of the list.
"""
"""
The algorithm is composed of the follow three steps which are also 3 iteration rounds.
1. Iterate the original list and duplicate each node. The duplicate of each node follows its original immediately.
2. Iterate the new list and assign the random pointer for each duplicated node.
3. Restore the original list and extract the duplicated nodes.
"""

from LinkedList import RandomPointerNode
class Solution(object):
    def copyRandomList(self, head):
        """
        :type head: Node
        :rtype: Node
        """
        if not head:
            return head

        c = head # original 1->2->3->4
        while c:
            next = c.next
            c.next = RandomPointerNode(c.val, c.next, c.random)
            c.next.next = next
            c = next
        # After first while loop, 1->1'->2->2'->3->3'->4->4'

        c = head
        while c:
            if c.random:
                c.next.random = c.random.next
            c = c.next.next
        # After second while loop, copy random pointer of the original list,
        # bcs we know clone is at adjacent

        c = head
        copyHead = head.next
        copy = copyHead
        while copy.next:
            c.next = c.next.next
            c = c.next
            copy.next = copy.next.next
            copy = copy.next
        c.next = c.next.next
        # After third while loop, 1->2->3->4, 1'->2'->3'->4'
        return copyHead

