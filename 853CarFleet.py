"""
N cars are going to the same destination along a one lane road.  The destination is target miles away.

Each car i has a constant speed speed[i] (in miles per hour), and initial position position[i] miles
towards the target along the road.

A car can never pass another car ahead of it, but it can catch up to it, and drive bumper to bumper
at the same speed.

The distance between these two cars is ignored - they are assumed to have the same position.

A car fleet is some non-empty set of cars driving at the same position and same speed.  Note that a
single car is also a car fleet.

If a car catches up to a car fleet right at the destination point, it will still be considered as
one car fleet.

How many car fleets will arrive at the destination?
"""

class Solution(object):
    def carFleet(self, target, position, speed):
        """
        :type target: int
        :type position: List[int]
        :type speed: List[int]
        :rtype: int
        """
        time = [float(target - p) / s for p, s in sorted(zip(position, speed))]
        res = cur = 0
        for t in reversed(time):
            if t > cur:
                res += 1
                cur = t
        return res

    def carFleet2(self, target, position, speed):
        res = 0
        timeArr = [0] * target
        for i in range(len(position)):
            timeArr[position[i]] = float(target - position[i]) / speed[i]

        prev = 0.0
        for i in range(target-1,-1,-1):
            cur = timeArr[i]
            if cur > prev:
                prev = cur
                res += 1
        return res

target = 12
position = [10,8,0,5,3]
speed = [2,4,1,1,3]
print(Solution().carFleet2(target,position,speed))