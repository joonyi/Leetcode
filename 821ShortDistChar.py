"""
Given a string S and a character C, return an array of integers representing
the shortest distance from the character C in the string.
"""
class Solution(object):
    def shortestToChar(self, S, C):
        """
        :type S: str
        :type C: str
        :rtype: List[int]
        """
        # Can use index subtraction for distance
        source = []
        res = [len(S)] * len(S)
        for i in range(len(S)):
            if S[i] == C:
                source.append(i)

        for s in source:
            i = s
            dist = 0
            while i >= 0:
                if res[i] > dist:
                    res[i] = dist
                dist += 1
                i -= 1
            i = s
            dist = 0
            while i < len(res):
                if res[i] > dist:
                    res[i] = dist
                dist += 1
                i += 1
        return res


    def shortestToChar2(self, S, C):
        prev = float('-inf')
        res = []
        for i, ch in enumerate(S):
            if ch == C:
                prev = i
            res.append(i - prev)

        prev = float('inf')
        for i in range(len(S) - 1, -1, -1):
            if S[i] == C:
                prev = i
            res[i] = min(res[i], prev - i)

        return res


S = "loveleetcode"
C = 'e'
print(Solution().shortestToChar2(S, C))
