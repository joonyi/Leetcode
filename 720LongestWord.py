"""
Given a list of strings words representing an English Dictionary, find the longest word in words
that can be built one character at a time by other words in words. If there is more than one possible answer, return the longest word with the smallest lexicographical order.

If there is no answer, return the empty string.
"""
class Solution(object):
    def longestWord(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        # Whenever our found word would be superior, we check if all it's prefixes are present, then replace our answer.
        res = ""
        wordset = set(words)
        for word in words:
            if len(word) > len(res) or len(word) == len(res) and word < res: # only allow longer words and less lexicographical words
                if all(word[:k] in wordset for k in range(1, len(word))): # check if all prefixes present
                    res = word

        return res

    def longestWord2(self, words):
        """
        :type words: List[str]
        :rtype: str
        """
        valid = set()
        valid.add("")

        for word in sorted(words, key=lambda x: len(x)):
            if word[:-1] in valid:
                valid.add(word)

        return max(sorted(valid), key=lambda x: len(x)) # to return smaller lexicographically

# words = ["w","wo","wor","worl", "world"]
words = ["a", "banana", "app", "appl", "ap", "apply", "apple"]
print(Solution().longestWord2(words))