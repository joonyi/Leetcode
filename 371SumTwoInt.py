class Solution(object):
    def getSum(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        # This one fail with a = -1, b = 1
        while (b != 0):
            carry = a & b
            a = a ^ b
            b = carry << 1

        return a

    def getSum2(self, a, b):
        """
        :type a: int
        :type b: int
        :rtype: int
        """
        if a == 0:
            return b
        elif b == 0:
            return a

        mask = 0xffffffff

        # in Python, every integer is associated with its two's complement and its sign.
        # However, doing bit operation "& mask" loses the track of sign.
        # Therefore, after the while loop, a is the two's complement of the final result as a 32-bit unsigned integer.
        while b != 0:
            a, b = (a ^ b) & mask, ((a & b) << 1) & mask

        # a is negative if the first bit is 1
        if (a >> 31) & 1:
            return ~(a ^ mask)
        else:
            return a


a = -1
b = 1
print(Solution().getSum2(a, b))