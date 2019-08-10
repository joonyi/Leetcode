"""
Given a non-negative integer numRows, generate the first numRows of Pascal's triangle.
In Pascal's triangle, each number is the sum of the two numbers directly above it.

Input: 5
Output:
[
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]
"""
class Solution(object):
    def generate(self, numRows):
        tri = [[1]*n for n in range(1,numRows+1)]
        for i in range(2,numRows):
            numCols = len(tri[i])
            for j in range(1,numCols-1):
                tri[i][j] = tri[i-1][j-1] + tri[i-1][j]
        return tri

    def generate2(self, numRows):
        pascal = [[1] * (i + 1) for i in range(numRows)]
        for i in range(numRows):
            for j in range(1, i):
                pascal[i][j] = pascal[i - 1][j - 1] + pascal[i - 1][j]
        return pascal

numRows = 33
print(Solution().generate2(numRows))