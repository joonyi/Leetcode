"""
Given a string text, you want to use the characters of text to form as many instances
of the word "balloon" as possible.

You can use each character in text at most once. Return the maximum number of
instances that can be formed.
"""


class Solution:
    def maxNumberOfBalloons(self, text: str) -> int:
        alpha = [0] * 26
        for c in text:
            alpha[ord(c) - ord('a')] += 1

        cnt = 0
        while True:
            for c in "balloon":
                i = ord(c) - ord('a')
                alpha[i] -= 1
                if alpha[i] < 0:
                    return cnt
            cnt += 1

    def maxNumberOfBalloons2(self, text: str) -> int:
        import collections
        cnt = collections.Counter(text)
        cntBalloon = collections.Counter('balloon')
        res = []
        for c in cntBalloon:
            res.append(cnt[c] // cntBalloon[c])
        return min(res)


text = "nlaebolko"  # 1
text = "loonbalxballpoon"  # 2
# text = "leetcode"  # 0
print(Solution().maxNumberOfBalloons2(text))
