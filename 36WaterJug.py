"""
You are given two jugs with capacities x and y litres. There is an infinite amount of
water supply available. You need to determine whether it is possible to measure exactly z litres
using these two jugs.

If z liters of water is measurable, you must have z liters of water contained within one
or both buckets by the end.

Operations allowed:
- Fill any of the jugs completely with water.
- Empty any of the jugs.
- Pour water from one jug into another till the other jug is completely full or the first
jug itself is empty.
"""


class Solution:
    def canMeasureWater(self, x: int, y: int, z: int) -> bool:
        def gcd(a, b):
            while b > 0:
                a, b = b, a % b
            return a

        if x + y < z:
            return False
        if x == z or y == z or x + y == z:
            return True

        g = gcd(x, y)
        return z % gcd(x, y) == 0

    def canMeasureWater2(self, x: int, y: int, z: int) -> bool:
        if x > y:  # swap
            x, y = y, x

        if z > x + y:
            return False

        # set the initial state will empty jars;
        queue = [(0, 0)]
        visited = {(0, 0)}
        while len(queue) > 0:
            a, b = queue.pop(0)
            if a + b == z:
                return True

            states = set()

            states.add((x, b))  # fill jar x;
            states.add((a, y))  # fill jar y;
            states.add((0, b))  # empty jar x;
            states.add((a, 0))  # empty jar y;
            states.add((min(x, b + a), 0 if b < x - a else b - (x - a)))  # pour jar y to x;
            states.add((0 if a + b < y else a - (y - b), min(b + a, y)))  # pour jar x to y;

            for state in states:
                if state in visited:
                    continue
                queue.append(state)
                visited.add(state)

        return False

"""
x = 4, y = 6, z = 8.

GCD(4, 6) = 2
8 is multiple of 2

so this input is valid and we have:
-1 * 4 + 6 * 2 = 8

In this case, there is a solution obtained by filling the 6 gallon jug twice and 
emptying the 4 gallon jug once. (Solution. Fill the 6 gallon jug and empty 4 gallons 
to the 4 gallon jug. Empty the 4 gallon jug. Now empty the remaining two gallons from 
the 6 gallon jug to the 4 gallon jug. Next refill the 6 gallon jug. This gives 8 gallons in the end)
"""

x, y, z = 3, 5, 4  # T
# x, y, z = 4, 6, 8  # T
print(Solution().canMeasureWater(x, y, z))

