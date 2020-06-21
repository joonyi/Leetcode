"""
Implement a trie with insert, search, and startsWith methods.
"""
from TrieNode import TrieNode
class Trie:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def insert(self, word: str) -> None:
        """
        Inserts a word into the trie.
        """
        r = self.root
        for c in word:
            if c not in r.contains:
                r.contains[c] = TrieNode()
            r = r.contains[c]
        r.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the trie.
        """
        r = self.root
        for c in word:
            if c in r.contains:
                r = r.contains[c]
            else:
                return False

        return r.isEnd

    def startsWith(self, prefix: str) -> bool:
        """
        Returns if there is any word in the trie that starts with the given prefix.
        """
        r = self.root
        for c in prefix:
            if c in r.contains:
                r = r.contains[c]
            else:
                return False
        return True


trie = Trie()
trie.insert("apple")
print(trie.search("apple"))  # true
print(trie.search("app"))    # false
print(trie.startsWith("app"))  # true
trie.insert("app")
print(trie.search("app"))     # true