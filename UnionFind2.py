class UnionFind(object):
    def __init__(self, edges):
        self.parent = list(range(len(edges)))
        self.rank = [0] * len(edges)
    def find(self, x):
        if self.parent[x] == x: # x's parent is its own
            return x
        self.parent[x] = self.find(self.parent[x]) # else search for its parent
        # and change x's parent, a heuristic called path compression
        return self.parent[x]
    def union(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty: # different parent mean different set, union them
            self.parent[rooty] = rootx # union to a set of smaller parent number
            return False
        else: # already have same parent, redundant connection
            return True
    def union_by_rank(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1
            return False
        else:
            return True

