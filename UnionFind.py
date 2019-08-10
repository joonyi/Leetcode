# This union find specific for num island, not general
class UnionFind(object):
    def __init__(self, grid):
        m, n = len(grid), len(grid[0])
        self.count = 0
        self.parent = [-1] * (m*n)
        self.rank = [0] * (m*n)
        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    self.parent[i*n + j] = i*n + j # make-set whose set representative is itself
                    # the formula convert matrix index to list index
                    self.count += 1 # number of set

    def find(self, i): # find-set
        if self.parent[i] != i:
            self.parent[i] = self.find(self.parent[i])
        return self.parent[i]

    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty: # root diff means diff set, so union them
            if self.rank[rootx] > self.rank[rooty]: # smaller set merge to larger set
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            self.count -= 1 # after union, one set reduced