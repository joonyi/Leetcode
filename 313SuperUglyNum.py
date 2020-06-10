"""
Write a program to find the nth super ugly number.

Super ugly numbers are positive numbers whose all prime factors are in the given
prime list primes of size k.

Example:

Input: n = 12, primes = [2,7,13,19]
Output: 32
Explanation: [1,2,4,7,8,13,14,16,19,26,28,32] is the sequence of the first 12
             super ugly numbers given primes = [2,7,13,19] of size 4.
Note:

1 is a super ugly number for any given primes.
The given numbers in primes are in ascending order.
0 < k ≤ 100, 0 < n ≤ 106, 0 < primes[i] < 1000.
The nth super ugly number is guaranteed to fit in a 32-bit signed integer.
"""


class Solution(object):
    def nthSuperUglyNumber(self, n, primes):
        """
        :type n: int
        :type primes: List[int]
        :rtype: int
        """
        ugly = [float('inf')] * n
        ugly[0] = 1
        idx = [0] * len(primes) # keep track latest idx of prime[i]*ugly_smaller > ugly_latest
        for i in range(1, n):
            for j in range(len(primes)):
                x = primes[j]*ugly[idx[j]]
                ugly[i] = min(ugly[i], x)

            for j in range(len(primes)):
                while primes[j]*ugly[idx[j]] <= ugly[i]:
                    idx[j] += 1

        return ugly[-1]

    def nthSuperUglyNumber2(self, n, primes):
        ugly = [0] * n
        idx = [0] * len(primes)
        val = [1] * len(primes)
        next = 1
        for i in range(n):
            ugly[i] = next
            next = 2**32 - 1
            for j in range(len(primes)):
                if val[j] == ugly[i]:
                    val[j] = ugly[idx[j]] * primes[j]
                    j += 1
                    next = min(next, val[j])

        return ugly[-1]

    def nthSuperUglyNumber3(self, n, primes):
        ugly, dp, index, ugly_nums = 1, [1], [0] * len(primes), [1] * len(primes)
        for i in range(1, n):
            # compute possibly ugly numbers and update index
            for j in range(len(primes)):
                if ugly_nums[j] == ugly:
                    ugly_nums[j] = dp[index[j]] * primes[j]
                    index[j] += 1
            # get the minimum
            ugly = min(ugly_nums)
            dp.append(ugly)
        return dp[-1]

n = 12
primes = [2,7,13,19]
print(Solution().nthSuperUglyNumber3(n, primes))
