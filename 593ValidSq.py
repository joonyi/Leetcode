"""
Given the coordinates of four points in 2D space, return whether the four points could construct a square.
The coordinate (x,y) of a point is represented by an integer array with two integers.

Note:
All the input integers are in the range [-10000, 10000].
A valid square has four equal sides with positive length and four equal angles (90-degree angles).
Input points have no order.
"""

from typing import List
class Solution:
    def validSquare(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        points = [p1, p2, p3, p4]
        d = {}
        for i in range(len(points) - 1):
            for j in range(i + 1, len(points)):
                x = (points[i][0] - points[j][0]) ** 2
                y = (points[i][1] - points[j][1]) ** 2
                d[x + y] = d.get(x + y, 0) + 1

        k, v = d.keys(), sorted(d.values())
        return len(k) == 2 and v[0] == 2 and v[1] == 4

    def validSquare2(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def distance(p1, p2):
            return (p1[0] - p2[0]) * (p1[0] - p2[0]) + (p1[1] - p2[1]) * (p1[1] - p2[1])
        d = {distance(p1, p2), distance(p1, p3), distance(p1, p4), distance(p2, p3),
                distance(p2, p4), distance(p3, p4)}

        return list(d).count(0) == 0 and len(d) == 2

    def validSquare3(self, p1: List[int], p2: List[int], p3: List[int], p4: List[int]) -> bool:
        def dist(p1, p2):
            return (p2[0] - p1[0]) * (p2[0] - p1[0]) + (p2[1] - p1[1]) * (p2[1] - p1[1])
        def check(p1, p2, p3, p4):
            return dist(p1, p2) > 0 and dist(p1, p2) == dist(p2, p3) and \
                   dist(p2, p3) == dist(p3, p4) and dist(p3, p4) == dist(p4, p1) and \
                   dist(p1, p3) == dist(p2, p4)
        return check(p1, p2, p3, p4) or check(p1, p3, p2, p4) or check(p1, p2, p4, p3)



p1, p2, p3, p4 = [0,0], [1,1], [1,0], [0,1]  # T
# p1, p2, p3, p4 = [1,1], [5,3], [3,5], [7,7]  # F
# p1, p2, p3, p4 = [0,0], [1,1], [0,0], [0,0]  # F
print(Solution().validSquare2(p1, p2, p3, p4))
