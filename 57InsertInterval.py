"""
Given a set of non-overlapping intervals, insert a new interval into the intervals (merge if necessary).

You may assume that the intervals were initially sorted according to their start times.
"""
class Solution(object):
    def insert(self, intervals, newInterval):
        """
        :type intervals: List[List[int]]
        :type newInterval: List[int]
        :rtype: List[List[int]]
        """
        s, e = newInterval[0], newInterval[1]
        left = [i for i in intervals if i[1] < s]
        right = [i for i in intervals if i[0] > e]
        if left + right != intervals:
            s = min(s, intervals[len(left)][0])
            e = max(e, intervals[~len(right)][1])
        return left + [[s, e]] + right

    def insert2(self, intervals, newInterval):
        # Collect the intervals strictly left or right of the new interval,
        # then merge the new one with the middle ones (if any) before inserting it
        # between left and right ones.
        s, e = newInterval[0], newInterval[1]
        left, right = [], []
        for interval in intervals:
            if interval[1] < s:
                left += interval,
            elif interval[0] > e:
                right += interval,
            else:
                s = min(s, interval[0])
                e = max(e, interval[1])
        return left + [[s, e]] + right

    def insert3(self, intervals, newInterval):
        # First, put all intervals that are to the left of the inserted interval.
        # Second, merge all intervals that intersect with the inserted interval.
        # Third, put all intervals that are to the right of the inserted interval.
        res = []
        idx = 0
        while idx < len(intervals) and intervals[idx][1] < newInterval[0]:
            res.append(intervals[idx])
            idx += 1
        while idx < len(intervals) and intervals[idx][0] <= newInterval[1]:
            newInterval[0] = min(newInterval[0], intervals[idx][0])
            newInterval[1] = max(newInterval[1], intervals[idx][1])
            idx += 1
        res.append(newInterval)
        while idx < len(intervals):
            res.append(intervals[idx])
            idx += 1

        return res


intervals, newInterval = [[1,3],[6,9]],  [2,5]
# intervals, newInterval = [[1,2],[3,5],[6,7],[8,10],[12,16]], [4,8]
print(Solution().insert3(intervals, newInterval))