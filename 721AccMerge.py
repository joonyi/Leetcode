from collections import defaultdict
class UnionFind(object):
    def __init__(self, accounts):
        self.parent = list(range(10001))
        self.rank = [0] * 10001
    def find(self, x):
        if self.parent[x] == x: # x's parent is its own
            return x
        self.parent[x] = self.find(self.parent[x]) # else search for its parent
        # and change x's parent, a heuristic called path compression
        return self.parent[x]
    def union(self, x, y):
        self.parent[self.find(x)] = self.find(y)
    def union_by_rank(self, x, y):
        rootx = self.find(x)
        rooty = self.find(y)
        if rootx != rooty:
            if self.rank[rootx] > self.rank[rooty]:
                self.parent[rooty] = rootx
            elif self.rank[rootx] < self.rank[rooty]:
                self.parent[rootx] = rooty
            else:
                self.parent[rooty] = rootx
                self.rank[rootx] += 1


class Solution(object):
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        uf = UnionFind(accounts)
        email_to_name = {}
        email_to_id = {}
        i = 0
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                email_to_name[email] = name # name can be replaced
                if email not in email_to_id: # but id should be unique
                    email_to_id[email] = i
                    i += 1
                uf.union_by_rank(email_to_id[acc[1]], email_to_id[email]) # Union all element in same list

        ans = defaultdict(list)
        for email in email_to_name:
            parent = uf.find(email_to_id[email])
            ans[parent].append(email)
        return [[email_to_name[v[0]]] + sorted(v) for v in ans.values()]

    # For every pair of emails in the same account, draw an edge between those emails
    # Then dfs to merge the connected components
    def accountsMerge2(self, accounts):
        em_to_name = {}
        graph = defaultdict(set)
        for acc in accounts:
            name = acc[0]
            for email in acc[1:]:
                graph[acc[1]].add(email)
                graph[email].add(acc[1])
                em_to_name[email] = name

        seen = set()
        ans = []
        for email in graph:
            if email not in seen: # visit the unvisited
                seen.add(email) # mark visited
                stack = [email]
                component = []
                while stack: # visit connected component
                    node = stack.pop()
                    component.append(node)
                    for nei in graph[node]:
                        if nei not in seen:
                            seen.add(nei)
                            stack.append(nei)
                ans.append([em_to_name[email]] + sorted(component))
        return ans


accounts = [["John", "johnsmith@mail.com", "john00@mail.com"],
            ["John", "johnnybravo@mail.com"],
            ["John", "johnsmith@mail.com", "john_newyork@mail.com"],
            ["Mary", "mary@mail.com"]]
# accounts = [["Gabe","Gabe0@m.co","Gabe3@m.co","Gabe1@m.co"],
#            ["Kevin","Kevin3@m.co","Kevin5@m.co","Kevin0@m.co"],
#            ["Ethan","Ethan5@m.co","Ethan4@m.co","Ethan0@m.co"],
#            ["Hanzo","Hanzo3@m.co","Hanzo1@m.co","Hanzo0@m.co"],
#            ["Fern","Fern5@m.co","Fern1@m.co","Fern0@m.co"]]
print(Solution().accountsMerge2(accounts))