"""
Given a string array words, find the maximum value of length(word[i]) * length(word[j])
where the two words do not share common letters. You may assume that each word will contain
only lower case letters. If no such two words exist, return 0.
"""
class Solution(object):
    def maxProduct(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        d = {}
        for w in words:
            mask = 0
            for c in set(w):
                mask |= (1 << (ord(c) - 97)) # smart bin repre of words
            d[mask] = max(d.get(mask, 0), len(w))
        # return max([d[x] * d[y] for x in d for y in d if not x & y] or [0])
        res = 0
        for x in d:
            for y in d:
                if not x & y: # check two words share common letters
                    res = max(res, d[x] * d[y])

        return res

words = ["abcw","baz","foo","bar","xtfn","abcdef"]
print(Solution().maxProduct(words))