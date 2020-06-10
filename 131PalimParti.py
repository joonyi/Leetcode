"""
Given a string s, partition s such that every substring of the partition is a palindrome.

Return all possible palindrome partitioning of s.
"""
class Solution(object):
    def partition(self, s):
        """
        :type s: str
        :rtype: List[List[str]]
        """
        def search(s, path, res):
            if not s:
                res.append(path)
                return

            for i in range(1, len(s) + 1):
                tmp = s[:i]
                if tmp[::-1] == tmp:
                    search(s[i:], path+[s[:i]], res)

        res = []
        search(s, [], res)
        return res

s = "aab"
print(Solution().partition(s))