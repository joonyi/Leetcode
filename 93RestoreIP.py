"""
Given a string containing only digits, restore it by returning all possible valid IP address combinations.
"""
class Solution(object):
    def restoreIpAddresses(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res = []
        self.dfs(s, 0, "", res)
        return res

    def dfs(self, s, index, path, res):
        if index == 4:
            if not s:
                res.append(path[:-1]) # -1 to remove last '.'
            return  # backtracking
        for i in range(1, 4):
            # the digits we choose should no more than the length of s
            if i <= len(s):
                # choose one digit
                if i == 1:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose two digits, the first one should not be "0"
                elif i == 2 and s[0] != "0":
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)
                # choose three digits, the first one should not be "0", and should less than 256
                elif i == 3 and s[0] != "0" and int(s[:3]) <= 255:
                    self.dfs(s[i:], index + 1, path + s[:i] + ".", res)

    def restoreIpAddresses2(self, s):
        if not s: return s
        n = len(s)
        res = []
        for a in range(1, 4):
            if n - a > 9 or n - a < 3: continue
            b_min = max(a + 1, n - 6)  # avoid to remain too many digits   (need =< 6 digits for C,D)
            b_max = min(a + 3, n - 2)  # avoid to remain not enough digits (need >= 2 digits for C,D)
            for b in range(b_min, b_max + 1):
                c_min = max(b + 1, n - 3)  # avoid to remain too many digits   (need =< 3 digits for D)
                c_max = min(b + 3, n - 1)  # avoid to remain not enough digits (need >= 1 digits for D)
                for c in range(c_min, c_max + 1):
                    A = int(s[:a])
                    B = int(s[a:b])
                    C = int(s[b:c])
                    D = int(s[c:])
                    # st = f'{A}.{B}.{C}.{D}'
                    st = str(A) + "." + str(B) + "." + str(C) + "." + str(D)
                    if len(st) == n + 3 and A < 256 and B < 256 and C < 256 and D < 256:
                        res.append(st)
        return res


s = "25525511135"
print(Solution().restoreIpAddresses(s))