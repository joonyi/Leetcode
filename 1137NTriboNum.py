"""
The Tribonacci sequence Tn is defined as follows:

T0 = 0, T1 = 1, T2 = 1, and Tn+3 = Tn + Tn+1 + Tn+2 for n >= 0.

Given n, return the value of Tn.
"""
class Solution(object):
    def tribonacci(self, n):
        """
        :type n: int
        :rtype: int
        """
        # TLE
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        return self.tribonacci(n-1) + self.tribonacci(n-2) + self.tribonacci(n-3)

    def tribonacci2(self, n):
        if n == 0:
            return 0
        elif n == 1:
            return 1
        elif n == 2:
            return 1

        T = [0] * (n + 2)
        T[0], T[1], T[2] = 0, 1, 1
        for i in range(3, n + 1):
            T[i] = T[i - 1] + T[i - 2] + T[i - 3]

        return T[n]


n = 27
print(Solution().tribonacci(n))