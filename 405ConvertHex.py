"""
Given an integer, write an algorithm to convert it to hexadecimal. For negative integer,
two’s complement method is used.

Note:
1. All letters in hexadecimal (a-f) must be in lowercase.
2. The hexadecimal string must not contain extra leading 0s. If the number is zero, it is represented
by a single zero character '0'; otherwise, the first character in the hexadecimal string will not be
the zero character.
3. The given number is guaranteed to fit within the range of a 32-bit signed integer.
4. You must not use any method provided by the library which converts/formats the number to hex directly.
"""
class Solution(object):
    def toHex(self, num):
        """
        :type num: int
        :rtype: str
        """
        if num == 0:
            return '0'
        elif num < 0:
            num = 2**32 + num

        num2char = {10:'a', 11:'b', 12:'c', 13:'d', 14:'e', 15:'f'}
        res = []
        while num > 0:
            if num % 16 >= 10:
                res.append(num2char[num % 16])
            else:
                res.append(str(num % 16))
            num //= 16

        return ''.join(res[::-1])

    def twos_complement(self, input_value, num_bits):
        '''Calculates a two's complement integer from the given input value's bits'''
        mask = 2 ** (num_bits - 1)
        return -(input_value & mask) + (input_value & ~mask)

    def toHex2(self, num):
        if num == 0:
            return '0'

        num2char = ['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']
        res = []
        while num != 0 and len(res) < 8:
            res.append(num2char[num & 15]) # equivalent to % 16
            num >>= 4 # equivalent to //=16
        return ''.join(res[::-1])

# 2**32 -1 = 4294967295
num = -1
print(Solution().toHex2(num))
