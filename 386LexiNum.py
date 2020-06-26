"""
Given an integer n, return 1 - n in lexicographical order.
For example, given 13, return: [1,10,11,12,13,2,3,4,5,6,7,8,9].
Please optimize your algorithm to use less time and space. The input size may be as large as 5,000,000.
"""

from typing import List
class Solution:
    def lexicalOrder(self, n: int) -> List[int]:
        def dfs(cur, res):
            res.append(cur)
            for i in range(10):
                if 10 * cur + i <= n:
                    dfs(10 * cur + i, res)

        res = []
        for i in range(1, 10):
            if i <= n:
                dfs(i, res)
        return res

    def lexicalOrder2(self, n: int) -> List[int]:
        A = sorted([str(i) for i in range(1, n + 1)])
        return list(map(int, A))

    def lexicalOrder3(self, n):
        ans = [1]
        while len(ans) < n:
            new = ans[-1] * 10
            while new > n:
                new = new // 10 + 1
                while new % 10 == 0:  # deal with case like 19+1=20 when we need to //10 again to restart at 2
                    new //= 10
            ans.append(new)
        return ans


n = 13  # [1,10,11,12,13,2,3,4,5,6,7,8,9]
# n = 1  # [1]
# n = 34  # [1,10,11,12,13,14,15,16,17,18,19,2,20,21,22,23,24,25,26,27,28,29,3,30,31,32,33,34,4,5,6,7,8,9]
print(Solution().lexicalOrder3(n))

