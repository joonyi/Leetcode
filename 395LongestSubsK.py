"""
Find the length of the longest substring T of a given string (consists of lowercase letters only)
such that every character in T appears no less than k times.
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        # TLE
        n = len(s)
        maxLen = 0
        # dp = [[0] * n for _ in range(n)]
        for i in range(n):
            cnt = dict()
            for j in range(i, n):
                cnt[s[j]] = cnt.get(s[j], 0) + 1
                minRepeat = min(cnt.values())
                if minRepeat >= k and j - i + 1 > maxLen:
                    maxLen = j - i + 1

        return maxLen

    def longestSubstring2(self, s, k):
        """
        If every character appears at least k times, the whole string is valid.
        Otherwise split by a least frequent character (because it will always be
        infrequent and thus can't be part of any valid substring) and make the most out of the splits.
        """
        if len(s) < k:
            return 0
        c = min(set(s), key=s.count)
        if s.count(c) >= k:
            return len(s)
        return max(self.longestSubstring2(t, k) for t in s.split(c))

    def longestSubstring3(self, s, k):
        maxLen = 0
        for h in range(1, 27):
            cnt = [0] * 26
            i, j = 0, 0
            unique, noLess = 0, 0
            while j < len(s):
                if unique <= h:
                    idx = ord(s[j]) - ord('a')
                    if cnt[idx] == 0:
                        unique += 1
                    cnt[idx] += 1
                    if cnt[idx] == k:
                        noLess += 1
                    j += 1
                else:
                    idx = ord(s[i]) - ord('a')
                    if cnt[idx] == k:
                        noLess -= 1
                    cnt[idx] -= 1
                    if cnt[idx] == 0:
                        unique -= 1
                    i += 1


                if unique == h and unique == noLess:
                    maxLen = max(j - i, maxLen)

        return maxLen

    def longestSubstring4(self, s: str, k: int) -> int:
        count = 0
        for i in range(1, 27):
            count = max(count, self.helper(s, k, i))
        return count

    def helper(self, s, k, numUniqueTarget):
        import collections
        start = end = numUnique = numNoLessThanK = count = 0
        chMap = collections.defaultdict(int)

        while end < len(s):
            if chMap[s[end]] == 0: numUnique += 1
            chMap[s[end]] += 1
            if chMap[s[end]] == k: numNoLessThanK += 1
            end += 1

            while numUnique > numUniqueTarget:
                if chMap[s[start]] == k: numNoLessThanK -= 1
                chMap[s[start]] -= 1
                if chMap[s[start]] == 0: numUnique -= 1
                start += 1

            if numUnique == numNoLessThanK: count = max(count, end - start)

        return count


s, k = "aaabb", 3  # 3
# s, k = "ababbc", 2  # 5
# s, k = "bbaaacbd", 3  # 3
print(Solution().longestSubstring3(s, k))
