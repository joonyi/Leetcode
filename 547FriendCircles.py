"""
There are N students in a class. Some of them are friends, while some are not.
Their friendship is transitive in nature. For example, if A is a direct friend of B,
and B is a direct friend of C, then A is an indirect friend of C. And we defined a
friend circle is a group of students who are direct or indirect friends.

Given a N*N matrix M representing the friend relationship between students in the class.
If M[i][j] = 1, then the ith and jth students are direct friends with each other,
otherwise not. And you have to output the total number of friend circles among all the students.
"""
class Solution(object):
    def findCircleNum(self, M):
        """
        :type M: List[List[int]]
        :rtype: int
        """
        def dfs(M, friends, i):
            if any(friends):
                for j in range(len(friends)):
                    if M[i][j]:
                        M[i][j] = 0
                        dfs(M, M[j], j)

        cnt = 0
        for i, friends in enumerate(M):
            for j in range(len(friends)):
                if M[i][j]:
                    M[i][j] = 0
                    cnt += 1
                    dfs(M, M[j], j)

        return cnt

    def findCircleNum2(self, M):
        from collections import defaultdict
        graph = defaultdict(list)
        for i, row in enumerate(M):
            for j in range(len(row)):
                if i != j and row[j]:
                    graph[i].append(j)

        def dfs(graph, friend, i):
            if friends[i]:
                friends[i] = 0
                for friend in graph[i]:
                    dfs(graph, friends, friend)

        friends = [1] * len(M)
        cnt = 0
        for i in range(len(friends)):
            if friends[i]:
                cnt += 1
                dfs(graph, friends, i)

        return cnt



M = [[1,1,0],[1,1,0],[0,0,1]]
# M = [[1,1,0],[1,1,1],[0,1,1]]
# M = [[1,0,0,1],[0,1,1,0],[0,1,1,1],[1,0,1,1]]

print(Solution().findCircleNum(M))