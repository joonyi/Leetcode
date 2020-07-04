"""
You are given the array paths, where paths[i] = [cityAi, cityBi] means there exists a direct path going from
cityAi to cityBi. Return the destination city, that is, the city without any path outgoing to
another city.

It is guaranteed that the graph of paths forms a line without any loop, therefore,
there will be exactly one destination city.

"""

from typing import List
class Solution:
    def destCity(self, paths: List[List[str]]) -> str:
        starts, dest = set(), set()
        for path in paths:
            starts.add(path[0])
            dest.add(path[1])
        return (dest - starts).pop()

    def destCity2(self, paths: List[List[str]]) -> str:
        import collections
        d = collections.defaultdict(str)
        for path in paths:
            src = path[0]
            dst = path[1]
            d[src] = dst
        for k, v in d.items():
            if v not in d:
                return v


paths = [["London","New York"],["New York","Lima"],["Lima","Sao Paulo"]]
# paths = [["B","C"],["D","B"],["C","A"]]
print(Solution().destCity2(paths))
