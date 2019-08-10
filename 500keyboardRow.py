"""
Given a List of words, return the words that can be typed using letters of alphabet
on only one row's of American keyboard like the image below: QWERTY keyboard
"""

class Solution(object):
    def findWords(self, words):
        first = set('qwertyiuopQWERTYUIOP')
        second = set('asdfghjklASDFGHJKL')
        third = set('zxcvbnmZXCVBNM')
        ret = []
        for word in words:
            if word[0] in first:
                row = first
            elif word[0] in second:
                row = second
            else:
                row = third

            for i in range(1,len(word)):
                if word[i] not in row:
                    break
            else:
                ret.append(word)

        return ret

    def findWords2(self, words):
        line1, line2, line3 = set('qwertyuiop'), set('asdfghjkl'), set('zxcvbnm')
        ret = []
        for word in words:
            w = set(word.lower())
            if w.issubset(line1) or w.issubset(line2) or w.issubset(line3):
                ret.append(word)
        return ret

input = ["Aasdfghjkl","Qwertyuiop","zZxcvbnm"]
print(Solution().findWords(input))

