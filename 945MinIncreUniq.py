"""
Given an array of integers A, a move consists of choosing any A[i], and incrementing it by 1.

Return the least number of moves to make every value in A unique.
"""

class Solution(object):
    def minIncrementForUnique(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # TLE
        if len(A) <= 1:
            return 0
        uniq = [0] * (max(max(A), len(A)) + 1)
        dups = []
        for n in A:
            if not uniq[n]:
                uniq[n] = 1
            else:
                dups.append(n)

        if not dups:
            return 0

        uniq += [0] * len(dups)
        cnt = 0
        for n in dups:
            while uniq[n]:
                n += 1
            uniq[n] = 1
            cnt += n
        return cnt - sum(dups)

    def minIncrementForUnique2(self, A):
        res = next_num = 0
        A.sort()
        for n in A:
            res += max(next_num - n, 0)
            next_num = max(next_num + 1, n + 1)
        return res

    def minIncrementForUnique3(self, A):
        # Union find??
        root = {}
        def find(x):
            root[x] = find(root[x] + 1) if x in root else x
            return root[x]

        return sum(find(a) - a for a in A)


# A = [1,2,2]  # 1
# A = [3,2,1,2,1,7]  # 6
A = [4,4,7,5,1,9,4,7,3,8]  # 12
# A = [14,4,5,14,13,14,10,17,2,12,2,14,7,13,14,13,4,16,4,10]  # 41
print(Solution().minIncrementForUnique3(A))
