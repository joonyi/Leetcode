"""
In a town, there are N people labelled from 1 to N.
There is a rumor that one of these people is secretly the town judge.

If the town judge exists, then:

The town judge trusts nobody.
Everybody (except for the town judge) trusts the town judge.
There is exactly one person that satisfies properties 1 and 2.
You are given trust, an array of pairs trust[i] = [a, b] representing that the person
labelled a trusts the person labelled b.

If the town judge exists and can be identified, return the label of the town judge.
Otherwise, return -1.
"""
class Solution(object):
    def findJudge(self, N, trust):
        """
        :type N: int
        :type trust: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        graph = defaultdict(list)
        oud = [0] * (N + 1)
        ind = [0] * (N + 1)
        for u, v in trust:
            graph[u].append(v)
            oud[u] += 1
            ind[v] += 1
        judge = []
        for i in range(1, len(oud)):
            if oud[i] == 0 and ind[i] == N - 1:
                judge.append(i)
        if len(judge) == 1:
            return judge[0]
        else:
            return -1

# N = 2
# trust = [[1, 2]]
# N = 3
# trust = [[1,3],[2,3]]
# N = 3
# trust = [[1,3],[2,3],[3,1]]
# N = 3
# trust = [[1,2],[2,3]]
N = 4
trust = [[1,3],[1,4],[2,3],[2,4],[4,3]]

print(Solution().findJudge(N, trust))