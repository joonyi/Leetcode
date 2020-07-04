"""
There are a number of spherical balloons spread in two-dimensional space.
For each balloon, provided input is the start and end coordinates of the horizontal diameter.
Since it's horizontal, y-coordinates don't matter and hence the x-coordinates of start and end
of the diameter suffice. Start is always smaller than end. There will be at most 104 balloons.

An arrow can be shot up exactly vertically from different points along the x-axis.
A balloon with xstart and xend bursts by an arrow shot at x if xstart ≤ x ≤ xend.
There is no limit to the number of arrows that can be shot. An arrow once shot keeps
travelling up infinitely. The problem is to find the minimum number of arrows that must be
shot to burst all balloons.
"""

from typing import List
class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        end = float('-inf')
        arrow = len(points)  # if all non-overlap, one arrow for one balloon
        points = sorted(points, key=lambda i: i[1])
        for point in points:
            if point[0] > end:  # start of current larger than end of previous means non-overlap
                end = point[1]
            else:  # else overlap, one arrow saved
                arrow -= 1
        return arrow

    def findMinArrowShots2(self, points):
        points = sorted(points, key=lambda x: x[1])
        arrow, end = 0, -float('inf')
        for interval in points:
            if interval[0] > end:  # greedily shoot the arrow when balloons found
                arrow += 1
                end = interval[1]
        return arrow



# points = [[10,16], [2,8], [1,6], [7,12]]  # 2
# points = [[1,2],[1,2],[1,2]] # 1
points = [[1,2],[1,2],[1,2], [2,3], [3,4]] # 2
print(Solution().findMinArrowShots2(points))
