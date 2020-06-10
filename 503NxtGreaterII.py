"""
Given a circular array (the next element of the last element is the first element of the array),
print the Next Greater Number for every element. The Next Greater Number of a number x is the first
greater number to its traversing-order next in the array, which means you could search circularly
to find its next greater number. If it doesn't exist, output -1 for this number.
"""
class Solution(object):
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        N = len(nums)
        res = [None] * N
        stack = [] # invariant of index of next greater element
        for i in range(2*N-1, -1, -1): # pass two times to complete circular traversal
            while stack and nums[stack[-1]] <= nums[i % N]:
                stack.pop()
            res[i % N] = -1 if not stack else nums[stack[-1]]
            stack.append(i%N)
        return res




nums = [1,2,1]
# nums = [5,4,3,2,1]
print(Solution().nextGreaterElements(nums))