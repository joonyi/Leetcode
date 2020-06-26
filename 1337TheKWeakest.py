"""
Given a m * n matrix mat of ones (representing soldiers) and zeros (representing civilians),
return the indexes of the k weakest rows in the matrix ordered from the weakest to the strongest.

A row i is weaker than row j, if the number of soldiers in row i is less than the number of soldiers
in row j, or they have the same number of soldiers but i is less than j. Soldiers are always stand
in the frontier of a row, that is, always ones may appear first and then zeros.
"""

from typing import List
class Solution:
    def kWeakestRows(self, mat: List[List[int]], k: int) -> List[int]:
        soldiers = [0] * len(mat)
        for i, row in enumerate(mat):
            soldiers[i] = [sum(row), i]
        ranks = sorted(soldiers, key=lambda s: (s[0], s[1]))

        return [r[1] for r in ranks[:k]]

    def kWeakestRows2(self, mat: List[List[int]], k: int) -> List[int]:
        # Binary search for 1, improve to lgN
        def getScore(arr):
            start, end = 0, len(arr)
            while start < end:
                mid = (start + end) // 2
                if arr[mid] == 1:
                    start = mid + 1
                else:
                    end = mid
            return start

        out = []
        for i, arr in enumerate(mat):
            score = getScore(arr)
            out.append([score, i])
        out.sort(key=lambda x: x[0])
        return [out[i][1] for i in range(k)]


"""
Another idea
1. Iterate through the matrix and create the heap with pair index , number of soldiers
2. Min heap implementation using comparator based on number of soilders
3. Pop The K nodes and store in answer
"""

mat = [[1,1,0,0,0],
 [1,1,1,1,0],
 [1,0,0,0,0],
 [1,1,0,0,0],
 [1,1,1,1,1]]
k = 3
mat = [[1,0,0,0],
 [1,1,1,1],
 [1,0,0,0],
 [1,0,0,0]]
k = 2
print(Solution().kWeakestRows2(mat, k))
