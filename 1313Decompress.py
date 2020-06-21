"""
We are given a list nums of integers representing a list compressed with run-length encoding.

Consider each adjacent pair of elements [freq, val] = [nums[2*i], nums[2*i+1]] (with i >= 0).
For each such pair, there are freq elements with value val concatenated in a sublist.
Concatenate all the sublists from left to right to generate the decompressed list.

Return the decompressed list.
"""

class Solution(object):
    def decompressRLElist(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = []
        for i in range(0, len(nums), 2):
            res += [nums[i + 1]] * nums[i]
        return res

    def decompressRLElist2(self, A):
        return [x for a, b in zip(A[0::2], A[1::2]) for x in [b] * a]
        # return [nums[i + 1] for i in range(0, len(nums), 2) for _ in range(nums[i])]

nums = [1,2,3,4]
# nums = [1,1,2,3]
print(Solution().decompressRLElist2(nums))