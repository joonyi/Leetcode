"""
You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point.
Check if these points make a straight line in the XY plane.

Constraints:
a) 2 <= coordinates.length <= 1000
b) coordinates[i].length == 2
c) -10^4 <= coordinates[i][0], coordinates[i][1] <= 10^4
d) coordinates contains no duplicate point.
"""

class Solution(object):
    def checkStraightLine(self, coordinates):
        """
        :type coordinates: List[List[int]]
        :rtype: bool
        """
        if len(coordinates) == 2:
            return True

        x0, y0 = coordinates[0][0], coordinates[0][1]
        x1, y1 = coordinates[1][0], coordinates[1][1]
        for i in range(2, len(coordinates)):
            x2, y2 = coordinates[i][0], coordinates[i][1]
            # this can also see as if two slopes are the same
            cross_prod = ((x1-x0) * (y2-y0)) - ((x2-x0) * (y1-y0))
            if cross_prod != 0:
                return False

        return True

coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
coordinates = [[1,1],[2,2],[3,4],[4,5],[5,6],[7,7]]
print(Solution().checkStraightLine(coordinates))
