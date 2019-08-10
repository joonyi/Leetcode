"""
The set [1,2,3,...,n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.
"""

class Solution(object):
    def getPermutation(self, n, k):
        """
        :type n: int
        :type k: int
        :rtype: str
        """
        # TLE
        nums = [i for i in range(1, n + 1)]
        for _ in range(1, k):
            self.NxtPermute(nums)

        return''.join(map(str, nums))


    def NxtPermute(self, nums):
        # permute in place
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


# [1,2,3,...,n]
n, k = 3, 3
print(Solution().getPermutation(n, k))
