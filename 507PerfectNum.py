"""
We define the Perfect Number is a positive integer that is equal to the sum of all
its positive divisors except itself.

Now, given an integer n, write a function that returns true when it is a perfect number
and false when it is not.

Example:
Input: 28
Output: True
Explanation: 28 = 1 + 2 + 4 + 7 + 14
Note: The input number n will not exceed 100,000,000. (1e8)
"""
class Solution(object):
    def checkPerfectNumber(self, num):
        """
        :type num: int
        :rtype: bool
        """
        if num <= 1: return False
        res = 1
        for i in range(2, int(num**0.5) + 1):
            if num % i == 0:
                res += num //i + i

        return res == num

    def checkPerfectNumber2(self, num):
        # Euclid-Euler Theorem
        def pn(p):
            return (1 << (p-1)) * ((1 << p) - 1)
        primes = (2, 3, 5, 7, 13, 17, 19, 31)
        for prime in primes:
            if pn(prime) == num:
                return True

        return False

num = 28 # T
num = 1 # F
print(Solution().checkPerfectNumber(num))