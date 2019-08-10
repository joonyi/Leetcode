"""
There are N gas stations along a circular route, where the amount of gas at station i is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from station i
to its next station (i+1). You begin the journey with an empty tank at one of the gas stations.

Return the starting gas station's index if you can travel around the circuit once in the
clockwise direction, otherwise return -1.

Note:
If there exists a solution, it is guaranteed to be unique.
Both input arrays are non-empty and have the same length.
Each element in the input arrays is a non-negative integer.
"""
class Solution(object):
    def canCompleteCircuit(self, gas, cost):
        """
        :type gas: List[int]
        :type cost: List[int]
        :rtype: int
        """
        starts = []
        for i in range(len(gas)):
            if gas[i] >= cost[i]:
                starts.append(i)

        for start in starts:
            i = start
            tank = gas[i]
            while True:
                tank -= cost[i]
                if tank < 0:
                    break
                i = (i + 1) % len(gas)
                if i == start:
                    return i
                tank += gas[i]

        return -1

    def canCompleteCircuit2(self, gas, cost):
        start, total, tank = 0, 0, 0
        for i in range(len(gas)):
            tank += gas[i] - cost[i]
            if tank < 0:
                start = i + 1
                total += tank
                tank = 0
        return start if total + tank >= 0 else -1

# gas  = [1,2,3,4,5] # 3
# cost = [3,4,5,1,2]
# gas  = [2,3,4] # -1
# cost = [3,4,3]
# gas = [4] # -1
# cost = [5]
gas = [5,1,2,3,4] # expect 4
cost = [4,4,1,5,1]
# gas = [4,5,2,6,5,3] # -1
# cost = [3,2,7,3,2,9]
# gas = [4,5,3,1,4] # -1
# cost = [5,4,3,4,2]
# gas = [2]
# cost = [2]
print(Solution().canCompleteCircuit2(gas, cost))
