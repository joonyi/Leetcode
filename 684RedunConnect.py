from UnionFind2 import UnionFind
class Solution(object):
    def findRedundantConnection(self, edges):
        """
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # For each edge (u, v), traverse the graph with a depth-first search to see
        # if we can connect u to v. If we can, then it must be the duplicate edge.
        # O(n^2) because for each edge, traverse the graph with O(n) and there are n edges
        import collections
        graph = collections.defaultdict(set)

        def dfs(source, target):
            if source not in seen:
                seen.add(source)
                if source == target: return True
                return any(dfs(nei, target) for nei in graph[source])

        for u, v in edges:
            seen = set()
            if u in graph and v in graph:
                if dfs(u, v):
                    return u, v
            graph[u].add(v)
            graph[v].add(u)

    def findRedundantConnection2(self, edges):
        # Idea find the first vertex which already union
        uf = UnionFind(edges)
        for x, y in edges:
            if uf.union_by_rank(x - 1, y - 1): # True if x, y already have same parent
                return [x, y]


A = [[1,2], [1,3], [2,3]]
# A = [[1,2], [2,3], [3,4], [1,4], [1,5]]
# A = [[1,4],[3,4],[1,3],[1,2],[4,5]]
print(Solution().findRedundantConnection2(A))