"""
You are given n pairs of numbers. In every pair, the first number is always smaller than
the second number.

Now, we define a pair (c, d) can follow another pair (a, b) if and only if b < c.
Chain of pairs can be formed in this fashion.

Given a set of pairs, find the length longest chain which can be formed.
You needn't use up all the given pairs. You can select pairs in any order.
"""
class Solution(object):
    def findLongestChain(self, pairs):
        """
        :type pairs: List[List[int]]
        :rtype: int
        """
        # Attempted but fail
        # Should sort with pairs[1], not pairs[0]
        max_now = -float('inf')
        pairs.sort(key=lambda pairs : pairs[0])
        for i in range(len(pairs)):
            cnt = 1
            j = i + 1
            pair = pairs[i]
            while j < len(pairs):
                if pairs[j][0] > pair[1]:
                    pair = pairs[j]
                    cnt += 1
                j += 1
            max_now = max(max_now, cnt)

        return max_now

    def findLongestChain2(self, pairs):
        pairs.sort()
        dp = [1] * len(pairs)
        for j in range(len(pairs)):
            for i in range(j):
                if pairs[i][1] < pairs[j][0]:
                    dp[j] = max(dp[j], dp[i] + 1)

        return max(dp)

    def findLongestChain3(self, pairs):
        # sort with second coordinate and greedily add to the chain
        import operator
        cur, cnt = float('-inf'), 0
        for x, y in sorted(pairs, key=operator.itemgetter(1)): # mean sort with pairs[1]
            if cur < x:
                cur = y
                cnt += 1
        return cnt

# pairs = [[1,2], [2,3], [3,4]]
# pairs = [[-10,-8],[8,9],[-5,0],[6,10],[-6,-4],[1,7],[9,10],[-4,7]] # expect 4
# pairs = [[-6,9],[1,6],[8,10],[-1,4],[-6,-2],[-9,8],[-5,3],[0,3]] # 3
pairs = [[7,9],[4,5],[7,9],[-7,-1],[0,10],[3,10],[3,6],[2,3]] # 4
print(Solution().findLongestChain3(pairs))