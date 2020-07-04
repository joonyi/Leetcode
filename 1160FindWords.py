"""
You are given an array of strings words and a string chars.

A string is good if it can be formed by characters from chars (each character can only be used once).

Return the sum of lengths of all good strings in words.
"""

from typing import List
class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        import collections
        chars_cnt = dict(collections.Counter(chars))
        res = 0
        for word in words:
            tmp = chars_cnt.copy()
            cnt = 0
            for c in word:
                if c in tmp and tmp[c] != 0:
                    tmp[c] -= 1
                    cnt += 1
                else:
                    cnt = 0
                    break
            res += cnt

        return res

    def countCharacters2(self, words: List[str], chars: str) -> int:
        import collections
        chars_cnt = collections.Counter(chars)
        cnt = 0
        for word in words:
            word_cnt = collections.Counter(word)
            if all([word_cnt[c] <= chars_cnt[c] for c in word_cnt]):
                cnt += len(word)
        return cnt



# words, chars = ["cat","bt","hat","tree"], "atach"
words, chars = ["hello", "world", "leetcode"], "welldonehoneyr"
print(Solution().countCharacters2(words, chars))
