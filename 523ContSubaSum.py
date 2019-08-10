"""
Given a list of non-negative numbers and a target integer k, write a function to check if the array
has a continuous subarray of size at least 2 that sums up to the multiple of k, that is,
sums up to n*k where n is also an integer.
"""


class Solution(object):
    def checkSubarraySum(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: bool
        """
        # Since the size of subarray is at least 2.
        if len(nums) <= 1: return False
        # Two continuous "0" will form a subarray which has sum = 0. 0 * k == 0 will always be true.
        for i in range(len(nums)-1):
            if nums[i] == 0 and nums[i+1] == 0:
                return True
        # At this point, k can't be "0" any longer.
        if k == 0: return False
        # Let's only check positive k. Because if there is a n makes n * k = sum, it is always true -n * -k = sum.
        if k < 0:
            k = -k

        for i in range(len(nums)):
            total = nums[i]
            j = i + 1
            while j < len(nums):
                total += nums[j]
                if total % k == 0:
                    return True
                j += 1

        return False

    def checkSubarraySum2(self, A, k):
        P = [0] 
        for x in A:
            v = P[-1] + x
            if k: v %= abs(k)
            P.append(v)

        seen = set()
        for i in range(len(P) - 3, -1, -1):
            seen.add(P[i + 2])
            if P[i] in seen:
                return True
        return False


nums = [23, 2, 4, 6, 7]
k = 6
# nums = [23, 2, 6, 4, 7]
# k = 6
# nums = [23,2,6,4,7] # False
# k = 0
# nums = [0,0] # true
# k = 0
# nums = [0] # false
# k = 0
# nums = [0] # False
# k = -1
# nums = [5,0,0]
# k = 0
print(Solution().checkSubarraySum2(nums, k))
"""
In short, start with mod =0, then we always do mod = (mod+nums[i])%k, if mod repeats, that means between these two mod = x occurences the sum is multiple of k.
Math: c = a % k, c = b % k, so we have a % k = b % k.
Where a is the mod at i and b is the mod at j and a <= b, i < j, because all nums are non-negative. And c is the mod that repeats.
Suppose b-a=d, then we have b % k = ((a+d) % k)%k = (a%k + d%k)%k
In order to make the equation valid: a % k = (a%k + d%k)%k
d%k has to be 0, so d, the different between b and a, is a multiple of k
Example:
[23, 2, 1, 6, 7] k=9
mod = 5, 7, 8, 5 <-- at here we found it
"""