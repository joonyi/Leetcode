"""
In a row of seats, 1 represents a person sitting in that seat, and 0 represents that the seat is empty.

There is at least one empty seat, and at least one person sitting.

Alex wants to sit in the seat such that the distance between him and the closest person to him
is maximized.

Return that maximum distance to closest person.
"""
class Solution(object):
    def maxDistToClosest(self, seats):
        """
        :type seats: List[int]
        :rtype: int
        """
        res = [float('inf')] * len(seats)
        dist = float('inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                res[i] = 0
                dist = 0
            else:
                res[i] = dist
            dist += 1

        # Backpropagation...lol
        for i in range(len(seats)-1, -1, -1):
            if seats[i] == 1:
                res[i] = 0
                dist = 0
            else:
                res[i] = min(res[i], dist)
            dist += 1

        return max(res)

    def maxDistToClosest2(self, seats):
        import itertools
        ans = 0
        for seat, group in itertools.groupby(seats): # groupby return consecutive number in list
            if not seat:
                K = len(list(group))
                ans = max(ans, (K + 1) // 2)

        return max(ans, seats.index(1), seats[::-1].index(1))

    def maxDistToClosest3(self, seats):
        prev = None
        res = -float('inf')
        for i in range(len(seats)):
            if seats[i] == 1:
                if prev == None:
                    res = i
                else:
                    res = max(res, (i - prev) // 2)
                prev = i
        res = max(res, len(seats) - 1 - prev)
        return res

# Another idea, last is the index of last seated seat.
# Loop on all seats, when we met a people, we count the distance from the last.
# The final result = max(distance at the beginning, distance in the middle / 2, distance at the end).

seats = [1,0,0,0,1,0,1]
# seats = [1,0,0,0]
print(Solution().maxDistToClosest3(seats))