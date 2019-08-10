"""
You are given a string representing an attendance record for a student.
The record only contains the following three characters:
'A' : Absent.
'L' : Late.
'P' : Present.
A student could be rewarded if his attendance record doesn't contain more than
one 'A' (absent) or more than two continuous 'L' (late).

You need to return whether the student could be rewarded according to his attendance record.
"""


class Solution(object):
    def checkRecord(self, s):
        """
        :type s: str
        :rtype: bool
        """
        if len(s) <= 1: return True
        A = 0
        if s[0] == "A": A += 1
        if len(s) == 2 and s[1] == "A":
            A += 1
            if A > 1: return False

        for i in range(2, len(s)):
            if s[i-2] == "L" and s[i-1] == "L" and s[i] == "L":
                return False
            elif s[i] == "A":
                A += 1
                if A > 1:
                    return False

        return True

    def checkRecord2(self, s):
        A, L_cont = 0, 0
        for ch in s:
            if ch == "A":
                A += 1
            if ch == "L":
                L_cont += 1
            else:
                L_cont = 0
            if A > 1 or L_cont > 2:
                return False
        return True


# A = "PPALLP" # True
# A = "PPALLL" # False
# A = "LLPPPLL" # True
A = "AL"
print(Solution().checkRecord2(A))