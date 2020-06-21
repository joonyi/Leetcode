"""
Design a data structure that supports the following two operations:

void addWord(word)
bool search(word)

search(word) can search a literal word or a regular expression string containing
only letters a-z or .. A . means it can represent any one letter.
"""
from TrieNode import TrieNode
class WordDictionary:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        r = self.root
        for c in word:
            if c not in r.contains:
                r.contains[c] = TrieNode()
            r = r.contains[c]
        r.isEnd = True

    def search(self, word: str) -> bool:
        """
        Returns if the word is in the data structure. A word could contain the dot character '.'
        to represent any one letter.
        """
        def dfs(word, node):
            for i in range(len(word)):
                if word[i] == "." and node.contains:
                    x = []
                    for c in node.contains.keys():
                        x.append(dfs(word[i + 1:], node.contains[c]))
                    return any(x)

                elif word[i] in node.contains:
                    node = node.contains[word[i]]
                else:
                    return False
            return node.isEnd

        return dfs(word, self.root)

class WordDictionary2:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.root = TrieNode()

    def addWord(self, word: str) -> None:
        """
        Adds a word into the data structure.
        """
        r = self.root
        for c in word:
            if c not in r.contains:
                r.contains[c] = TrieNode()
            r = r.contains[c]
        r.isEnd = True

    def search(self, word: str) -> bool:
        def dfs(node, word):
            if not word:
                if node.isEnd:
                    self.res = True
                return
            if word[0] == ".":
                for n in node.contains.values():
                    dfs(n, word[1:])
            else:
                node = node.contains.get(word[0])
                if not node:
                    return
                dfs(node, word[1:])

        self.res = False
        dfs(self.root, word)
        return self.res


# Your WordDictionary object will be instantiated and called as such:
# obj = WordDictionary()
# obj.addWord("at"); obj.addWord("and"); obj.addWord("an"); obj.addWord("add")
# print(obj.search("a"))  # F
# print(obj.search(".at"))  # F
# obj.addWord("bat")
# print(obj.search(".at"))  # T
# print(obj.search("an."))  # T
# print(obj.search("a.d."))  # F
# print(obj.search("b."))  # F
# print(obj.search("a.d"))  # T
# print(obj.search("."))  # F

# obj = WordDictionary()
# obj.addWord("bad")
# obj.addWord("dad")
# obj.addWord("mad")
# print(obj.search("pad")) # F
# print(obj.search("bad")) # T
# print(obj.search(".ad")) # T
# print(obj.search("b..")) # T
# print(obj.search("...")) # T

obj = WordDictionary()
obj.addWord("a")
obj.addWord("a")
print(obj.search(".")) # T
print(obj.search("a")) # T
print(obj.search("aa")) # F
print(obj.search("a")) # T
print(obj.search(".a")) # F
print(obj.search("a.")) # F



