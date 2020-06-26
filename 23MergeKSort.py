"""
Merge k sorted linked lists and return it as one sorted list. Analyze and describe its complexity.
"""
from LinkedList import *
class Solution(object):
    def mergeKLists(self, lists):
        """
        :type lists: List[ListNode]
        :rtype: ListNode
        """
        # Append on values into a list, sort it, return a sorted list
        self.nodes = []
        head = point = ListNode(0)
        for l in lists:
            while l:
                self.nodes.append(l.val)
                l = l.next
        for x in sorted(self.nodes):
            point.next = ListNode(x)
            point = point.next
        return head.next

    def mergeKLists2(self, lists):
        # Priority Queue
        import heapq
        pre = cur = ListNode(0)
        heap = []
        for i in range(len(lists)):
            # in case of two or more nodes have same val, it prompts error bcs compare Listnode, add one more i to prevent
            heapq.heappush(heap, (lists[i].val, i, lists[i]))

        while heap:
            node = heapq.heappop(heap)
            idx = node[1]
            cur.next = node[2]
            cur = cur.next
            if cur.next:
                heapq.heappush(heap, (cur.next.val, idx, cur.next))

        return pre.next

    def mergeKLists3(self, lists):
        # divide and conquer
        amount = len(lists)
        interval = 1
        while interval < amount:
            for i in range(0, amount - interval, interval * 2):
                # merge 0-1, 2-3, 4-5, then 0-2, then 0-4
                lists[i] = self.merge2Lists(lists[i], lists[i + interval])
            interval *= 2
        return lists[0] if amount > 0 else lists

    def merge2Lists(self, l1, l2):
        head = point = ListNode(0)
        while l1 and l2:
            if l1.val <= l2.val:
                point.next = l1
                l1 = l1.next
            else:
                point.next = l2
                l2 = l1
                l1 = point.next.next
            point = point.next
        if not l1:
            point.next = l2
        else:
            point.next = l1
        return head.next

    def mergeKLists4(self, lists):
        # Compare one by one TLE
        # Next time write a better implementation
        min_idx = 0
        h = head = ListNode(0)
        while True:
            isBreak = True
            minV = float('inf')
            for i in range(len(lists)):
                if lists[i]:
                    if lists[i].val < minV:
                        min_idx = i
                        minV = lists[i].val
                    isBreak = False

            if isBreak: break

            h.next = lists[min_idx]
            h = h.next
            lists[min_idx] = lists[min_idx].next

        h.next = None
        return head.next


A = createLinkedList([1,4,5])
B = createLinkedList([1,3,4])
C = createLinkedList([2,6])
printNode(Solution().mergeKLists4([A, B, C]))