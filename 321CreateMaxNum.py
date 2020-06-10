"""
Given two arrays of length m and n with digits 0-9 representing two numbers.
Create the maximum number of length k <= m + n from digits of the two.
The relative order of the digits from the same array must be preserved.
Return an array of the k digits.

Note: You should try to optimize your time and space complexity.
"""
class Solution(object):
    def maxNumber(self, nums1, nums2, k):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :type k: int
        :rtype: List[int]
        """
        n, m = len(nums1), len(nums2)
        ret = [0] * k
        for i in range(0, k + 1):
            j = k - i
            if i > n or j > m: continue
            left = self.maxSingleNumber(nums1, i)
            right = self.maxSingleNumber(nums2, j)
            num = self.merge2(left, right)
            ret = max(num, ret)
        return ret

    def mergeMax(self, nums1, nums2):
        ans = []
        while nums1 or nums2:
            if nums1 > nums2:
                ans += nums1[0]
                nums1 = nums1[1:]  # remove first element
            else:
                ans += nums2[0]
                nums2 = nums2[1:]  # remove first element
        return ans

    def merge2(self, nums1, nums2):
        return [max(nums1, nums2).pop(0) for _ in nums1 + nums2]

    def maxSingleNumber(self, nums, k):
        drop = len(nums) - k
        out = []
        for num in nums:
            while drop and out and out[-1] < num:
                out.pop()
                drop -= 1
            out.append(num)
        return out[:k]

'''
To create the max number from num1 and nums2 with k elements, we assume the final result 
combined by i numbers (denotes as left) from num1 and j numbers (denotes as right) from nums2, 
where i+j==k.

Obviously, left and right must be the maximum possible number in num1 and num2 respectively. 
i.e. num1 = [6,5,7,1] and i == 2, then left must be [7,1].

The final result is the maximum possible merge of all left and right.

1. iterate i from 0 to k.
2. find max number from num1, num2 by select i , k-i numbers, denotes as left, right
3. find max merge of left, right
'''

nums1 = [3, 4, 6, 5]
nums2 = [9, 1, 2, 5, 8, 3]
k = 5
nums1 = [3, 9]
nums2 = [8, 9]
k = 3
# nums1 = [6,7,5]
# nums2 = [4,8,1]
# k = 3
print(Solution().maxNumber(nums1, nums2, k))
