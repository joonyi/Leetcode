"""
N couples sit in 2N seats arranged in a row and want to hold hands.
We want to know the minimum number of swaps so that every couple is sitting side by side.
A swap consists of choosing any two people, then they stand up and switch seats.

The people and seats are represented by an integer from 0 to 2N-1,
the couples are numbered in order, the first couple being (0, 1),
the second couple being (2, 3), and so on with the last couple being (2N-2, 2N-1).

The couples' initial seating is given by row[i] being the value of the person
who is initially sitting in the i-th seat.
"""
class UF(object):
    def __init__(self, n):
        self.parents = [0] * n
        for i in range(n):
            self.parents[i] = i
        self.count = n

    def find(self, i):
        if self.parents[i] == i:
            return i
        self.parents[i] = self.find(self.parents[i])
        return self.parents[i]

    def union(self, i, j):
        a = self.find(i)
        b = self.find(j)
        if a != b:
            self.parents[a] = b
            self.count -= 1

class Solution(object):
    def minSwapsCouples(self, row):
        """
        :type row: List[int]
        :rtype: int
        """
        n = len(row)
        pos = {}
        for i in range(n):
            pos[row[i]] = i

        count = 0
        for i in range(0, n, 2):
            # if even, next position is a higher odd
            j = row[i] + 1 if row[i] % 2 == 0 else row[i] - 1
            if row[i+1] != j:
                self.swap(row, pos, i+1, pos[j]) # search for the higher odd and swap to correct pos
                count += 1

        return count

    def swap(self, row, pos, x, y):
        tmp = row[x]
        pos[tmp] = y
        pos[row[y]] = x
        row[x] = row[y]
        row[y] = tmp

    def minSwapsCouples2(self, row):
        N = len(row)//2
        uf = UF(N)
        for i in range(N):
            a = row[2*i]
            b = row[2*i + 1]
            uf.union(a//2, b//2)
        return N - uf.count


row = [0,2,4,6,7,1,3,5]
print(Solution().minSwapsCouples2(row))