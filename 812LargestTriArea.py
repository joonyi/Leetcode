"""
You have a list of points in the plane.
Return the area of the largest triangle that can be formed by any 3 of the points.

Example:
Input: points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
Output: 2
Explanation:
The five points are show in the figure below. The red triangle is the largest.
"""
class Solution(object):
    def largestTriangleArea(self, points):
        """
        :type points: List[List[int]]
        :rtype: float
        """
        # Shoealace formula
        # Area = 0.5 * abs(x1*y2 + x2*y3 + x3*y1 - x1*y3 - x3*y2 - x2*y1)
        import itertools
        def area(p, q, r):
            return .5 * abs(p[0] * q[1] + q[0] * r[1] + r[0] * p[1]
                            - p[1] * q[0] - q[1] * r[0] - r[1] * p[0])

        # Brute force all possible combinations of points
        return max(area(*triangle)
                   for triangle in itertools.combinations(points, 3))



# Shoealace formula
# Heron formula
# area = 0.5 * a * b * sin(C) and calculate the angle C with trigonometry.
points = [[0,0],[0,1],[1,0],[0,2],[2,0]]
print(Solution().largestTriangleArea(points))