"""
Given string S and a dictionary of words words, find the number of words[i] that is a subsequence of S.

Example :
Input:
S = "abcde"
words = ["a", "bb", "acd", "ace"]
Output: 3

Explanation: There are three words in words that are a subsequence of S: "a", "acd", "ace".
Note:
All words in words and S will only consists of lowercase letters.
The length of S will be in the range of [1, 50000].
The length of words will be in the range of [1, 5000].
The length of words[i] will be in the range of [1, 50].
"""
class Solution(object):
    def numMatchingSubseq(self, S, words):
        """
        :type S: str
        :type words: List[str]
        :rtype: int
        """
        # TLE
        def Search(S, start, path, res):
            if start > len(S):
                return
            if path in words and path not in res:
                self.cnt += d[path]
                res.append(path)
            for i in range(start, len(S)):
                Search(S, i + 1, path + S[i], res)

        d = {}
        for word in words:
            if word not in d:
                d[word] = 1
            else:
                d[word] += 1
        self.cnt = 0
        res = []
        Search(S, 0, '', res)
        return self.cnt, res

    def numMatchingSubseq2(self, S, words):
        import collections
        waiting = collections.defaultdict(list)
        for w in words:
            waiting[w[0]].append(iter(w[1:]))
        for c in S:
            for it in waiting.pop(c, ()):
                waiting[next(it, None)].append(it)
        return len(waiting[None])


    def numMatchingSubseq3(self, S, words):
        # slow
        def check(s, i):
            for c in s:
                i = S.find(c, i) + 1 # string.find(value, start, end)
                if not i: return False
            return True

        return sum((check(word, 0) for word in words))

    def numMatchingSubseq4(self, S, words):
        import collections
        word_dict = collections.defaultdict(list)
        count = 0

        for word in words:
            word_dict[word[0]].append(word)

        for char in S:
            words_expecting_char = word_dict[char]
            word_dict[char] = []
            for word in words_expecting_char:
                if len(word) == 1:
                    # Finished subsequence!
                    count += 1
                else:
                    word_dict[word[1]].append(word[1:])

        return count


S, words = "abcde", ["a", "bb", "acd", "ace"] # 3
# S, words = "dsahjpjauf", ["ahjpjau","ja","ahbwzgqnuk","tnmlanowax"]
# S, words = "qlhxagxdqh", ["qlhxagxdq","qlhxagxdq","lhyiftwtut","yfzwraahab"]
print(Solution().numMatchingSubseq4(S, words))

