"""
Given two strings A and B of lowercase letters, return true if and only if we can swap
two letters in A so that the result equals B.
"""

class Solution(object):
    def buddyStrings(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: bool
        """
        if len(A) != len(B): return False # if the len differ not possible
        if A == B: # if A == B, only possible if there are two same characters
            return len(A) - len(set(A)) >= 1
        else:
            pairs = []
            for a, b in zip(A, B):
                if a != b:
                    pairs.append((a, b))
                if len(pairs) >= 3: return False # Three pairs won't be able with one swap
            return len(pairs) == 2 and pairs[0] == pairs[1][::-1] # For two pairs, check one swap is possible

# A, B = "ab", "ba"
# A, B = "ab", "ab"
# A, B = "aa", "aa"
# A, B = "aaaaaaabc", "aaaaaaacb"
A, B = "ab", "de"
print(Solution().buddyStrings(A, B))