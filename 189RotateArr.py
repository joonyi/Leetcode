class Solution(object):
    def rotate(self, nums, k):
        """
        :type nums: List[int]
        :type k: int
        :rtype: None Do not return anything, modify nums in-place instead.
        """
        # Time Limit Exceeded, O(n^2)
        for _ in range(k):
            tmp = nums[-1]
            for i in range(len(nums)-1):
                nums[-1-i] = nums[-2-i]
            nums[0] = tmp

        return nums

    def rotate2(self, nums, k):
        first = nums[:len(nums)-k]
        last = nums[len(nums)-k:]
        nums[:k+1] = last
        nums[k:] = first
        print(nums)

    # Actually same as above
    def rotate3(self, nums, k):
        k = k % len(nums)
        nums[:] = nums[len(nums) - k:] + nums[:len(nums) - k]
        print(nums)

    def rotate4(self, nums, k):
        # Need to do the math here, mainly how to swap correctly
        n, k, j = len(nums), k % len(nums), 0
        while n > 0 and k % n != 0:
            for i in range(0, k):
                nums[j + i], nums[len(nums) - k + i] = nums[len(nums) - k + i], nums[j + i]  # swap
            n, j = n - k, j + k
            k = k % n

"""
Another idea: using reverse
Original List                   : 1 2 3 4 5 6 7
After reversing all numbers     : 7 6 5 4 3 2 1
After reversing first k numbers : 5 6 7 4 3 2 1
After revering last n-k numbers : 5 6 7 1 2 3 4 --> Result

Another idea: store a temp number and put the number directly into correct place
O(n)
"""

nums =  [-1,-100,3,99] # [3,99,-1,-100]
k = 2
nums, k = [1,2,3,4,5,6,7], 3
Solution().rotate4(nums,k)