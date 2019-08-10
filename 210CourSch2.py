from collections import defaultdict
class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Idea DFS to detect cycle, if no cycle, able to do topological sort
        WHITE = 1
        GRAY = 2
        BLACK = 3
        # Create the adjacency list representation of the graph
        adj_list = defaultdict(list)
        # A pair [a, b] in the input represents edge from b --> a
        for dest, src in prerequisites:
            adj_list[src].append(dest)
        topological_sorted_order = []
        is_possible = True
        # By default all vertces are WHITE
        color = {k: WHITE for k in range(numCourses)}

        def dfs(node):
            nonlocal is_possible
            # Don't recurse further if we found a cycle already
            if not is_possible:
                return
            # Start the recursion
            color[node] = GRAY
            # Traverse on neighboring vertices
            if node in adj_list:
                for neighbor in adj_list[node]:
                    if color[neighbor] == WHITE:
                        dfs(neighbor)
                    elif color[neighbor] == GRAY:
                        # An edge to a GRAY vertex represents a cycle
                        is_possible = False
            # Recursion ends. We mark it as black
            color[node] = BLACK
            topological_sorted_order.append(node)

        for vertex in range(numCourses):
            # If the node is unprocessed, then call dfs on it.
            if color[vertex] == WHITE:
                dfs(vertex)
        return topological_sorted_order[::-1] if is_possible else []

    def findOrder2(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # Idea: BFS all the 0-indegree node, if possible to get to all nodes,
        # then no cycle
        adj_list = defaultdict(list)
        indegree = {}
        for dest, src in prerequisites:
            adj_list[src].append(dest)
            # Record each node's in-degree
            indegree[dest] = indegree.get(dest, 0) + 1

        # Queue for maintainig list of nodes that have 0 in-degree
        zero_indegree_queue = [k for k in range(numCourses) if k not in indegree]
        topological_sorted_order = []
        # Until there are nodes in the Q
        while zero_indegree_queue:
            # Pop one node with 0 in-degree
            vertex = zero_indegree_queue.pop()
            topological_sorted_order.append(vertex)
            # Reduce in-degree for all the neighbors
            if vertex in adj_list:
                for neighbor in adj_list[vertex]:
                    indegree[neighbor] -= 1

                    # Add neighbor to Q if in-degree becomes 0
                    if indegree[neighbor] == 0:
                        zero_indegree_queue.append(neighbor)

        return topological_sorted_order if len(topological_sorted_order) == numCourses else []

# numCourses = 3
# prerequisites = [[0,1],[0,2],[1,2]]
# prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]]
numCourses = 4
prerequisites = [[1,0],[2,0],[3,1],[3,2]]
print(Solution().findOrder2(numCourses, prerequisites))