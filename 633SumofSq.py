"""
Given a non-negative integer c, your task is to decide whether there're two integers
a and b such that a^2 + b^2 = c.
"""
class Solution(object):
    def judgeSquareSum(self, c):
        """
        :type c: int
        :rtype: bool
        """
        # MLE
        for i in range(int(c//2) + 1):
            tmp = c - i**2
            if tmp < 0:
                continue
            if tmp**0.5 == int(tmp**0.5):
                return True

        return False

    def judgeSquareSum2(self, c):
        for i in range(int(c//2) + 1):
            b = c - i*i
            n = 1
            sum = 0
            while sum < b:
                sum += n
                n += 2

            if sum == b:
                return True

        return False

c = 5
print(Solution().judgeSquareSum2(c))
