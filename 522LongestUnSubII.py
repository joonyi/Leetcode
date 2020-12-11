"""
Given a list of strings, you need to find the longest uncommon subsequence among them.
The longest uncommon subsequence is defined as the longest subsequence of one of these strings
and this subsequence should not be any subsequence of the other strings.

A subsequence is a sequence that can be derived from one sequence by deleting some characters
without changing the order of the remaining elements. Trivially, any string is a subsequence of
itself and an empty string is a subsequence of any string.

The input will be a list of strings, and the output needs to be the length of the
longest uncommon subsequence. If the longest uncommon subsequence doesn't exist, return -1.
"""

from typing import List
class Solution:
    def findLUSlength(self, strs: List[str]) -> int:
        strs.sort(key=len, reverse=True)
        for i, word1 in enumerate(strs):
            res = [not self.isSubsequence(word1, word2) for j, word2 in enumerate(strs) if i != j]
            if all(res):
                return len(word1)

        return -1

    def isSubsequence(self, s1, s2):
        # True if s1 is a subsequence of s2
        i = 0
        for c in s2:
            if i < len(s1) and s1[i] == c:
                i += 1
        return i == len(s1)



strs = ["aba", "cdc", "eae"]
print(Solution().findLUSlength(strs))