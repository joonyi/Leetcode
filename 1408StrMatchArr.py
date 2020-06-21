"""
Given an array of string words. Return all strings in words which is substring of
another word in any order.

String words[i] is substring of words[j], if can be obtained removing some characters
to left and/or right side of words[j].
"""


class Solution(object):
    def stringMatching(self, words):
        """
        :type words: List[str]
        :rtype: List[str]
        """
        res = set()
        for i in range(len(words) - 1):
            for j in range(i + 1, len(words)):
                if len(words[i]) >= len(words[j]):
                    if words[j] in words[i]:
                        res.add(words[j])
                else:
                    if words[i] in words[j]:
                        res.add(words[i])
        return list(res)

    def stringMatching2 (self, words):
        arr = ' '.join(words)
        # subStr = [i for i in words if arr.count(i) >= 2]
        substr = []
        for i in words:
            if arr.count(i) >= 2:
                substr.append(i)

        return substr

words = ["mass","as","hero","superhero"]
# words = ["leetcode","et","code"]
words = ["leetcoder","leetcode","od","hamlet","am"]

print(Solution().stringMatching2(words))