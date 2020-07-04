"""
Given a string path, where path[i] = 'N', 'S', 'E' or 'W', each representing moving one unit
north, south, east, or west, respectively. You start at the origin (0, 0) on a 2D plane and
walk on the path specified by path.

Return True if the path crosses itself at any point, that is, if at any time you are on a
location you've previously visited. Return False otherwise.
"""

class Solution:
    def isPathCrossing(self, path: str) -> bool:
        x, y = 0, 0
        coordinates = {(x, y)}
        for d in path:
            if d == "N":
                y += 1
            elif d == "E":
                x += 1
            elif d == "S":
                y -= 1
            else:
                x -= 1

            if (x, y) in coordinates:
                return True
            else:
                coordinates.add((x, y))

        return False


path = "NES"  # False
# path = "NESWW"  # True
path = "NNSWWEWSSESSWENNW"  # True
print(Solution().isPathCrossing(path))
