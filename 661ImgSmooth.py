"""
Given a 2D integer matrix M representing the gray scale of an image, you need to design
a smoother to make the gray scale of each cell becomes the average gray scale (rounding down)
of all the 8 surrounding cells and itself. If a cell has less than 8 surrounding cells,
then use as many as you can.

Neighbour include left, right, up, down, four diagonal (if exist)
"""
class Solution(object):
    def imageSmoother(self, M):
        """
        :type M: List[List[int]]
        :rtype: List[List[int]]
        """
        R, C = len(M), len(M[0])
        ans = [[0] * C for _ in M]

        for r in range(R):
            for c in range(C):
                count = 0
                for nr in (r - 1, r, r + 1):
                    for nc in (c - 1, c, c + 1):
                        if 0 <= nr < R and 0 <= nc < C:
                            ans[r][c] += M[nr][nc]
                            count += 1
                ans[r][c] //= count

        return ans


M = [[1,1,1],
 [1,0,1],
 [1,1,1]]
print(Solution().imageSmoother(M))