"""
Reverse bits of a given 32 bits unsigned integer.
"""
class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        res = 0
        i = 31
        while n:
            res += (n & 1) * 2**i
            i -= 1
            n >>= 1
        return res

    def reverseBits2(self, n):
        # For 8-bit example, abcdefgh -> efghabcd -> ghefcdab -> hgfedcba
        n = (n >> 16) | (n << 16)
        n = ((n & 0xff00ff00) >> 8) | ((n & 0x00ff00ff) << 8)
        n = ((n & 0xf0f0f0f0) >> 4) | ((n & 0x0f0f0f0f) << 4)
        n = ((n & 0xcccccccc) >> 2) | ((n & 0x33333333) << 2)
        n = ((n & 0xaaaaaaaa) >> 1) | ((n & 0x55555555) << 1)
        return n


n = 43261596
print(Solution().reverseBits(n))