"""
Given an array of 4 digits, return the largest 24 hour time that can be made.

The smallest 24 hour time is 00:00, and the largest is 23:59.  Starting from 00:00,
a time is larger if more time has elapsed since midnight.

Return the answer as a string of length 5.  If no valid time can be made, return an empty string.
"""

from typing import List
class Solution:
    def largestTimeFromDigits(self, A: List[int]) -> str:
        # Greedy not working
        d = dict()
        for a in A:
            d[a] = d.get(a, 0) + 1

        time = ["", "", ":", "", ""]
        for i in range(len(time)):
            if i == 0:
                if 2 in d and d[2] != 0:
                    d[2] -= 1
                    time[i] = "2"
                elif 1 in d and d[1] != 0:
                    d[1] -= 1
                    time[i] = "1"
                elif 0 in d and d[0] != 0:
                    d[0] -= 1
                    time[i] = "0"
                else:
                    return ""
            elif i == 1:
                if time[i-1] == "2":
                    if 3 in d and d[3] != 0:
                        d[3] -= 1
                        time[i] = "3"
                    elif 2 in d and d[2] != 0:
                        d[2] -= 1
                        time[i] = "2"
                    elif 1 in d and d[1] != 0:
                        d[1] -= 1
                        time[i] = "1"
                    elif 0 in d and d[0] != 0:
                        d[0] -= 1
                        time[i] = "0"
                    else:
                        return ""
                else:
                    x = max(d.keys())
                    if d[x] == 0:
                        d.pop(x)
                        x = max(d.keys())
                    time[i] = str(x)
                    d[x] -= 1
            elif i == 3:
                if 5 in d and d[5] != 0:
                    d[5] -= 1
                    time[i] = "5"
                elif 4 in d and d[4] != 0:
                    d[4] -= 1
                    time[i] = "4"
                elif 3 in d and d[3] != 0:
                    d[3] -= 1
                    time[i] = "3"
                elif 2 in d and d[2] != 0:
                    d[2] -= 1
                    time[i] = "2"
                elif 1 in d and d[1] != 0:
                    d[1] -= 1
                    time[i] = "1"
                elif 0 in d and d[0] != 0:
                    d[0] -= 1
                    time[i] = "0"
                else:
                    return ""
            elif i == 4:
                last = ""
                for k in d:
                    if d[k] != 0:
                        last = str(k)
                time[i] = last

        return ''.join(time)

    def largestTimeFromDigits2(self, A: List[int]) -> str:
        # Brute Force
        import itertools
        k = sorted(list(itertools.permutations(A)), reverse=True)
        for i in k:
            a, b, c, d = i
            su = (a * 10 + b)
            sd = (c * 10 + d)

            if su < 24 and sd < 60:
                return f"{a}{b}:{c}{d}"

        return ''

    def largestTimeFromDigits3(self, A: List[int]) -> str:
        """
        The inner most loop at most iterates 4 * 4 * 4 = 64 times.
        A[i], A[j], A[k], & A[l] are the 4 elements of A, where i, j, k & l are
        the permutation of 0, 1, 2, & 3. Therefore, since i + j + k + l = 0 + 1 + 2 + 3 = 6,
        we have l = 6 - i - j - k
        """
        ans = ''
        for i, a in enumerate(A):
            for j, b in enumerate(A):
                for k, c in enumerate(A):
                    if i == j or i == k or j == k:
                        continue
                    hour = str(a) + str(b)
                    minute = str(c) + str(A[6 - i - j - k])
                    if hour < '24' and minute < '60':  # valid answer
                        ans = max(ans, hour + ':' + minute)
        return ans


A = [1,2,3,4] # 23:41
# A = [5,5,5,5] # ""
# A = [0,4,0,0] # 04:00
# A = [4,1,0,0]  # 14:00
# A = [1,9,6,0]  # 19:06
A = [2,0,6,6] # 06:26
print(Solution().largestTimeFromDigits3(A))

