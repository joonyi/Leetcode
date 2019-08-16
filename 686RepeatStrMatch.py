"""
Given two strings A and B, find the minimum number of times A has to be repeated such that
B is a substring of it. If no such solution, return -1.

For example, with A = "abcd" and B = "cdabcdab".

Return 3, because by repeating A three times (“abcdabcdabcd”), B is a substring of it; and
B is not a substring of A repeated two times ("abcdabcd").

Note:
The length of A and B will be between 1 and 10000.
"""
class Solution(object):
    def repeatedStringMatch(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: int
        """
        q = (len(B) - 1) // len(A) + 1 # q is the multiplier that make len(A)==len(B), +1 because at least multiply once
        for i in range(2):
            if B in A * (q + i):
                return q + i
        return -1


    def repeatedStringMatch2(self, A, B): # Rabin-Karp (Rolling Hash)
        def check(index):
            return all(A[(i + index) % len(A)] == x
                       for i, x in enumerate(B))

        q = (len(B) - 1) // len(A) + 1

        p, MOD = 113, 10 ** 9 + 7
        p_inv = pow(p, MOD - 2, MOD)
        power = 1

        b_hash = 0
        for x in map(ord, B):
            b_hash += power * x
            b_hash %= MOD
            power = (power * p) % MOD

        a_hash = 0
        power = 1
        for i in range(len(B)):
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            power = (power * p) % MOD

        if a_hash == b_hash and check(0): return q

        power = (power * p_inv) % MOD
        for i in range(len(B), (q + 1) * len(A)):
            a_hash = (a_hash - ord(A[(i - len(B)) % len(A)])) * p_inv
            a_hash += power * ord(A[i % len(A)])
            a_hash %= MOD
            if a_hash == b_hash and check(i - len(B) + 1):
                return q if i < q * len(A) else q + 1

        return -1

A, B = "abcd", "cdabcdab"
# A, B = "aa", "a"
# A, B = "abc", "cabcabca"
# A, B = "aaaaaaaaaaaaaaaaaaaaaab", "ba"
print(Solution().repeatedStringMatch2(A, B))