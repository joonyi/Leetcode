"""
Given a positive integer n, find the least number of perfect square numbers
(for example, 1, 4, 9, 16, ...) which sum to n.
"""
class Solution(object):
    def numSquares(self, n):
        """
        :type n: int
        :rtype: int
        """
        # dp[n] indicates that the perfect squares count of the given n
        dp = [float('inf')] * (n + 1)
        dp[0] = 0
        for i in range(1, n + 1):
            j = 1
            while j * j <= i:
                # for each i, it is the sum of some number i-j*j and a perfect square j*j
                dp[i] = min(dp[i], dp[i - j*j] + 1)
                j += 1

        return dp[n]

    def numSquares2(self, n):
        # Lagrange's Four Square theorem
        if int(n**0.5) * int(n**0.5) == n:
            return 1

        # The result is 4 if and only if n can be written in the form of 4 ^ k * (8 * m + 7).Please
        # Legendre's three-square theorem
        while (n & 3) == 0: # n%4 == 0
            n >>= 2

        if (n & 7) == 7: # n%8 == 7
            return 4

        for i in range(1, int(n**0.5) + 1):
            if int((n - i*i)**0.5) * int((n - i*i)**0.5) == n - i*i:
                return 2

        return 3

    def numSquares3(self, n):
        # BFS. Consider a graph which consists of number 0...n as its nodes
        # Node j is connected to node i via an edge iff either j = i + perfect sq or
        # i = j + perfect sq. Starting from node 0, do bfs to find step m to reach n
        if n < 2:
            return n
        lst = []
        i = 1
        while i * i <= n:
            lst.append(i * i)
            i += 1
        cnt = 0
        toCheck = {n}
        while toCheck:
            cnt += 1
            temp = set()
            for x in toCheck:
                for y in lst:
                    if x == y:
                        return cnt
                    if x < y:
                        break
                    temp.add(x - y)
            toCheck = temp

        return cnt

n = 12 # 3
print(Solution().numSquares3(n))