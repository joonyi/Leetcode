"""
Given a positive integer num consisting only of digits 6 and 9.

Return the maximum number you can get by changing at most one digit (6 becomes 9, and 9 becomes 6).
"""
class Solution:
    def maximum69Number (self, num: int) -> int:
        n = num
        max_6 = cnt = -1
        while n > 0:
            cnt += 1
            if n % 10 == 6:
                max_6 = cnt
            n //= 10

        if max_6 == -1:
            return num
        else:
            return num - 6 * 10**max_6 + 9 * 10**max_6

    def maximum69Number2(self, num: int) -> int:
        return int(str(num).replace('6', '9', 1))


# num = 9669
# num = 9996
num = 9999
print(Solution().maximum69Number(num))