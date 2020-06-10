"""
Given n non-negative integers representing an elevation map where the width of each bar is 1, compute how much
water it is able to trap after raining.
"""
class Solution(object):
    def trap(self, height):
        """
        :type height: List[int]
        :rtype: int
        """
        if not height:
            return 0
        res = 0
        n = len(height)
        left_max = [0] * n # max height of bar from this idx to the left
        right_max = [0] * n # max height of bar from this idx to the right
        left_max[0] = height[0]
        right_max[n - 1] = height[n - 1]
        for i in range(1, n):
            left_max[i] = max(height[i], left_max[i - 1])
        for i in range(n - 2, -1, -1):
            right_max[i] = max(height[i], right_max[i + 1])
        for i in range(1, n - 1):
            res += min(left_max[i], right_max[i]) - height[i] # trap water as high as the smaller bar
        return res

    def trap2(self, height):
        res = i = 0
        stack = []
        while i < len(height):
            while stack and height[i] > height[stack[-1]]: # when current height taller than in stack, this is a right bar
                top = stack.pop()
                if not stack: # if popping one element make stack empty, this is a left bar
                    break
                distance = i - stack[-1] - 1 # top of stack is index of left bar
                bounded_height = min(height[i], height[stack[-1]]) - height[top]
                res += distance * bounded_height
            stack.append(i)
            i += 1
        return res

    def trap3(self, height):
        # two pointer
        res = left = 0
        right = len(height) - 1
        left_max = right_max = 0
        while left < right:
            if height[left] < height[right]: # a taller bar exists on left pointer's right side
                if height[left] >= left_max: # but greater than left tallest bar, so can't contain water
                    left_max = height[left] # update left tallest bar
                else:
                    res += left_max - height[left] # and smaller than left bar, so can contain water
                left += 1

            else: # a taller bar exists on right pointer's left side
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    res += right_max - height[right]
                right -= 1
        return res

    def trap4(self, height):
        # Keep track of the already safe level and the total water so far.
        # In each step, process and discard the lower one of the leftmost or rightmost elevation.
        left, right = 0, len(height) - 1
        level, water = 0, 0
        while left < right:
            if height[left] < height[right]:
                lower = height[left]
                left += 1
            else:
                lower = height[right]
                right -= 1
            level = max(level, lower)
            water += level - lower
        return water

height = [0,1,0,2,1,0,1,3,2,1,2,1] # 6
print(Solution().trap4(height))
