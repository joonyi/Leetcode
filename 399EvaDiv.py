"""
Equations are given in the format A / B = k, where A and B are variables represented as strings,
and k is a real number (floating point number). Given some queries, return the answers.
If the answer does not exist, return -1.0.
"""

import collections
from typing import List
class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        # A variation of Floyd–Warshall
        quot = collections.defaultdict(dict)
        # Build Graph
        for (num, den), val in zip(equations, values):
            quot[num][num] = quot[den][den] = 1.0
            quot[num][den] = val
            quot[den][num] = 1 / val
        for k in quot:
            for i in quot[k]:
                for j in quot[k]:
                    quot[i][j] = quot[i][k] * quot[k][j]
        return [quot[num].get(den, -1.0) for num, den in queries]


    def calcEquation2(self, equations, values, queries):
        def build_graph(equations, values):
            G = collections.defaultdict(list)
            for i in range(len(equations)):
                edge = equations[i]
                weight = values[i]
                source, dest = edge
                G[source].append((dest, weight))
                G[dest].append((source, 1 / weight))
            return G

        def dfs(s, e, seen, G, value):
            if s not in G or e not in G or s in seen:  # return -1 if source or end not in Graph or already visited
                return -1
            if s == e:
                return value
            seen.append(s)
            for i in range(len(G[s])):
                product = dfs(G[s][i][0], e, seen, G, value * G[s][i][1])  # visit that node with value multiplied
                if product != -1:
                    return product
            return -1

        G = build_graph(equations, values)

        return [dfs(s, e, [], G, 1.0) for s, e in queries]



equations = [ ["a", "b"], ["b", "c"] ]
values = [2.0, 3.0]
queries = [ ["a", "c"], ["b", "a"], ["a", "e"], ["a", "a"], ["x", "x"] ] # [6.0, 0.5, -1.0, 1.0, -1.0 ]
print(Solution().calcEquation2(equations, values, queries))
