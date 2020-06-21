"""
Given two strings s1 and s2, write a function to return true if s2 contains the permutation of s1.
In other words, one of the first string's permutations is the substring of the second string.
"""
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # Sliding window
        str2prime = dict(a=2, b=3, c=5, d=7, e=11, f=13, g=17, h=19,
                         i=23, j=29, k=31, l=37, m=41, n=43, o=47, p=53,
                         q=59, r=61, s=67, t=71, u=73, v=79, w=83, x=89,
                         y=97, z=101)
        n1 = 1
        for c in s1:
            n1 *= str2prime[c]

        n2 = 1
        for i, x in enumerate(s2):
            n2 *= str2prime[x]
            if i >= len(s1):
                n2 //= str2prime[s2[i - len(s1)]]
            if n1 == n2:
                return True
        return False

    def checkInclusion2(self, s1, s2):
        # Sliding window
        from collections import Counter
        ctr1 = Counter(s1)
        i = 0
        while i < len(s2) - len(s1) + 1:
            if s2[i] in ctr1:
                ctr2 = Counter(s2[i: i + len(s1)])
                if ctr1 == ctr2: return True
            i += 1
        return False

    def checkInclusion3(self, s1, s2):
        # Sliding window
        A = [ord(x) - ord('a') for x in s1]
        B = [ord(x) - ord('a') for x in s2]

        target = [0] * 26
        for x in A:
            target[x] += 1

        window = [0] * 26
        for i, x in enumerate(B):
            window[x] += 1
            if i >= len(A):  # if window longer than s1, delete previous entry
                window[B[i - len(A)]] -= 1
            if window == target:
                return True
        return False

# s1, s2 = "ab", "eidbaooo"  # T
s1, s2= "ab", "eidboaoo"  # F
print(Solution().checkInclusion(s1, s2))
