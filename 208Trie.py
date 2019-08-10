class Trie(object):
    def __init__(self):
        self.root = {}

    def Insert(self, word):
        p = self.root
        for c in word:
            if c not in p:
                p[c] = {}
            p = p[c]
            p['#'] = True

    def Search(self, word):
        node = self.find(word)
        return node is not None and '#' in node

    def StartWith(self, prefix):
        return self.find(prefix) is not None

    def find(self, prefix):
        p = self.root
        for c in prefix:
            if c not in p:
                return None
            p = p[c]
        return p