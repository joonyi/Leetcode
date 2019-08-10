class Solution(object):
    def findReplaceString(self, S, indexes, sources, targets):
        """
        :type S: str
        :type indexes: List[int]
        :type sources: List[str]
        :type targets: List[str]
        :rtype: str
        """
        # S = list(S)
        ret = ''
        i = 0
        for index in indexes:
            if S[index:index+len(sources[i])] == sources[i]:
                ret += targets[i]
            i += 1
        return ret


S = "abcd"
indexes = [0,2]
sources = ["a","cd"]
targets = ["eee","ffff"]
print(Solution().findReplaceString(S, indexes, sources, targets))
