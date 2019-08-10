"""
Given an array equations of strings that represent relationships between variables,
each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".
Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to
satisfy all the given equations.
"""

# 1. One idea, construct a graph with every == equation in one color,
# then for each a!=b equation, dfs a from b to check if they have a same color
# 2. Another idea, union find. == equation in one set. Then check !=, two inequal node
# should not be in same set
class UnionFind(object):
    def __init__(self):
        self.parent = {} # because 26 alphabet
    def find(self, x):
        if self.parent[x] == x:
            return x
        self.parent[x] = self.find(self.parent[x])
    def union(self, x, y):
        self.parent[self.find(y)] = self.find(x)


class Solution(object):
    def equationsPossible(self, equations):
        """
        :type equations: List[str]
        :rtype: bool
        """
        uf = {}

        def find(x):
            if x not in uf:
                return x
            if uf[x] != x:
                uf[x] = find(uf[x])
            return uf[x]

        for x, eq, _, y in equations: # Construct graph for equality
            if eq == "=":
                if x not in uf:
                    uf[x] = x
                if y not in uf:
                    uf[y] = y
                uf[find(x)] = find(y)

        for x, eq, _, y in equations:
            if eq == "!" and find(x) == find(y):
                return False

        return True

# A = ["a==b","b!=a"]
# A = ["b==a","a==b"]
# A = ["a==b","b==c","a==c"]
# A = ["a==b","b!=c","c==a"]
A = ["c==c","b==d","x!=z"]
print(Solution().equationsPossible(A))