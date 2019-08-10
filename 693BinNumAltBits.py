"""
Given a positive integer, check whether it has alternating bits: namely,
if two adjacent bits will always have different values.
"""
class Solution(object):
    def hasAlternatingBits(self, n):
        """
        :type n: int
        :rtype: bool
        """
        n = n ^ (n >> 1)
        while n:
            if n % 2 == 0:
                return False
            n >>= 1
        return True

    def hasAlternatingBits2(self, n):
        n, cur = divmod(n, 2)
        while n:
            if cur == n % 2: return False
            n, cur = divmod(n, 2)
        return True

    def hasAlternatingBits3(self, n):
        # How this work
        n ^= n >> 2
        return not (n & n - 1)

n = 5 # T
# n = 7 # F
# n = 11 # F
# n = 10 # T
# n = 4 # F
print(Solution().hasAlternatingBits3(n))