"""
Given two non-negative integers num1 and num2 represented as string, return the sum of num1 and num2.

Note:

The length of both num1 and num2 is < 5100.
Both num1 and num2 contains only digits 0-9.
Both num1 and num2 does not contain any leading zero.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def addStrings(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        p = len(num1) - 1
        q = len(num2) - 1
        carry = 0
        res = ''
        while p >= 0 or q >= 0 or carry:
            if p < 0 and q < 0:
                add = carry
            elif p < 0:
                add = ord(num2[q]) - 48 + carry
            elif q < 0:
                add = ord(num1[p]) - 48 + carry
            else:
                add = ord(num1[p]) - 48 + ord(num2[q]) - 48 + carry

            carry = 0
            if add >= 10:
                carry = 1
                add -= 10

            res = str(add) + res
            p -= 1
            q -= 1

        return res


num1 = '1'
num2 = '9'
print(Solution().addStrings(num1, num2))