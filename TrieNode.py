class TrieNode(object):
    def __init__(self):
        self.isEnd = False
        self.contains = {}

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