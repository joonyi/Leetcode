class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time Limit Exceeded
        for _ in range(k):
            tmp = nums[-1]
            for i in range(len(nums)-1):
                nums[-1-i] = nums[-2-i]
            nums[0] = tmp

        return nums

    def rotate2(self, nums, k):
        first = nums[:k+1]
        last = nums[k+1:]
        s = last + first
        nums[k:] = first
        nums[:k] = last
# Not working

        print(nums,s)

nums =  [-1,-100,3,99]
k = 2
Solution().rotate2(nums,k)