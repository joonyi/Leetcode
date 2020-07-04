"""
Given a non-negative integer n, count all numbers with unique digits, x, where 0 ≤ x < 10**n
"""

class Solution:
    def countNumbersWithUniqueDigits(self, n: int) -> int:
        """
        Let f(n) = count of number with unique digits of length n
        f(1) = 10 (0...9)
        f(2) = 9 * 9 (9 numbers for first choice 1...9 and 9 numbers, excluding already picked, for second choice)
        f(3) = f(2) * 8 (8 numbers left for third number)
        f(4) = f(3) * 7 and so on
        f(11) = f(12) = f(13) = 0, bcs no available unique digits to be picked
        """
        if n == 0:
            return 1

        res = 10
        uniqDigits = 9
        available = 9
        while n > 1 and available > 0:
            uniqDigits = uniqDigits * available
            res += uniqDigits
            available -= 1
            n -= 1
        return res

    def countNumbersWithUniqueDigits2(self, n: int) -> int:
        def count(n, used, d):
            if d == n:  # termination when current number contains n digits, can't add more digits
                return 1
            total = 1  # start as 1 bcs prefix num itself is a valid ans
            i = 1 if d == 0 else 0
            while i <= 9:  # start with 1 then 1x, 1xx,..., 2, 2x, 2xx...
                if not used[i]:
                    used[i] = True
                    total += count(n, used, d + 1)
                    used[i] = False
                i += 1
            return total

        if n > 10: n = 10
        res = [False] * 10
        return count(n, res, 0)


n = 2 # 91 excluding 11,22,33,44,55,66,77,88,99
print(Solution().countNumbersWithUniqueDigits2(n))
