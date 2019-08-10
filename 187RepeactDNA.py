"""
All DNA is composed of a series of nucleotides abbreviated as A, C, G, and T,
for example: "ACGAATTCCG". When studying DNA, it is sometimes useful to identify
repeated sequences within the DNA.

Write a function to find all the 10-letter-long sequences (substrings) that
occur more than once in a DNA molecule.
"""
class Solution(object):
    def findRepeatedDnaSequences(self, s):
        """
        :type s: str
        :rtype: List[str]
        """
        res, record = set(), set()
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            # [record, r][substring in record].add(substring)
            if substring in record:
                res.add(substring)
            else:
                record.add(substring)
        return list(res)

    def findRepeatedDnaSequences2(self, s):
        # TLE bcs set.add() is O(1), list.append is O(n)
        res, record = set(), []
        for i in range(len(s) - 9):
            substring = s[i:i + 10]
            # [record, r][substring in record].add(substring)
            if substring in record:
                res.add(substring)
            else:
                record.append(substring)
        return res

    def findRepeatedDnaSequences3(self, s):
        # Karp-Rabin Algorithm
        if len(s) < 10:
            return []
        tags, N, base = {"A": 0, "C": 1, "G": 2, "T": 3}, 10, 4
        cache, repeats = set([]), set([])
        number, factor = 0, 1
        for i in range(N):
            number, factor = number * base + tags[s[i]], factor * base
        factor /= base  # Pre-compute 4^9
        cache.add(number)
        for i in range(N, len(s)):
            number = (number - tags[s[i - N]] * factor) * base + tags[s[i]]
            if number in cache:
                repeats.add(s[i - (N - 1):i + 1])
            else:
                cache.add(number)
        return [x for x in repeats]

# s = "AAAAACCCCCAAAAACCCCCCAAAAAGGGTTT"
s = "AAAAAAAAAAAA"
print(Solution().findRepeatedDnaSequences3(s))