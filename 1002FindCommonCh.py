"""
Given an array A of strings made only from lowercase letters, return a list of all characters
that show up in all strings within the list (including duplicates).
For example, if a character occurs 3 times in all strings but not 4 times,
you need to include that character three times in the final answer.

You may return the answer in any order.
"""
class Solution(object):
    def commonChars(self, A):
        """
        :type A: List[str]
        :rtype: List[str]
        """
        import collections
        res = collections.Counter(A[0])
        for a in A:
            res &= collections.Counter(a) # & return min count of key, | return max count
        return list(res.elements())

    def commonChars2(self, A):
        cnt = [float('inf')] * 26
        for s in A:
            cnt1 = [0] * 26
            for c in s:
                cnt1[ord(c) - ord('a')] += 1
            for i in range(26):
                cnt[i] = min(cnt[i], cnt1[i])

        res = []
        for i in range(26):
            if cnt[i]:
                tmp = chr(i + ord('a'))
                res.extend(tmp* cnt[i])
        return res



# A = ["bella","label","roller"]
A = ["cool","lock","cook"]
print(Solution().commonChars2(A))