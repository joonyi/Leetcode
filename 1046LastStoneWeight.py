"""
We have a collection of rocks, each rock has a positive integer weight.

Each turn, we choose the two heaviest rocks and smash them together.
Suppose the stones have weights x and y with x <= y.  The result of this smash is:

If x == y, both stones are totally destroyed;
If x != y, the stone of weight x is totally destroyed, and the stone of weight y has new weight y-x.
At the end, there is at most 1 stone left.  Return the weight of this stone
(or 0 if there are no stones left.)
"""

class Solution(object):
    def lastStoneWeight(self, stones):
        """
        :type stones: List[int]
        :rtype: int
        """
        while len(stones) > 1:
            stones.sort()
            if stones[-1] == stones[-2]:
                stones = stones[:len(stones)-2]
            else:
                stones[-2] = stones[-1] - stones[-2]
                stones.pop()

        return stones[0] if stones else 0

    def lastStoneWeight2(self, stones):
        import heapq
        pq = [-stone for stone in stones]
        heapq.heapify(pq)
        for i in range(len(stones) - 1):
            y, x = -heapq.heappop(pq), -heapq.heappop(pq)
            heapq.heappush(pq, -abs(y - x))
        return -pq[0]

# stones = [2,7,4,1,8,1]
stones = [2,2]
print(Solution().lastStoneWeight2(stones))