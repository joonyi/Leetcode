"""
In an array A of 0s and 1s, how many non-empty subarrays have sum S?
"""
class Solution(object):
    def numSubarraysWithSum(self, A, S):
        """
        :type A: List[int]
        :type S: int
        :rtype: int
        """
        # TLE sliding window
        if len(A) == 1 and A[0] == S:
            return 1
        elif len(A) == 1 and A[0] != S:
            return 0

        p = 0
        cnt = 0
        while p < len(A):
            sum = A[p]
            q = p
            while q < len(A) and sum <= S:
                if p != q:
                    sum += A[q]
                if sum == S:
                    cnt += 1

                q += 1

            p += 1
        return cnt

    def numSubarraysWithSum2(self, A, S):
        indexes = [-1] + [ix for ix, v in enumerate(A) if v] + [len(A)]
        ans = 0

        if S == 0:
            for i in range(len(indexes) - 1):
                # w: number of zeros between two consecutive ones
                w = indexes[i + 1] - indexes[i] - 1
                ans += w * (w + 1) / 2
            return ans

        for i in range(1, len(indexes) - S):
            j = i + S - 1
            left = indexes[i] - indexes[i - 1]
            right = indexes[j + 1] - indexes[j]
            ans += left * right
        return ans

    def numSubarraysWithSum3(self, A, S):
        # Prefix sum
        import collections
        P = [0]
        for x in A: P.append(P[-1] + x)
        count = collections.Counter()

        ans = 0
        for x in P:
            ans += count[x]
            count[x + S] += 1
        return ans

    def numSubarraysWithSum4(self, A, S):
        # Prefix sum
        import collections
        c = collections.Counter({0: 1})
        psum = res = 0
        for i in A:
            psum += i
            res += c[psum - S]
            c[psum] += 1
        return res


A, S = [1,0,1,0,1], 2 #4
# A, S = [1,1,0,1], 2 #4
# A, S = [0,0,0,0,0], 0 #15
print(Solution().numSubarraysWithSum4(A, S))