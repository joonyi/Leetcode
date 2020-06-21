"""
Implement a magic directory with buildDict, and search methods.

For the method buildDict, you'll be given a list of non-repetitive words to build a dictionary.

For the method search, you'll be given a word, and judge whether if you modify exactly one character
into another character in this word, the modified word is in the dictionary you just built.
"""

class MagicDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.wordsdict = {}

    def buildDict(self, dict: [str]) -> None:
        """
        Build a dictionary through a list of words
        """
        for i in dict:
            self.wordsdict[len(i)] = self.wordsdict.get(len(i), []) + [i]

    def search(self, word: str) -> bool:
        """
        Returns if there is any word in the trie that equals to the given word after modifying exactly one character
        """
        for candi in self.wordsdict.get(len(word), []):
            countdiff = 0
            for j in range(len(word)):
                if candi[j] != word[j]:
                    countdiff += 1
            if countdiff == 1:
                return True
        return False


from TrieNode import TrieNode
class MagicDictionary2(object):
    def __init__(self):
        self.root = TrieNode()

    def buildDict(self, dict):
        for word in dict:
            r = self.root
            for chr in word:
                if chr not in r.contains:
                    r.contains[chr] = TrieNode()
                r = r.contains[chr]  # move to next node
            r.isEnd = True

    def search(self, word):
        def findWord(remain, r, word):
            if not word:
                return True if remain == 0 and r.isEnd else False
            for key in r.contains.keys():
                if key == word[0]:
                    if findWord(remain, r.contains[key], word[1:]):
                        return True
                elif remain == 1:
                    if findWord(0, r.contains[key], word[1:]):
                        return True
            return False

        return findWord(1, self.root, word)

import collections
class MagicDictionary3(object):

    def yield_neighbor(self, word):
        # if word is 'apple' Generate '*pple', 'a*ple', 'ap*le', 'app*e', 'appl*'
        for i in range(len(word)):
            yield word[:i] + '*' + word[i + 1:]

    def buildDict(self, words):
        self.words = set(words)
        # if word is 'apple' generates '*pple', 'a*ple', 'ap*le', 'app*e', 'appl*'
        cand = [word[:i] + '*' + word[i + 1:] for word in words for i in range(len(word))]
        self.near = collections.Counter(cand)

    def search(self, word):
        candidates = [word[:i] + '*' + word[i + 1:] for i in range(len(word))]
        return any(self.near[cand] > 1 or
                   self.near[cand] == 1 and word not in self.words
                   for cand in candidates)


# Your MagicDictionary object will be instantiated and called as such:
obj = MagicDictionary3()
words = ["hello", "hallo", "leetcode"]
# word = "hhllo"  # T
word = "hello"  # F


obj.buildDict(words)
print(obj.search(word))