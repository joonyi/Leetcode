"""
Detect cycle in a graph
"""
class Solution(object):
    def eventualSafeNodes(self, graph):
        """
        :type graph: List[List[int]]
        :rtype: List[int]
        """
        # visited so that no visit twice
        # visiting to detect back edges
        def dfs(graph, visited, visiting, cycle, i):
            if visited[i] == 0:
                visited[i] = 1
                visiting[i] = 1
                for node in graph[i]:
                    dfs(graph, visited, visiting, cycle, node)
            elif visiting[i] == 1:
                for j in range(len(visiting)):
                    if visiting[j]:
                        cycle.add(j)

            visiting[i] = 0 # Finish visiting the node

        cycle = set()
        vertices = set()
        for i in range(len(graph)):
            visited = [0] * len(graph)
            visiting = [0] * len(graph)
            vertices.add(i)
            if i not in cycle:
                dfs(graph, visited, visiting, cycle, i)

        return sorted(vertices - cycle)

    def eventualSafeNodes2(self, graph):
        import collections
        WHITE, GRAY, BLACK = 0, 1, 2
        color = collections.defaultdict(int)

        def dfs(node):
            if color[node] != WHITE: # create unvisited default color 0, white
                return color[node] == BLACK # T if finished, F if Gray,

            color[node] = GRAY # visiting
            for nei in graph[node]:
                if color[nei] == BLACK: # already visited
                    continue
                if color[nei] == GRAY or not dfs(nei): # detect back edge
                    return False # return False here, so cycle gray color remain
            color[node] = BLACK # finished
            return True

        res = list(filter(dfs, range(len(graph))))
        return res
        # filter test each element in second parameter, if true, keep that element

    def eventualSafeNodes3(self, graph):
        # Idea: terminal nodes are safe and also their parents
        # All nodes that can reach terminal nodes is also safe
        # Reverse graph edges to find those nodes
        import collections
        N = len(graph)
        safe = [False] * N

        graph = list(map(set, graph))
        rgraph = [set() for _ in range(N)]
        q = collections.deque()

        for i, js in enumerate(graph):
            if not js:
                q.append(i) # node with not outgoing edges
            for j in js:
                rgraph[j].add(i) # Build reverse edge graph

        while q:
            j = q.popleft()
            safe[j] = True
            for i in rgraph[j]:
                graph[i].remove(j)
                if len(graph[i]) == 0:
                    q.append(i)

        return [i for i, v in enumerate(safe) if v]

graph = [[1,2],[2,3],[5],[0],[5],[],[]]
# graph = [[0],[2,3,4],[3,4],[0,4],[]] # expected 4
# graph = [[1,3,4,5,7,9],[1,3,8,9],[3,4,5,8],[1,8],[5,7,8],[8,9],[7,8,9],[3],[],[]] # [5,8,9]
print(Solution().eventualSafeNodes3(graph))

"""
Notice that when using map, the items in the result are values returned by the function cube.

In contrast, the values returned by f in filter(f, ...) are not the items in result. 
f(i) is only used to determine if the value i should be kept in result.
"""