"""
We are given two sentences A and B.  (A sentence is a string of space separated words.
Each word consists only of lowercase letters.)

A word is uncommon if it appears exactly once in one of the sentences,
and does not appear in the other sentence.

Return a list of all uncommon words.
You may return the list in any order.
"""

class Solution(object):
    def uncommonFromSentences(self, A, B):
        """
        :type A: str
        :type B: str
        :rtype: List[str]
        """
        A = A.split()
        B = B.split()
        dict = {}
        for word in A:
            if word not in dict:
                dict[word] = 1
            else:
                dict[word] += 1

        for word in B:
            dict[word] = dict.get(word, 0) + 1

        res = []
        for key, val in dict.items():
            if val == 1:
                res.append(key)
        return res

# A = "apple apple"
# B = "banana"
A = "this apple is sweet"
B = "this apple is sour"
print(Solution().uncommonFromSentences(A, B))