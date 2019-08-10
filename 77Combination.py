"""
Given two integers n and k, return all possible combinations of k numbers out of 1 ... n.

Example:
Input: n = 4, k = 2
Output:
[
  [2,4],
  [3,4],
  [2,3],
  [1,2],
  [1,3],
  [1,4],
]
"""
class Solution(object):
    def combine(self, n, k):
        ret = []
        self.dfs(n, k,[], 1, ret)
        return ret

    def dfs(self, n, k, path, start, ret):
        if len(path) == k:
            ret.append(path)
            return

        for i in range(start, n+1):
            self.dfs(n, k, path+[i], i+1, ret)

    def combine2(self, n, k):
        if k == n or k == 0:
            return [[i for i in range(1, k + 1)]]
        return [x + [n] for x in self.combine2(n - 1, k - 1)] + self.combine2(n - 1, k)

    # Strange but worked
    def combine3(self, n, k):
        ret = []
        i = 0
        p = [0 for _ in range(k)]
        while i >= 0 and p[0] <= n-k+1:
            p[i] += 1
            if p[i] > n:
                i -= 1
            elif i == k - 1:
                ret.append(p[:])
            else:
                i += 1
                p[i] = p[i - 1]

        return ret


n = 7
k = 3
print(Solution().combine3(n,k))