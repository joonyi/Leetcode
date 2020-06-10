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
        if numRows == 1:
            return s

        rows = [''] * min(numRows, len(s))
        curRow = 0
        goingDown = False
        for c in s:
            rows[curRow] += c
            if curRow == 0 or curRow == numRows - 1:
                goingDown = not goingDown
            curRow += 1 if goingDown else -1
        res = []
        for row in rows:
            res.append(row)
        return ''.join(res)



# s = "PAYPALISHIRING" # "PINALSIGYAHRPI"
# numRows = 4
s = "PAYPALISHIRING" # "PAHNAPLSIIGYIR"
numRows = 3
# s, numRows = "A", 2
print(Solution().convert(s, numRows))