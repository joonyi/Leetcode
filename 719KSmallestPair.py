"""
Given an integer array, return the k-th smallest distance among all the pairs.
The distance of a pair (A, B) is defined as the absolute difference between A and B.

Example 1:
Input:
nums = [1,3,1]
k = 1
Output: 0

Explanation:
Here are all the pairs:
(1,3) -> 2
(1,1) -> 0
(3,1) -> 2
Then the 1st smallest distance pair is (1,1), and its distance is 0.
"""
# Counting sort
# time O(n^2)
# space O(max(nums))
class Solution:
    def smallestDistancePair(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: int
        """
        N = 1000000
        count = [0] * N
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                count[abs(nums[i] - nums[j])] += 1

        sum = 0
        for i in range(N+1):
            sum += count[i]
            if sum >= k:
                return i

    # space O(1)
    # time O(nlog(max(n,nums)))
    def smallestDistancePair2(self, nums, k):
        nums.sort()
        n = len(nums)
        left = 0
        right = nums[-1] - nums[0]
        track = []
        while left < right:
            count = 0
            mid = left + (right - left)//2
            j = 0
            for i in range(n):
                while j < n and nums[j] - nums[i] <= mid:
                    j += 1
                count += j - i - 1

            # if count >= k: # Both works
            #     right = mid
            # else:
            #     left = mid + 1

            if count < k:
                left = mid + 1
            else:
                right = mid

        return left

nums = [1,2,6]
k = 3
print(Solution().smallestDistancePair2(nums,k))
