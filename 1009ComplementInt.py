"""
Every non-negative integer N has a binary representation.
For example, 5 can be represented as "101" in binary, 11 as "1011" in binary, and so on.
Note that except for N = 0, there are no leading zeroes in any binary representation.

The complement of a binary representation is the number in binary you get when changing
every 1 to a 0 and 0 to a 1.  For example, the complement of "101" in binary is "010" in binary.

For a given number N in base-10, return the complement of it's binary representation
as a base-10 integer.
"""
from math import log2
class Solution(object):
    def bitwiseComplement(self, N):
        """
        :type N: int
        :rtype: int
        """
        if N == 0:
            return 1
        bit = int(log2(N)) + 1
        comple = 2**bit - 1
        return N^comple

    def bitwiseComplement2(self, N):
        c = 1
        while c < N: # Construct Mask
            c = (c << 1) + 1
        return N ^ c


N = 6
print(Solution().bitwiseComplement2(N))