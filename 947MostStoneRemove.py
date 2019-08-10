class Solution(object):
    def removeStones(self, stones):
        """
        :type stones: List[List[int]]
        :rtype: int
        """
        from collections import defaultdict
        # Build graph from input first
        adj = defaultdict(list)
        for i, row in enumerate(stones):
            adj[i] = []
            x, y = row
            for j in range(len(stones)):
                if x == stones[j][0] and y == stones[j][1]:
                    continue
                elif x == stones[j][0] or y == stones[j][1]:
                    adj[i].append(j)

        def dfs(i, count):
            if not has_stone[i] and stones[i] != [0,0]:
                has_stone[i] = 1
                count += 1
                self.max_count = count if count > self.max_count else self.max_count
                for node in adj[i]:
                    dfs(node, count)
                count -= 1
                has_stone[i] = 0

        self.max_count = 0
        has_stone = [0 for _ in range(len(stones))]
        count = 0
        for k in range(len(stones)):
            dfs(k, count)
        return self.max_count


# stones = [[0,0],[0,1],[1,0],[1,2],[2,1],[2,2]] # 5
# stones = [[0,0],[0,2],[1,1],[2,0],[2,2]] #3
stones = [[0,0],[0,1],[1,0],[1,1],[2,1],[2,2],[3,2],[3,3],[3,4],[4,3],[4,4]] # 10
# stones = [[3,2],[3,1],[4,4],[1,1],[0,2],[4,0]] # expected 4
# stones = [[0,1],[1,0],[1,1]]
print(Solution().removeStones(stones))
