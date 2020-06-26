"""
There is a list of sorted integers from 1 to n. Starting from left to right,
remove the first number and every other number afterward until you reach the end of the list.

Repeat the previous step again, but this time from right to left,
remove the right most number and every other number from the remaining numbers.

We keep repeating the steps again, alternating left to right and right to left,
until a single number remains.

Find the last number that remains starting with a list of length n.
"""


class Solution:
    def lastRemaining(self, n: int) -> int:
        # TLE
        nums = list(range(1, n + 1))
        while len(nums) > 1:
            nums = nums[1::2]
            nums = nums[::-1]
        return nums[0]

    def lastRemaining2(self, n: int) -> int:
        left = True  # when delete from left
        step, head = 1, 1
        while n > 1:
            if left or n % 2 == 1:
                """
                Head is updated when
                1. delete form left
                2. delete from right and odd remaining number
                like 2 4 6 8 10, move from 10, take out 10, 6 and 2, head is deleted and move to 4
                like 2 4 6 8 10 12, move from 12, take out 12, 8, 4, head is still remaining 2
                """
                head = head + step
            n  //= 2  # every time half numbers remain
            step = step * 2
            left = not left
        return head


n = 9  # 6
# n = 1  # 1
n = 100000000  # 32896342
print(Solution().lastRemaining2(n))
