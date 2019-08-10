"""
Input: [5,3,4,5]
Output: true
Explanation:
Alex starts first, and can only take the first 5 or the last 5.
Say he takes the first 5, so that the row becomes [3, 4, 5].
If Lee takes 3, then the board is [4, 5], and Alex takes 5 to win with 10 points.
If Lee takes the last 5, then the board is [3, 4], and Alex takes 4 to win with 9 points.
This demonstrated that taking the first 5 was a winning move for Alex, so we return true.
"""
class Solution(object):
    def stoneGame(self, piles):
        """
        :type piles: List[int]
        :rtype: bool
        """
        n = len(piles)
        res = [[0 for _ in range(n)] for _ in range(n)]
        for size in range(n):
            for j in range(size, n):
                i = j - size
                a, b, c = 0, 0, 0

                if i + 2 <= j:
                    a = res[i + 2][j]
                if i + 1 <= j - 1:
                    b = res[i + 1][j - 1]
                if i <= j - 2:
                    c = res[i][j - 2]

                res[i][j] = max(piles[i] + min(a, b), piles[j] + min(b, c))

        left = sum(piles) - res[0][len(piles)-1]
        if res[0][len(piles)-1] > left:
            return True
        else:
            return False

    # 1D dp, not sure how it works
    def stoneGame2(self, piles):
        n = len(piles)
        dp = piles[:]
        for d in range(1, n):
            for i in range(n - d):
                dp[i] = max(piles[i] - dp[i + 1], piles[i + d] - dp[i])
        return dp[0] > 0



piles = [5,3,4,5]
print(Solution().stoneGame2(piles))