"""
Given a non-negative index k where k ≤ 33, return the kth index row of the Pascal's triangle.
Note that the row index starts from 0.

Input: 3
Output: [1,3,3,1]
Follow up:

Could you optimize your algorithm to use only O(k) extra space?
"""

# Mysterious Solution
class Solution(object):
    def getRow(self, rowIndex):
        A = [0 for i in range(rowIndex+1)]
        A[0] = 1
        for i in range(1,rowIndex+1):
            for j in range(i,0,-1):
                A[j] += A[j-1]
        return A

    def getRow2(self, rowIndex):
        row = [1]
        for _ in range(rowIndex):
            row = [x + y for x, y in zip([0] + row, row + [0])]
        return row

print(Solution().getRow2(3))
