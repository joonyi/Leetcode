"""
Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's
and return its area.
"""


class Solution(object):
    def maximalRectangle(self, matrix):
        """
        :type matrix: List[List[str]]
        :rtype: int
        """
        # take each row as histogram and accumulate the area, find their max
        if len(matrix) == 0:
            return 0
        m, n = len(matrix), len(matrix[0])
        heights = [0] * n
        maxArea = -1
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '0':
                    heights[j] = 0
                else:
                    heights[j] += 1
            area = self.largestRectangleArea(heights)
            maxArea = max(maxArea, area)
        return maxArea

    def largestRectangleArea(self, heights):
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

    def maximalRectangle2(self, matrix):
        if not matrix:
            return 0
        m, n = len(matrix), len(matrix[0])
        left = [0] * n # left boundary
        right = [n] * n # right boundary
        height = [0] * n # height * (right - left) = area
        maxA = 0
        for i in range(m):
            cur_left, cur_right = 0, n
            for j in range(n):
                if matrix[i][j] == '1':
                    height[j] += 1
                else:
                    height[j] = 0

            for j in range(n):
                if matrix[i][j] == '1':
                    left[j] = max(left[j], cur_left)
                else:
                    left[j] = 0
                    cur_left = j + 1

            for j in range(n-1, -1, -1):
                if matrix[i][j] == '1':
                    right[j] = min(right[j], cur_right)
                else:
                    right[j] = n
                    cur_right = j

            for j in range(n):
                maxA = max(maxA, (right[j] - left[j]) * height[j])

        return maxA



matrix = [
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
# matrix = [["0"]]
print(Solution().maximalRectangle2(matrix))