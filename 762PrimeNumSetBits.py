"""
Given two integers L and R, find the count of numbers in the range [L, R] (inclusive) having
a prime number of set bits in their binary representation.

(Recall that the number of set bits an integer has is the number of 1s present when written in binary.
For example, 21 written in binary is 10101 which has 3 set bits. Also, 1 is not a prime.)
"""

class Solution(object):
    def countPrimeSetBits(self, L, R):
        """
        :type L: int
        :type R: int
        :rtype: int
        """
        # TLE
        if R < 2:
            return 0

        sieve = [True] * 100001
        sieve[0] = sieve[1] = False
        for i in range(2, int(100001**0.5) + 1):
            if sieve[i]:
                for j in range(i*i, 100001, i):
                    sieve[j] = False

        res = 0
        for n in range(L, R + 1):
            bit = 0
            while n:
                if n % 2:
                    bit += 1
                n >>= 1
            res += sieve[bit]

        return res

    def countPrimeSetBits2(self, L, R):
        res = 0
        for n in range(L, R + 1):
            bit = 0
            while n:
                if n % 2:
                    bit += 1
                n >>= 1
            if self.isPrime(bit):
                res += 1

        return res

    def isPrime(self, x):
        # We only need primes up to 19 because R <= 10^6 < 2^20
        return (x == 2 or x == 3 or x == 5 or x == 7 or x == 11 or x == 13 or x == 17 or x == 19)


    def countPrimeSetBits3(self, L, R):
        # 0b10100010100010101100 is the bit wise representation of 665772
        # shift 665772 according to bits in the number
        # & with 1 to check it is prime
        # sum the result for each number
        return sum(665772 >> bin(i).count('1') & 1 for i in range(L, R + 1))

# L, R = 6, 10
# L, R = 10, 15
L, R = 28013, 35698
print(Solution().countPrimeSetBits(L, R))