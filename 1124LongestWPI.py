"""
We are given hours, a list of the number of hours worked per day for a given employee.

A day is considered to be a tiring day if and only if the number of hours worked is (strictly)
greater than 8.

A well-performing interval is an interval of days for which the number of tiring days is strictly
larger than the number of non-tiring days.

Return the length of the longest well-performing interval.
"""

from typing import List
class Solution:
    def longestWPI(self, hours: List[int]) -> int:
        res = score = 0
        seen = {}
        for i, h in enumerate(hours):
            score = score + 1 if h > 8 else score - 1
            if score > 0:
                res = i + 1
            seen.setdefault(score, i)
            if score - 1 in seen:
                res = max(res, i - seen[score - 1])
        return res


    def longestWPI2(self, hours: List[int]) -> int:
        N = len(hours)
        prefixSum = [0] * (N + 1)
        for i in range(1, N + 1):
            score = 1 if hours[i - 1] > 8 else -1
            prefixSum[i] = prefixSum[i - 1] + score

        smdStack = [] # strick monotone decreasing
        for i in range(N + 1):
            if not smdStack or (prefixSum[smdStack[-1]] > prefixSum[i]):
                smdStack.append(i)

        res = 0
        for j in range(N, -1, -1):
            # for generalized problem
            # while smdStack and prefixSum[smdStack[-1]] + K <= prefixSum[j]
            while smdStack and prefixSum[smdStack[-1]] < prefixSum[j]:
                res = max(res, j - smdStack[-1])
                smdStack.pop()

        return res


"""
Explanation
We starts with a score = 0,
If the working hour > 8, we plus 1 point.
Otherwise we minus 1 point.
We want find the maximum interval that have strict positive score.

After one day of work, if we find the total score > 0,
the whole interval has positive score,
so we set res = i + 1.

If the score is a new lowest score, we record the day by seen[cur] = i.
seen[score] means the first time we see the score is seen[score]th day.

We want a positive score, so we want to know the first occurrence of score - 1.
score - x also works, but it comes later than score - 1.
So the maximum interval is i - seen[score - 1]

"""

"""
(Monotone stack are just normal stack with a constraint that the elements in them are 
monotonically increasing or decreasing. When processing a new element, 
we either pop top elements then push new elem or discard this new element to guarantee 
the property of monotonicity. If you are not familiar with this data structure, 
you'd better solve some similar leetcode problems before this one).
"""


hours = [9,9,6,0,6,6,9] # 3 The longest well-performing interval is [9,9,6]
print(Solution().longestWPI2(hours))