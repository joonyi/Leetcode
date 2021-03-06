"""
Given n non-negative integers a1, a2, ..., an , where each represents a point at coordinate (i, ai).
n vertical lines are drawn such that the two endpoints of line i is at (i, ai) and (i, 0).
Find two lines, which together with x-axis forms a container, such that the container contains the most water.

Note: You may not slant the container and n is at least 2.
"""
class Solution(object):
    def maxArea(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        # Brute Force
        maxA = 0
        for i in range(len(height)):
            for j in range(i + 1, len(height)):
                maxA = max(maxA, min(height[i], height[j]) * (j - i))
        return maxA

    def maxArea2(self, height):
        left = 0
        right = len(height) -  1 # start with the widest container
        result = 0
        while left < right:
            result = max(result, (right - left) * min(height[left], height[right]))
            if height[left] < height[right]: # this is already the largest container left one can form, so no need to consider again
                left += 1
            else:
                right -= 1

        return result


height = [1,8,6,2,5,4,8,3,7] # 49
print(Solution().maxArea2(height))