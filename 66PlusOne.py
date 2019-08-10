"""
Given a non-empty array of digits representing a non-negative integer,
plus one to the integer.

The digits are stored such that the most significant digit is at the
head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero,
except the number 0 itself.
"""

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        B = []
        carry = 1
        while carry:
            a = digits.pop() if digits else 0
            carry += a
            carry, r = divmod(carry, 10)
            B.append(r)
        B.reverse()
        return digits + B

    def plusOne2(self, digits):
        for i in range(len(digits)-1, -1, -1):
            if digits[i] == 9:
                digits[i] = 0
            else:
                digits[i] += 1
                return digits

        digits[0] = 1 # Only happen when digits overflow
        digits.append(0)
        return digits


A = [9]
print(Solution().plusOne2(A))