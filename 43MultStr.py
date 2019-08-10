"""
Given two non-negative integers num1 and num2 represented as strings,
return the product of num1 and num2, also represented as a string.

The length of both num1 and num2 is < 110.
Both num1 and num2 contain only digits 0-9.
Both num1 and num2 do not contain any leading zero, except the number 0 itself.
You must not use any built-in BigInteger library or convert the inputs to integer directly.
"""
class Solution(object):
    def multiply(self, num1, num2):
        """
        :type num1: str
        :type num2: str
        :rtype: str
        """
        n1 = 0
        for num in num1:
            n1 = n1 * 10 + ord(num) - 48
        n2 = 0
        for num in num2:
            n2 = n2 * 10 + ord(num) - 48

        product = n1 * n2

        return str(product)

    # O(n^2)
    def multiply2(self, num1, num2):
        m = len(num1)
        n = len(num2)
        pos = [0] * (m + n)
        for i in range(m-1, -1, -1):
            for j in range(n-1, -1, -1):
                mul = (ord(num1[i]) - 48) * (ord(num2[j]) - 48)
                p1 = i + j
                p2 = i + j + 1
                sum = mul + pos[p2]
                pos[p1] += sum // 10
                pos[p2] = sum % 10

        res = ''
        for x in pos:
            if res == '' and x == 0:
                continue
            else:
                res += str(x)
        return res

    def multiply3(self, num1, num2):
        if num1 == '0' or num2 == '0':
            return '0'
        m = len(num1) - 1
        n = len(num2) - 1
        carry = 0
        res = ''
        for i in range(0, m+n+1 or carry):
            for j in range(max(0,i-n), min(i,m)+1):
                carry += (ord(num1[m-j]) - 48) * (ord(num2[n-i+j]) - 48)
            res += str(carry % 10)
            carry //= 10


        return res[::-1]


num1 = "123"
num2 = "456"
print(Solution().multiply3(num1, num2))