"""
Given a collection of intervals, find the minimum number of intervals you need to
remove to make the rest of the intervals non-overlapping.
"""
from typing import List
class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        # Get the maximum of non-overlapping intervals
        # Total intervals minus max non-overlap is min of overlap
        if not intervals: return 0
        intervals.sort(key=lambda x: x[1])
        end = intervals[0][1]
        cnt = 1
        for i in range(1, len(intervals)):
            if intervals[i][0] >= end:  # Find non-overlap
                end = intervals[i][1]  # update previous non-overlap end
                cnt += 1

        return len(intervals) - cnt

    def eraseOverlapIntervals2(self, intervals):
        # Which interval would be the best first (leftmost) interval to keep?
        # One that ends first, as it leaves the most room for the rest
        end = float('-inf')
        erased = 0
        intervals = sorted(intervals, key=lambda i: i[1])
        for interval in intervals:
            if interval[0] >= end:  # start of current larger than end of previous means non-overlap
                end = interval[1]
            else:  # else overlap, erase + 1
                erased += 1
        return erased

    def eraseOverlapIntervals3(self, intervals):
        if not intervals: return 0
        intervals.sort(key=lambda x: x[0])  # sort on start time
        currEnd, cnt = intervals[0][1], 0
        for x in intervals[1:]:
            if x[0] < currEnd:  # find overlapping interval
                cnt += 1
                currEnd = min(currEnd, x[1])  # erase the one with larger end time
            else:
                currEnd = x[1]  # update end time
        return cnt



intervals = [[1,2],[1,3],[2,3],[3,4]]  # 1
# intervals = [[1,2],[1,2],[1,2]] # 2
# intervals = [[1,2],[2,3]]  # 0
print(Solution().eraseOverlapIntervals(intervals))