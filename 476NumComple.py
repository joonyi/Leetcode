"""
Given a positive integer, output its complement number. T
he complement strategy is to flip the bits of its binary representation.

Note:
The given integer is guaranteed to fit within the range of a 32-bit signed integer.
You could assume no leading zero bit in the integer’s binary representation.
"""
class Solution(object):
    def findComplement(self, num):
        """
        :type num: int
        :rtype: int
        """
        accum = 0
        unit = 1
        while num > 0:
            if num % 2 == 0:
                accum += unit
            unit *= 2
            num >>= 1

        return accum

    def findComplement2(self, num):
        """
        num          = 00000101
        mask         = 11111000
        ~mask & ~num = 00000010
        """
        mask = ~0
        while num & mask:
            mask <<= 1
        return ~mask & ~num


num = 5
print(Solution().findComplement2(num))