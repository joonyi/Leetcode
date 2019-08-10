"""
The string "PAYPALISHIRING" is written in a zigzag pattern on a given number of rows
like this: (you may want to display this pattern in a fixed font for better legibility)
"""

# Not working
class Solution(object):
    def convert(self, s, numRows):
        """
        :type s: str
        :type numRows: int
        :rtype: str
        """
        col = len(s) // numRows
        col = col + (col - 1)
        skip = numRows - 2
        zig = [[0 for _ in range(col)] for _ in range(numRows)]
        for i in range(numRows):
            k = 0
            # while j < len(s):
            for j in range(i, len(s), numRows + 1):
                zig[i][k] = s[j]
                k += 1 + skip

        return zig

    def convert2(self, s, numRows):
        col = len(s) // numRows
        col += (col) * (len(s) % numRows)
        reset = numRows + numRows - 2
        if reset == 0 or col <= 0:
            return s
        zig = [[0 for _ in range(col)] for _ in range(numRows)]
        i, j = 0, 0
        r, c = 0, -1
        dir = 1
        while i < len(s):
            if i % reset == 0:
                dir = 1
                if c < col - 1:
                    c += 1

            zig[r][c] = s[i]
            r += dir * 1
            if r == numRows:
                r = numRows - 2
                dir = -1
                c += 1
            i += 1

        res = ''
        for i in range(len(zig)):
            for j in range(len(zig[i])):
                if zig[i][j] != 0:
                    res += zig[i][j]

        return res



# s = "PAYPALISHIRING"
# numRows = 4
# s = "A"
# numRows = 2
s = "ABCDEF"
numRows = 2
print(Solution().convert2(s, numRows))