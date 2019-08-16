"""
A boomerang is a set of 3 points that are all distinct and not in a straight line.
Given a list of three points in the plane, return whether these points are a boomerang.

Example 1:
Input: [[1,1],[2,3],[3,2]]
Output: true

Example 2:
Input: [[1,1],[2,2],[3,3]]
Output: false
"""
class Solution(object):
    def isBoomerang(self, points):
        """
        :type points: List[List[int]]
        :rtype: bool
        """
        # Check cross product is zero
        # Or, You might notice that if all of these points are on the same straight line,
        # then the triangle will have have an area of 0. Therefore we can check if A, B and C are on
        # a straight line by checking if the area of the triangle they form is 0.
        # (Ax * (By − Cy) + Bx * (Cy − Ay) + Cx * (Ay − By)) / 2
        xi, yi = points[0][0], points[0][1]
        xj, yj = points[1][0], points[1][1]
        xk, yk = points[2][0], points[2][1]
        cross_product = (xj - xi) * (yk - yi) - (xk - xi) * (yj - yi)
        return True if cross_product != 0 else False


# points =  [[1,1],[2,3],[3,2]] #T
points = [[1,1],[2,2],[3,3]] #F
# points = [[0,0],[0,2],[2,1]] # T
print(Solution().isBoomerang(points))