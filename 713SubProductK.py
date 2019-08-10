"""
Your are given an array of positive integers nums.

Count and print the number of (contiguous) subarrays where the product of all the elements
in the subarray is less than k.
"""
class Solution(object):
    def numSubarrayProductLessThanK(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        # Prefix product TLE
        prefix = [1]
        for n in nums:
            prefix.append(prefix[-1] * n)
        cnt = 0
        for i in range(1, len(prefix)):
            if prefix[i] < k:
                cnt += 1
            for j in range(1, i):
                if prefix[i] // prefix[j] < k:
                    cnt += 1
        return cnt

    def numSubarrayProductLessThanK2(self, nums, k):
        # sliding window
        if k <= 1: return 0
        prod = 1
        ans = left = 0
        for right, val in enumerate(nums):
            prod *= val
            while prod >= k:
                prod //= nums[left]
                left += 1
            ans += right - left + 1
        return ans

    def numSubarrayProductLessThanK3(self, nums, k):
        # Bcs log(product x) equals to sum of log(x), transform from subarray product to subarray sum
        import math, bisect
        if k == 0: return 0
        k = math.log(k)

        prefix = [0]
        for x in nums:
            prefix.append(prefix[-1] + math.log(x))

        ans = 0
        for i, x in enumerate(prefix):
            j = bisect.bisect(prefix, x + k - 1e-9, i + 1)

            ans += j - i - 1
        return ans



nums, k = [10,5,2,6], 100
print(Solution().numSubarrayProductLessThanK3(nums, k))