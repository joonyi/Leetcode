"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous)
subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.
"""
class Solution(object):
    def sumSubarrayMins(self, A):
        """
        :type A: List[int]
        :rtype: int
        """
        # Brute Force, TLE
        accum = sum(A)
        for i in range(len(A)-1):
            for j in range(i+1, len(A)):
                accum += min(A[i:j+1])
        return accum

    def sumSubarrayMins2(self, A):
        # monotone stack
        MOD = 10 ** 9 + 7
        N = len(A)

        # prev has i* - 1 in increasing order of A[i* - 1]
        # where i* is the answer to query j
        stack = []
        prev = [None] * N # previous less element
        for i in range(N):
            while stack and A[i] <= A[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        # next has k* + 1 in increasing order of A[k* + 1]
        # where k* is the answer to query j
        stack = []
        next_ = [None] * N
        for k in range(N - 1, -1, -1):
            while stack and A[k] < A[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)

        # Use prev/next array to count answer
        ans = 0 # from the distance of min val, calculate the answer
        for i in range(N):
            # ans += (prev[i] * next_[i] * A[i]) % MOD
            ans += ((i - prev[i]) * (next_[i] - i) * A[i]) % MOD
            # ans %= MOD
        return ans
        # return sum((i - prev[i]) * (next_[i] - i) * A[i] for i in range(N)) % MOD

    def sumSubarrayMins3(self, A):
        MOD = 10 ** 9 + 7

        stack = []
        ans = dot = 0
        for j, y in enumerate(A):
            # Add all answers for subarrays [i, j], i <= j
            count = 1
            while stack and stack[-1][0] >= y:
                x, c = stack.pop()
                count += c
                dot -= x * c

            stack.append((y, count))
            dot += y * count
            ans += dot
        return ans % MOD

# A = [3,1,2,4]
A = [71,55,82,55] # 593
# A = [3,6,9,12,6,8,6]
print(Solution().sumSubarrayMins3(A))