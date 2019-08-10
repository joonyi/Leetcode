"""
Given two integers dividend and divisor, divide two integers without using multiplication,
division and mod operator.

Return the quotient after dividing dividend by divisor.

The integer division should truncate toward zero.
"""
class Solution(object):
    def divide(self, dividend, divisor):
        """
        :type dividend: int
        :type divisor: int
        :rtype: int
        """
        # TLE
        if dividend == 0:
            return 0

        cnt = 0
        if dividend < 0 and divisor < 0:
            signed = 1
        elif dividend < 0 and divisor > 0:
            signed = -1
        elif dividend > 0 and divisor < 0:
            signed = -1
        else:
            signed = 1

        dividend = abs(dividend)
        divisor = abs(divisor)
        while dividend >= divisor:
            dividend -= divisor
            cnt += 1

        return signed*cnt

    def divide2(self, dividend, divisor):
        positive = (dividend < 0) is (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            temp, i = divisor, 1
            while dividend >= temp:
                dividend -= temp
                res += i
                i <<= 1
                temp <<= 1
        if not positive:
            res = -res
        return min(max(-2147483648, res), 2147483647)

    def divide3(self, dividend, divisor):
        if dividend == -2147483648 and divisor == -1:
            return 2147483647

        positive = (dividend < 0) == (divisor < 0)
        dividend, divisor = abs(dividend), abs(divisor)
        res = 0
        while dividend >= divisor:
            tmp = divisor
            m = 1
            while tmp << 1 <= dividend:
                tmp <<= 1
                m <<= 1
            dividend -= tmp
            res += m

        if positive:
            return res
        else:
            return -res

# Idea: keep multiply divisor by 2 to approach dividend, m to count how times multiply 2
# for 17, 3, look for multiply 3 just enough to subtract 17, which is 12
# 17 - 12 = 5. Start another round 5 - 3 = 2 smaller than divisor 3, then return the answer
# The process is dividend = res * divisor + remainder

# dividend, divisor = 10, 3
# dividend, divisor = 7,-3
dividend, divisor = 17, 3
print(Solution().divide3(dividend, divisor))
