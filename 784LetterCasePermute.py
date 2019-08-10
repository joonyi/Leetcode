"""
Given a string S, we can transform every letter individually to be lowercase or uppercase
to create another string.  Return a list of all possible strings we could create.
"""

class Solution(object):
    def letterCasePermutation(self, S):
        """
        :type S: str
        :rtype: List[str]
        """
        def Permute(S, path, res, i):
            if i == len(S):
                res.append(path)
                return

            if S[i].isdigit():
                Permute(S, path + S[i], res, i + 1)
            else:
                Permute(S, path + S[i].lower(), res, i + 1)
                Permute(S, path + S[i].upper(), res, i + 1)

        res = []
        Permute(S, '', res, 0)
        return res

S = "12345"
print(Solution().letterCasePermutation(S))
