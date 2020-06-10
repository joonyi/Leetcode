"""
Given a list of dominoes, dominoes[i] = [a, b] is equivalent to dominoes[j] = [c, d] if and only if
either (a==c and b==d), or (a==d and b==c) - that is, one domino can be rotated to be equal to another
domino.

Return the number of pairs (i, j) for which 0 <= i < j < dominoes.length, and dominoes[i] is equivalent
to dominoes[j].
"""
class Solution(object):
    def numEquivDominoPairs(self, dominoes):
        """
        :type dominoes: List[List[int]]
        :rtype: int
        """
        seen = set()
        res = 0
        for domino in dominoes:
            a, b = domino
            if (a,b) not in seen:
                seen.add((a,b))
                seen.add((b,a))
            else:
                res += 1

        return res

    def numEquivDominoPairs2(self, dominoes):
        d = {}
        cnt = 0
        for a, b in dominoes:
            key = min(a, b) * 10 + max(a, b)
            # if d.__contains__(key):
            if key in d:
                cnt += d[key]  # the number of dominoes already in the map is the number of the newly found pairs.
                d[key] += 1
            else:
                d[key] = 1
        return cnt

# dominoes = [[1,2],[2,1],[3,4],[5,6]]
dominoes = [[1,2],[1,2],[1,1],[1,2],[2,2]]
print(Solution().numEquivDominoPairs2(dominoes))