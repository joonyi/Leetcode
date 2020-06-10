"""
Students are asked to stand in non-decreasing order of heights for an annual photo.

Return the minimum number of students not standing in the right positions.
(This is the number of students that must move in order for all students to be standing in non-decreasing order of height.)
"""
class Solution(object):
    def heightChecker(self, heights):
        """
        :type heights: List[int]
        :rtype: int
        """
        cnt = 0
        for i, j in zip(sorted(heights), heights):
            if i != j:
                cnt += 1

        return cnt

heights = [1,1,4,2,1,3]
print(Solution().heightChecker(heights))