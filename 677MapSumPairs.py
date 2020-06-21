"""
Implement a MapSum class with insert, and sum methods.

For the method insert, you'll be given a pair of (string, integer).
The string represents the key and the integer represents the value.
If the key already existed, then the original key-value pair will be overridden to the new one.

For the method sum, you'll be given a string representing the prefix,
and you need to return the sum of all the pairs' value whose key starts with the prefix.
"""
class MapSum(object):
    def __init__(self):
        self.root = dict()

    def insert(self, key, val):
        self.root[key] = val

    def sum(self, prefix):
        sums = 0
        for key in self.root:
            if key.startswith(prefix):
                sums += self.root[key]
        return sums
        # return sum(self.d[i] for i in self.d if i.startswith(prefix))


class TrieNode():
    def __init__(self, count=0):
        self.count = count
        self.children = {}

class MapSum(object):
    def __init__(self):
        self.root = TrieNode()
        self.keys = {}

    def insert(self, key, val):
        # Time: O(k)
        curr = self.root
        # determine if the string already exists in the Trie
        # If it does, we calculate the difference in the previous and new value
        delta = val - self.keys.get(key, 0)
        self.keys[key] = val
        curr.count += delta

        for char in key:
            if char not in curr.children:
                curr.children[char] = TrieNode()
            curr = curr.children[char]
            curr.count += delta

    def sum(self, prefix):
        # Time: O(k)
        curr = self.root
        for char in prefix:
            if char not in curr.children:
                return 0
            curr = curr.children[char]
        return curr.count


# Your MapSum object will be instantiated and called as such:
obj = MapSum()
# obj.insert("aa", 3)
# print(obj.sum("a"))  # 3
# obj.insert("aa", 2)
# print(obj.sum("a"))  # 2

obj.insert("apple", 3)
print(obj.sum("ap"))  # 3
obj.insert("app", 2)
print(obj.sum("ap"))  # 5