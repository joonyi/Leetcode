"""
Define S = [s,n] as the string S which consists of n connected strings s.
For example, ["abc", 3] ="abcabcabc".

On the other hand, we define that string s1 can be obtained from string s2 if we can remove
some characters from s2 such that it becomes s1. For example, “abc” can be obtained from “abdbec”
based on our definition, but it can not be obtained from “acbbe”.

You are given two non-empty strings s1 and s2 (each at most 100 characters long) and
two integers 0 ≤ n1 ≤ 106 and 1 ≤ n2 ≤ 106. Now consider the strings S1 and S2,
where S1=[s1,n1] and S2=[s2,n2]. Find the maximum integer M such that [S2,M] can be obtained from S1.

"""

class Solution:
    def getMaxRepetitions(self, s1: str, n1: int, s2: str, n2: int) -> int:
        """
        Fact:
        If s2 repeats in S1 R times, then S2 must repeats in S1 R / n2 times.
        Conclusion:
        We can simply count the repetition of s2 and then divide the count by n2
        """
        idx, repeat_count = 0, 0
        for _ in range(n1):
            for j in range(len(s1)):
                if s1[j] == s2[idx]:
                    idx += 1
                if idx == len(s2):
                    idx = 0
                    repeat_count += 1
        return repeat_count // n2


    def getMaxRepetitions2(self, s1, n1, s2, n2):
        """
        Match the two virtual s1 with s2, until the s1 index reach it's limit length,
        which by definition is n1*len(s1). Then the i2 position at this point will be the final
        result in terms of char length.
        The rest is just converting i2 to the number of words, where word length is len(s2)*n2.

        To improve performance, we use dictionary to store previously matched indexes in
        original s1 and s2, if the same matched index comes again, that means we are in a
        repeating pattern, in which case we increase i1 and i2 by the length of their
        repeating circle until there is not enough chars left in virtual s1
        """

        d, l1, l2, i1, i2 = {}, len(s1), len(s2), 0, 0
        tot = l1 * n1

        while i1 < tot:
            if s1[i1 % l1] == s2[i2 % l2]:
                if (i1 % l1, i2 % l2) in d:
                    prev1, prev2 = d[(i1 % l1, i2 % l2)]
                    cir1, cir2 = i1 - prev1, i2 - prev2
                    count_cir1 = (tot - i1) // cir1
                    i1 += count_cir1 * cir1
                    i2 += count_cir1 * cir2
                    if i1 >= tot: break
                else:
                    d[(i1 % l1, i2 % l2)] = (i1, i2)
                i2 += 1
            i1 += 1
        return i2 // l2 // n2


s1, n1 = "acb", 4
s2, n2 = "ab", 2
print(Solution().getMaxRepetitions2(s1, n1, s2, n2))
