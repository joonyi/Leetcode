"""
We are given two strings, A and B.

A shift on A consists of taking string A and moving the leftmost character to the rightmost position.
For example, if A = 'abcde', then it will be 'bcdea' after one shift on A. Return True if and only if
A can become B after some number of shifts on A.
"""
class Solution(object):
    def rotateString(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(B) < len(A):
            return False
        A += A
        return B in A


    def rotateString2(self, A, B):
        # KMP algorithm
        N = len(A)
        if N != len(B): return False
        if N == 0: return True

        # Compute shift table
        shifts = [1] * (N + 1)
        left = -1
        for right in range(N):
            while left >= 0 and B[left] != B[right]:
                left -= shifts[left]
            shifts[right + 1] = right - left
            left += 1

        # Find match of B in A+A
        match_len = 0
        for char in A + A:
            while match_len >= 0 and B[match_len] != char:
                match_len -= shifts[match_len]

            match_len += 1
            if match_len == N:
                return True

        return False

"""
1. Brute Force
2. Simple check as above. Work bcs B is a rotated string
3. Rolling hash
4, KMP (Knuth-Morris-Pratt), O(n)
"""
A, B = 'abcde', 'cdeab'
# A, B = 'abcde', 'abced'
# A, B = "aa", "a"
print(Solution().rotateString2(A, B))