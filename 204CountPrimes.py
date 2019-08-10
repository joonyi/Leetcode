"""
Count the number of prime numbers less than a non-negative number, n.

Example:

Input: 10
Output: 4
Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
"""
import time
class Solution:
    def countPrimes(self, n):
        if n < 3:
            return 0
        primes = [True] * n
        primes[0] = primes[1] = False
        for i in range(2, int(n ** 0.5) + 1):
            if primes[i]:
                primes[i * i: n: i] = [False] * len(primes[i * i: n: i])
        return sum(primes)

    def countPrimes2(self, n):
        """
        :type n: int
        :rtype: int
        """
        not_prime = [False] * n
        count = 0
        for i in range(2, n):
            if not not_prime[i]:
                count += 1
                j = 2
                while i * j < n:
                    not_prime[i * j] = True
                    j += 1
        # print not_prime
        return count

n = 2000000
print(Solution().countPrimes2(n))
print("This program took: " + str(time.process_time() * 1000) + "ms.")