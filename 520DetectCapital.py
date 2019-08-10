"""
Given a word, you need to judge whether the usage of capitals in it is right or not.

We define the usage of capitals in a word to be right when one of the following cases holds:

All letters in this word are capitals, like "USA".
All letters in this word are not capitals, like "leetcode".
Only the first letter in this word is capital if it has more than one letter, like "Google".
Otherwise, we define that this word doesn't use capitals in a right way.
"""


class Solution(object):
    def detectCapitalUse(self, word):
        """
        :type word: str
        :rtype: bool
        """

        if word.isupper():
            return True
        elif word.istitle():
            return True
        else:
            return word.islower()

    def detectCapitalUse2(self, word):
        return all('A' <= ch <= 'Z' for ch in word) or all('a' <= ch <= 'z' for ch in word) or ('A' <= word[0] <= 'Z' and all('a' <= ch <= 'z' for ch in word[1:]))

word = "adsfc"
print(Solution().detectCapitalUse2(word))