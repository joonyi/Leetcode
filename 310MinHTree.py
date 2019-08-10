"""
For an undirected graph with tree characteristics, we can choose any node as the root.
The result graph is then a rooted tree. Among all possible rooted trees, those with
minimum height are called minimum height trees (MHTs). Given such a graph,
write a function to find all the MHTs and return a list of their root labels.
"""
class Solution(object):
    def findMinHeightTrees(self, n, edges):
        """
        :type n: int
        :type edges: List[List[int]]
        :rtype: List[int]
        """
        # TLE
        # Should use dynamic programming idea so that height wont be calculated twice
        # Build graph
        from collections import defaultdict
        graph = defaultdict(list)
        for i, j in edges:
            graph[i].append(j)
            graph[j].append(i)

        min_height = [0] * n
        for s in range(n):
            height = [0] * n
            cnt = 0
            visited = set()
            visited.add(s)
            queue = [s]
            while queue:
                nxt = []
                cnt += 1
                for u in queue:
                    for v in graph[u]:
                        if v not in visited:
                            height[v] = cnt
                            visited.add(v)
                            nxt.append(v)
                queue = nxt

            min_height[s] = max(height)

        res = []
        min_val = min(min_height)
        for i, val in enumerate(min_height):
            if val == min_val:
                res.append(i)

        return res

    def findMinHeightTrees2(self, n, edges):
        """
        MHT has to be the middle point (or two middle points) of the longest path of the tree.
        Remove leaves iteratively till one more two middle points, which is the answer
        """
        if n == 1: return [0]
        adj = [set() for _ in range(n)]
        for i, j in edges:
            adj[i].add(j)
            adj[j].add(i)

        leaves = [i for i in range(n) if len(adj[i]) == 1]

        while n > 2:
            n -= len(leaves)
            newLeaves = []
            for i in leaves:
                j = adj[i].pop()
                adj[j].remove(i)
                if len(adj[j]) == 1: newLeaves.append(j)
            leaves = newLeaves
        return leaves

# n = 4
# edges = [[1, 0], [1, 2], [1, 3]]
n = 6
edges = [[0, 3], [1, 3], [2, 3], [4, 3], [5, 4]]
print(Solution().findMinHeightTrees2(n, edges))