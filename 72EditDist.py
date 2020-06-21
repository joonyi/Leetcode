class Solution(object):
    def minDistance(self, word1, word2):
        """
        :type word1: str
        :type word2: str
        :rtype: int
        """
        cache = {}
        def recurse(m, n):
            if (m, n) in cache:
                return cache[(m, n)]
            if m == 0:
                res = n
            elif n == 0:
                res = m
            elif word1[m - 1] == word2[n - 1]:
                res = recurse(m - 1, n - 1)
            else:
                subCost = 1 + recurse(m - 1, n - 1)
                delCost = 1 + recurse(m - 1, n)
                insCost = 1 + recurse(m, n - 1)
                res = min(subCost, delCost, insCost)
            cache[(m, n)] = res
            return res

        x = recurse(len(word1), len(word2))
        return x

word1, word2 = "horse", "ros"
# word1, word2 = "dinitrophenylhydrazine", "benzalphenylhydrazone"
print(Solution().minDistance(word1, word2))