class Solution(object):
    def groupAnagrams(self, strs):
        """
        :type strs: List[str]
        :rtype: List[List[str]]
        """
        from collections import defaultdict
        anagrams = defaultdict(list)
        for word in strs:
            alpha = [0] * 26
            for c in word:
                alpha[ord(c) - ord('a')] += 1

            anagrams[tuple(alpha)].append(word)
        return list(anagrams.values())

    def groupAnagrams2(self, strs):
        from collections import defaultdict
        anagrams = defaultdict(list)
        for s in strs:
            anagrams[tuple(sorted(s))].append(s)
        return list(anagrams.values())

    def groupAnagrams3(self, strs):
        prime = [2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 41, 43, 47, 53, 59, 61, 67, 71, 73, 79, 83, 89, 97, 101, 103]
        res = []
        m_dict = {}
        for s_str in strs:
            key = 1
            for s_char in s_str:
                key *= prime[ord(s_char) - ord('a')]

            if key in m_dict:
                index = m_dict.get(key)
                t = res[index]
                t.append(s_str)
            else:
                t = [s_str]
                res.append(t)
                m_dict[key] = len(res) - 1
        return res


strs = ["eat", "tea", "tan", "ate", "nat", "bat"]
print(Solution().groupAnagrams3(strs))