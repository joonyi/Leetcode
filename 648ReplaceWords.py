"""
In English, we have a concept called root, which can be followed by some other words
to form another longer word - let's call this word successor. For example, the root an,
followed by other, which can form another word another.

Now, given a dictionary consisting of many roots and a sentence. You need to replace
all the successor in the sentence with the root forming it. If a successor
has many roots can form it, replace it with the root with the shortest length.

You need to output the sentence after the replacement.
"""
from typing import List
from TrieNode import TrieNode
class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        r = self.root
        for c in word:
            if c not in r.contains:
                r.contains[c] = TrieNode()
            r = r.contains[c]
        r.isEnd = True

    def startsWith(self, prefix: str) -> bool:
        r = self.root
        for c in prefix:
            if c in r.contains:
                r = r.contains[c]
            else:
                return False
        return True

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        # Naive solution
        sentence = sentence.split()
        for i in range(len(sentence)):
            trie = Trie()
            trie.insert(sentence[i])
            for word in dict:
                if trie.startsWith(word):
                    sentence[i] = word
                    trie = Trie()
                    trie.insert(sentence[i])

        return ' '.join(sentence)

    def replaceWords2(self, roots, sentence):
        rootset = set(roots)
        def replace(word):
            for i in range(1, len(word)):
                if word[:i] in rootset:
                    return word[:i]
            return word

        return " ".join(map(replace, sentence.split()))

    def replaceWords3(self, dict, sentence):
        trie = {}
        for word in dict:
            t = trie
            for ch in word:
                if ch not in t:
                    t[ch] = {}
                t = t[ch]
            t['#'] = '#'

        def process(string):
            node = trie
            for i, ch in enumerate(string):
                if ch not in node:
                    break
                node = node[ch]  # move to next node
                if '#' in node:  # Return when meeting first end
                    return string[:i + 1]
            return string

        sentence = sentence.split()
        for i in range(len(sentence)):
            sentence[i] = process(sentence[i])
        return ' '.join(sentence)
        # return ' '.join(map(process, sentence.split()))


dict = ["cat","bat","rat"]
sentence = "the cattle was rattled by the battery"
print(Solution().replaceWords3(dict, sentence))
