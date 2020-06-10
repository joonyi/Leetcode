"""
Given a non-negative integer, you could swap two digits at most once to get the maximum valued number.
Return the maximum valued number you could get.
"""


class Solution(object):
    def maximumSwap(self, num):
        """
        :type num: int
        :rtype: int
        """
        # Convert int to list int
        nums = []
        while num > 0:
            nums.append(num % 10)
            num //= 10
        nums = nums[::-1]

        i = 0
        while i < len(nums):
            maxV = max(nums[i:])
            idx = list(reversed(nums[i:])).index(maxV) # find max value occurs the latest
            idx = len(nums) - idx - 1
            if nums[i] != maxV:
                nums[i], nums[idx] = nums[idx], nums[i]
                break
            i += 1

        # Convert list int to int
        res = 0
        for i, x in enumerate(nums):
            x = x * 10**(len(nums)-i-1)
            res += x
        return res

    def maximumSwap2(self, num):
        A = list(map(int, str(num)))
        last = {int(x): i for i, x in enumerate(A)} # max occur latest
        for i, x in enumerate(A):
            for d in range(9, x, -1): # check digit greater down to current number
                if last.get(d, 0) > i: # if this larger number exist in larger index, means can swap to get larger result
                    A[i], A[last[d]] = A[last[d]], A[i]
                    return int("".join(map(str, A)))
        return num


num = 2736
# num = 9973
num = 98368 # 98863
# num = 1993 # expect 9913 not 9193
print(Solution().maximumSwap2(num))