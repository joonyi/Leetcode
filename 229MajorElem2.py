"""
Given an integer array of size n, find all elements that appear more than n/3 times.

Note: The algorithm should run in linear time and in O(1) space.

Example 1:
Input: [3,2,3]
Output: [3]

Example 2:
Input: [1,1,1,3,3,2,2,2]
Output: [1,2]
"""
import collections
class Solution(object):
    def majorityElement(self, nums):
        dict = {}
        ret = []
        for num in nums:
            if num not in dict:
                dict[num] = 0
            else:
                dict[num] += 1

            if dict[num] == len(nums) // 3:
                ret.append(num)

        return ret

    # Boyer-Moore Majority Vote
    def majorityElement2(self, nums):
        ctr = collections.Counter()
        for n in nums:
            ctr[n] += 1
            if len(ctr) == 3:
                ctr -= collections.Counter(set(ctr))
        return [n for n in ctr if nums.count(n) > len(nums) / 3]

input = [1,1,1,3,3,2,2,2]
print(Solution().majorityElement2(input))