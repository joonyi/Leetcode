"""
Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.
"""


class Solution(object):
    def largestRectangleArea(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        N = len(heights)
        stack = []
        prev = [None] * N  # previous less element
        for i in range(N):
            while stack and heights[i] <= heights[stack[-1]]:
                stack.pop()
            prev[i] = stack[-1] if stack else -1
            stack.append(i)

        stack = []
        next_ = [None] * N
        for k in range(N - 1, -1, -1):
            while stack and heights[k] < heights[stack[-1]]:
                stack.pop()
            next_[k] = stack[-1] if stack else N
            stack.append(k)


        maxArea = 0
        for i in range(N):
            maxArea = max(maxArea, heights[i] * (next_[i] - prev[i] - 1))
        return maxArea

    def largestRectangleArea2(self, heights):
        # Same algorithm as above, just another way to write
        if not heights:
            return 0
        N = len(heights)
        lessFromLeft = [None] * N
        lessFromRight = [None] * N
        lessFromRight[N - 1] = N
        lessFromLeft[0] = -1

        for i in range(1, N):
            p = i - 1
            while p >= 0 and heights[p] >= heights[i]:
                p = lessFromLeft[p]
            lessFromLeft[i] = p

        for i in range(N - 2, -1, -1):
            p = i + 1
            while p < N and heights[p] >= heights[i]:
                p = lessFromRight[p]
            lessFromRight[i] = p

        maxArea = 0
        for i in range(N):
            maxArea = max(maxArea, heights[i] * (lessFromRight[i] - lessFromLeft[i] - 1))

        return maxArea

    def largestRectangleArea3(self, heights):
        N = len(heights)
        stack = [] # keep index of previous lesser element
        maxArea = 0
        for i in range(N + 1):
            h = 0 if i == N else heights[i] # if nums is monotone increasing, pop out when length reached
            while stack and h < heights[stack[-1]]:
                curHeight = heights[stack.pop()]
                preIndex = -1 if not stack else stack[-1]
                area = curHeight * (i - preIndex - 1)
                maxArea = max(maxArea, area)
            stack.append(i)

        return maxArea



nums = [2,1,5,6,2,3]
# nums = [1,2,3,4,5]
print(Solution().largestRectangleArea3(nums))