"""
Find the nth digit of the infinite integer sequence 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11,
Note: n is positive and will fit within the range of a 32-bit signed integer (n < 231).
"""


class Solution(object):
    def findNthDigit(self, n):
        """
        :type n: int
        :rtype: int
        """
        start, size, step = 1, 1, 9
        while n > size * step:
            n = n - (size * step)
            size = size + 1
            step = step * 10
            start = start * 10

        return int(str(start + (n - 1) // size)[(n - 1) % size])

n = 110
print(Solution().findNthDigit(n))