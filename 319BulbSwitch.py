"""
There are n bulbs that are initially off. You first turn on all the bulbs.
Then, you turn off every second bulb. On the third round, you toggle every third bulb
(turning on if it's off or turning off if it's on). For the i-th round, you toggle every i bulb.
For the n-th round, you only toggle the last bulb. Find how many bulbs are on after n rounds.
As we know that there are n bulbs, let's name them as 1, 2, 3, 4, ..., n.

You first turn on all the bulbs.
Then, you turn off every second bulb.(2, 4, 6, ...)
On the third round, you toggle every third bulb.(3, 6, 9, ...)
For the ith round, you toggle every i bulb.(i, 2i, 3i, ...)
For the nth round, you only toggle the last bulb.(n)

If n > 6, you can find that bulb 6 is toggled in round 2 and 3.
Later, it will also be toggled in round 6, and round 6 will be the last round when bulb 6 is toggled.
Here, 2,3 and 6 are all factors of 6 (except 1).

Prove:
We can come to the conclusion that the bulb i is toggled k times.
Here, k is the number of i's factors (except 1).
k + 1 will be the total number of i's factors
"""

class Solution(object):
    def bulbSwitch(self, n):
        """
        :type n: int
        :rtype: int
        """
        return int(n ** 0.5)



n = 3
print(Solution().bulbSwitch(n))