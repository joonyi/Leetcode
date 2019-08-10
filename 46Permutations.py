"""
Given a collection of distinct integers, return all possible permutations.
"""
class Solution(object):
    def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def generate_permute(nums, res, j):
            if j == len(nums):
                res.append(nums[:])
                return

            for i in range(j, len(nums)):
                nums[i], nums[j] = nums[j], nums[i]
                generate_permute(nums, res, j + 1)
                nums[j], nums[i] = nums[i], nums[j]

        res = []
        generate_permute(nums, res, 0)
        return res

    def permute2(self, nums):
        import itertools
        return list(itertools.permutations(nums))
        # return map(list, itertools.permutations(nums))

# Can try two idea
# Take any number as the first number and append any permutation of the other numbers.
# Insert the first number anywhere in any permutation of the remaining numbers.

nums = [1,1,2]
print(Solution().permute(nums))
