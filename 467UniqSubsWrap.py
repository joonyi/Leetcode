"""
Consider the string s to be the infinite wraparound string of "abcdefghijklmnopqrstuvwxyz",
so s will look like this: "...zabcdefghijklmnopqrstuvwxyzabcdefghijklmnopqrstuvwxyzabcd....".

Now we have another string p. Your job is to find out how many unique non-empty substrings of p
are present in s. In particular, your input is the string p and you need to output the number of
different non-empty substrings of p in the string s.

Note: p consists of only lowercase English letters and the size of p might be over 10000.
"""

class Solution:
    def findSubstringInWraproundString(self, p: str) -> int:
        # TLE
        def check(q):
            for i in range(1, len(q)):
                if (ord(q[i]) - ord(q[i - 1])) % 26 != 1:
                    return False
            return True

        seen = set()
        for i in range(len(p)):
            for j in range(i + 1, len(p) + 1):
                if len(p[i:j]) == 1:
                    seen.add(p[i:j])
                elif check(p[i:j]):
                    seen.add(p[i:j])

        return seen

    def findSubstringInWraproundString2(self, p: str) -> int:
        # Not working
        cnt = set(p)
        adj = [False] * len(p)
        adj[0] = True
        for i in range(1, len(p)):
            if adj[i - 1] and (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                adj[i] = True
                cnt.add(p[:i + 1])
                cnt.add(p[i:i + 1])
            elif not adj[i - 1] and (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                adj[i] = True
                cnt.add(p[i:i + 1])

        return cnt

    def findSubstringInWraproundString3(self, p):
        res = {i: 1 for i in p}
        n = 1
        for i, j in zip(p, p[1:]):
            # l = l + 1 if (ord(j) - ord(i)) % 26 == 1 else 1
            if (ord(j) - ord(i)) % 26 == 1:
                n += 1
            else:
                n = 1
            res[j] = max(res[j], n)
        return sum(res.values())

    def findSubstringInWraproundString4(self, p):
        cnt = [0] * 26  # max number of unique substring ends with the letter i. i represent char
        maxLength = 0
        for i in range(len(p)):
            if i > 0 and (ord(p[i]) - ord(p[i - 1])) % 26 == 1:
                maxLength += 1
            else:
                maxLength = 1

            idx = ord(p[i]) - ord('a')  # convert i to char
            # if overlapping, store the longest one
            # e.g. bcd occur after abcd, the max number of unique substring ends with 'd' still is 4
            cnt[idx] = max(cnt[idx], maxLength)

        return sum(cnt)


p = "a"
# p = "cac"
# p = "zab"  # 6
p = 'abcd'  # 10
# p = 'abed'  # 5
# p = "aabb"  # 3
# p = "abaab"  # 3
# p = "zaba"  # 6
print(Solution().findSubstringInWraproundString4(p))


