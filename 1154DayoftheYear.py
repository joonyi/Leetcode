"""
Given a string date representing a Gregorian calendar date formatted as YYYY-MM-DD,
return the day number of the year.
"""

import datetime
class Solution:
    def dayOfYear(self, date: str) -> int:
        """"""
        t1 = datetime.datetime.strptime(date, '%Y-%m-%d')
        t2 = date.split("-")[0] + "-01" + "-01"
        t2 = datetime.datetime.strptime(t2, '%Y-%m-%d')
        d = t1 - t2
        return d.days + 1

    def dayOfYear2(self, date: str) -> int:
        Y, M, D = map(int, date.split('-'))
        return int((datetime.datetime(Y, M, D) - datetime.datetime(Y, 1, 1)).days + 1)

    def dayOfYear3(self, date: str) -> int:
        days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        Y, M, D = map(int, date.split('-'))
        """
        Every year that is exactly divisible by four is a leap year, 
        except for years that are exactly divisible by 100, but these centurial years are leap years 
        if they are exactly divisible by 400. For example, the years 1700, 1800, and 1900 
        are not leap years, but the years 1600 and 2000 are
        """
        if M > 2 and Y % 4 == 0 and (Y % 100 != 0 or Y % 400 == 0):
            D += 1  # Add one day for February for a leap year
        for i in range(M - 1):
            D += days[i]
        return D




# date = "2019-01-09"  # 9
date = "2019-02-10"  # 41
# date = "2003-03-01"  # 60
date = "2004-03-01"  # 61
# date = "1900-03-25"

print(Solution().dayOfYear3(date))
