"""
For strings S and T, we say "T divides S" if and only if S = T + ... + T
(T concatenated with itself 1 or more times)

Return the largest string X such that X divides str1 and X divides str2.
"""
class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        if len(str1) == len(str2):
            return str1 if str1==str2 else ''

        elif len(str1) < len(str2):
            return self.gcdOfStrings(str2, str1)  # Swap str1 str2
        elif str1[:len(str2)] == str2:
            return self.gcdOfStrings(str1[len(str2):],str2)
        else:
            return ''

    def gcdOfStrings2(self, str1: str, str2: str) -> str:
        def gcd(a, b):
            return b if a == 0 else gcd(b % a, a)

        d = gcd(len(str1), len(str2))
        # gcd multiply by prefix should be the same another string
        if str1[:d] * (len(str2) // d) == str2 and str2[: d] * (len(str1) // d) == str1:
            return str1[: d]
        else:
            return ''


str1, str2 = "ABCABC", "ABC"
str1, str2 = "ABABAB", "ABAB"
str1, str2 = "LEET", "CODE"
print(Solution().gcdOfStrings2(str1, str2))


