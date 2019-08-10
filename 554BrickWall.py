"""
There is a brick wall in front of you. The wall is rectangular and has several rows of bricks.
The bricks have the same height but different width. You want to draw a vertical line from the
top to the bottom and cross the least bricks.

The brick wall is represented by a list of rows. Each row is a list of integers representing
the width of each brick in this row from left to right.

If your line go through the edge of a brick, then the brick is not considered as crossed.
You need to find out how to draw the line to cross the least bricks and return the number
of crossed bricks.

You cannot draw a line just along one of the two vertical edges of the wall, in which case
the line will obviously cross no bricks.
"""


class Solution(object):
    def leastBricks(self, wall):
        """
        :type wall: List[List[int]]
        :rtype: int
        """
        space, row = 0, []
        interstice = {}
        for i, bricks in enumerate(wall):
            for j in range(len(bricks)-1):
                space += bricks[j]
                row.append(space)
                interstice[space] = interstice.get(space, 0) + 1

            space, row = 0, []

        max_now = 0
        for space, count in interstice.items():
            if count > max_now:
                max_now = count

        return len(wall) - max_now

wall = [[1,2,2,1],
        [3,1,2],
        [1,3,2],
        [2,4],
        [3,1,2],
        [1,3,1,1]]
print(Solution().leastBricks(wall))