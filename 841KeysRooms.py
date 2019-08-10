"""
There are N rooms and you start in room 0.  Each room has a distinct number in 0, 1, 2, ..., N-1,
and each room may have some keys to access the next room.

Formally, each room i has a list of keys rooms[i], and each key rooms[i][j]
is an integer in [0, 1, ..., N-1] where N = rooms.length.  A key rooms[i][j] = v
opens the room with number v.

Initially, all the rooms start locked (except for room 0).
You can walk back and forth between rooms freely.
Return true if and only if you can enter every room.
"""

class Solution(object):
    def canVisitAllRooms(self, rooms):
        """
        :type rooms: List[List[int]]
        :rtype: bool
        """
        visit = [0] * len(rooms)

        def dfs_visit(rooms, i):
            if visit[i] == 0:
                visit[i] = 1
                for next in rooms[i]:
                    dfs_visit(rooms, next)

        dfs_visit(rooms, 0)
        return 0 not in visit

    def canVisitAllRooms2(self, rooms):
        visit = [0] * len(rooms)
        visit[0] = 1 # Always start from room 0
        queue = [0]
        while queue:
            node = queue.pop(0)
            for next in rooms[node]:
                if visit[next] == 0:
                    visit[next] = 1
                    queue.append(next)

        return 0 not in visit

# A = [[1],[2],[3],[]]
A = [[1,3],[3,0,1],[2],[0]]
print(Solution().canVisitAllRooms2(A))