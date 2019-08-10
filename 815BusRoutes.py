from collections import defaultdict
class Solution(object):
    def numBusesToDestination(self, routes, S, T):
        """
        :type routes: List[List[int]]
        :type S: int
        :type T: int
        :rtype: int
        """
        # TLE
        if S == T: return 0

        graph = defaultdict(list)
        for route in routes:
            for j in route:
                for k in route:
                    if j != k:
                        graph[j].append(k)

        queue = [graph[S]]
        cnt = 0
        visited = set()
        visited.add(S)
        while queue:
            nxt_stop = []
            cnt += 1
            for stops in queue:
                for stop in stops:
                    if stop not in visited:
                        if stop == T:
                            return cnt
                        visited.add(stop)
                        nxt_stop.append(graph[stop])

            queue = nxt_stop

        return -1

    def numBusesToDestination2(self, routes, S, T):
        if S == T: return 0
        routes = list(map(set, routes)) # need this so that no TLE
        graph = defaultdict(set)
        for i, r1 in enumerate(routes):
            for j in range(i + 1, len(routes)):
                r2 = routes[j]
                if any(r in r2 for r in r1):
                    graph[i].add(j)
                    graph[j].add(i)
        # Build graph differently, if any element in both set, connect two sets

        seen, targets = set(), set()
        for node, route in enumerate(routes):
            if S in route: seen.add(node)
            if T in route: targets.add(node)

        queue = [(node, 1) for node in seen]
        for node, depth in queue:
            if node in targets: return depth
            for nei in graph[node]:
                if nei not in seen:
                    seen.add(nei)
                    queue.append((nei, depth + 1))
        return -1

routes = [[1, 2, 7], [3, 6, 7]]
S = 1
T = 6
# routes = [[1,7],[3,5]]
# S = 5
# T = 5
print(Solution().numBusesToDestination2(routes, S, T))