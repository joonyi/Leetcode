"""
Given an integer, write a function to determine if it is a power of three.
"""
class Solution(object):
    def isPowerOfThree(self, n):
        """
        :type n: int
        :rtype: bool
        """
        if n <= 0:
            return False
        if n == 1:
            return True
        if n % 3 == 0:
            return self.isPowerOfThree(n//3)
        else:
            return False

n = -3
print(Solution().isPowerOfThree(n))