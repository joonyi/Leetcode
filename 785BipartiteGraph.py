"""
Given an undirected graph, return true if and only if it is bipartite.

Recall that a graph is bipartite if we can split it's set of nodes into two independent
subsets A and B such that every edge in the graph has one node in A and another node in B.

The graph is given in the following form: graph[i] is a list of indexes j for which the edge
between nodes i and j exists.  Each node is an integer between 0 and graph.length - 1.
There are no self edges or parallel edges: graph[i] does not contain i,
and it doesn't contain any element twice.
"""
#  Use two colors to color the graph and see if there are any adjacent having same color
class Solution(object):
    def isBipartite(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: bool
        """
        n = len(graph)
        colors = [0] * n # 0 => initialize, 1 => first color, -1 => second color

        def validColor(graph, colors, color, node):
            """
            :type colors: List[int], keep track color of each node
            :type color: int, alternate coloring node with 1 and -1
            """
            if colors[node] != 0: # check if the node already visited
                return colors[node] == color # check if the already colored consistent with two-coloring scheme
            colors[node] = color # color the node
            for next in graph[node]:
                if not validColor(graph, colors, -color, next): # -color to alternate coloring
                    return False
            return True

        for i in range(n):
            if colors[i] == 0 and not validColor(graph, colors, 1, i):
                return False
        return True

    def isBipartite2(self, graph):
        n = len(graph)
        colors = [0] * n
        for i in range(n):
            if colors[i] != 0: # this is for disconnect component
                continue
            queue = []
            queue.append(i)
            colors[i] = 1 # White 1, Black -1
            while queue:
                node = queue.pop(0)
                for next in graph[node]:
                    if colors[next] == 0: # if node hasn't been colored
                        colors[next] = -colors[node] # alternate coloring
                        queue.append(next)
                    elif colors[next] != -colors[node]: # if not consistent with two-coloring scheme, not bipartite
                        return False

        return True


# A = [[1,2,3], [0,2], [0,1,3], [0,2]]
A = [[1,3], [0,2], [1,3], [0,2]]
print(Solution().isBipartite2(A))