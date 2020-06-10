"""
Given a positive 32-bit integer n, you need to find the smallest 32-bit integer which has
exactly the same digits existing in the integer n and is greater in value than n.
If no such positive 32-bit integer exists, you need to return -1.
"""

class Solution(object):
    def nextGreaterElement(self, n):
        """
        :type n: int
        :rtype: int
        """
        # num = n
        # nums = []
        # while num > 0:
        #     nums.append(num % 10)
        #     num //= 10
        # nums = nums[::-1]
        nums = list(map(int, str(n))) # same result as above

        i = k = len(nums) - 1
        while i > 0 and nums[i - 1] >= nums[i]:
            i -= 1
        j = i
        while j < k:
            nums[j], nums[k] = nums[k], nums[j]
            j += 1
            k -= 1
        if i > 0:
            i -= 1
            k = i
            while nums[k] <= nums[i]:
                k += 1
            nums[i], nums[k] = nums[k], nums[i]

        res = int(''.join(map(str, nums)))
        if res > n and res < 2**31 - 1:
            return int(res)
        return -1

    def nextGreaterElement2(self, n):
        s = list(map(int, str(n)))
        i = len(s) - 1
        while i - 1 >= 0 and s[i] <= s[i - 1]:
            i -= 1

        if i == 0:
            return -1

        j = i
        while j + 1 < len(s) and s[j + 1] > s[i - 1]:
            j += 1

        s[i - 1], s[j] = s[j], s[i - 1]
        s[i:] = reversed(s[i:])
        ret = int(''.join(map(str, s)))

        return ret if ret <= ((1 << 31) - 1) else -1

# Idea from next permutation
# Traverse the number from rightmost digit till a digit smaller than previous traversed digit
# Ex 534976, stop at 4. if not such digit exists, output -1
# At the right side of 4, look for smallest digit greater than 4.
# Swap 4 and 6, then reverse the digit from d to right most
n = 230241
n = 2147483647
print(Solution().nextGreaterElement2(n))