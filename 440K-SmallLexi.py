import random
class Solution(object):
    def findKthNumber(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: int
        """
        # Too slow, TLE
        def RandomSelect(A, p, r, k):
            q = self.RandomPartition(A, p, r)
            i = q - p + 1
            if k == i:
                return A[q]
            elif k < i:
                return RandomSelect(A, p, q - 1, k)
            else:
                return RandomSelect(A, q + 1, r, k - i)

        A = [str(i) for i in range(1, n + 1)]
        p, r = 0, len(A) - 1
        return RandomSelect(A, p, r, k)


    def RandomPartition(self, A, p, r):
        i = random.randint(p, r)
        A[r], A[i] = A[i], A[r]
        return self.Partition(A, p, r)

    def Partition(self, A, p, r):
        pivot = A[r]
        i = p - 1
        for j in range(p, r):
            if A[j] <= pivot:
                i += 1
                A[j], A[i] = A[i], A[j]

        A[i + 1], A[r] = A[r], A[i + 1]
        return i + 1

    def findKthNumber2(self, n, k):
        def calSteps(n, n1, n2):
            steps = 0
            while n1 <= n:
                steps += min(n+1, n2) - n1
                n1 *= 10
                n2 *= 10
            return steps

        curr = 1
        k -= 1
        while k > 0:
            steps = calSteps(n, curr, curr+1)
            if steps <= k:
                curr += 1
                k -= steps
            else:
                curr *= 10
                k -= 1

        return curr

# Denary tree with next level is parent*10 to parent*10+9
# 1 (curr) has children 10~10, 2 (curr+1) has children 2~29 etc
# Find the kth element is to do a k steps preorder traverse of the tree.
# But dont need to do exact k steps, but calculate steps between curr and curr+1
# (neighbor nodes in same level), in order to skip unnecessary moves

n = 200
k = 40
# n = 13
# k = 2
print(Solution().findKthNumber2(n, k))