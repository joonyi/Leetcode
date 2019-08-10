"""
Given a list of 24-hour clock time points in "Hour:Minutes" format,
find the minimum minutes difference between any two time points in the list.
"""
class Solution(object):
    def findMinDifference(self, timePoints):
        """
        :type timePoints: List[str]
        :rtype: int
        """
        A = [0] * len(timePoints)
        i = 0
        for time in timePoints:
            A[i] = int(time[:2]) * 60 + int(time[3:])
            i += 1

        A.sort()
        diff = A[0] - 0 + 1440 - A[-1]
        for i in range(1, len(A)):
            if A[i] - A[i-1] < diff:
                diff = A[i] - A[i-1]

        return diff

    def findMinDifference2(self, timePoints):
        def convert(time):
            return int(time[:2]) * 60 + int(time[3:])

        minutes = list(map(convert, timePoints))
        minutes.sort()

        return min((y - x) % (24 * 60)
                   for x, y in zip(minutes, minutes[1:] + minutes[:1]))

        # a = [1,2,3], a[1:] + a[:1] = [2,3,1]
        # zip them become (1,2), (2,3), (3,1)


# timePoints = ["23:59","00:00"]
timePoints = ["05:31","22:08","00:35"]
print(Solution().findMinDifference2(timePoints))