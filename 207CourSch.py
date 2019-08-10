class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # Idea is dfs to find cycles
        graph = [[] for _ in range(numCourses)]
        visit = [0 for _ in range(numCourses)] # states: 0 = unknown, -1 == visiting, 1 = visited
        for x, y in prerequisites:
            graph[x].append(y)

        def dfs(i):
            if visit[i] == -1:
                return False
            if visit[i] == 1:
                return True
            visit[i] = -1
            for node in graph[i]:
                if not dfs(node): # if node not visited, visit it
                    return False
            visit[i] = 1
            return True

        for i in range(numCourses):
            if not dfs(i):
                return False
        return True

    def canFinish2(self, numCourses, prerequisites):
        from collections import deque
        # Idea is to record every node is travelled once
        ind = [[] for _ in range(numCourses)]  # indegree
        oud = [0] * numCourses  # outdegree
        for p in prerequisites:
            oud[p[0]] += 1
            ind[p[1]].append(p[0])
        dq = deque()
        for i in range(numCourses):
            if oud[i] == 0:
                dq.append(i)
        k = 0
        while dq:
            x = dq.pop()
            k += 1
            for i in ind[x]:
                oud[i] -= 1
                if oud[i] == 0:
                    dq.append(i)
        return k == numCourses


numCourses = 8
prerequisites = [[1,0],[2,6],[1,7],[6,4],[7,0],[0,5]] # No cycle
# prerequisites = [[1,0],[2,6],[1,7],[5,1],[6,4],[7,0],[0,5]] # Has cycle
# prerequisites = [[0,1],[1,0]]
print(Solution().canFinish2(numCourses, prerequisites))