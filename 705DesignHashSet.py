"""
Design a HashSet without using any built-in hash table libraries.

To be specific, your design should include these functions:

add(value): Insert a value into the HashSet.
contains(value) : Return whether the value exists in the HashSet or not.
remove(value): Remove a value in the HashSet. If the value does not exist in the HashSet, do nothing.
"""
class MyHashSet(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.hashset = set()

    def add(self, key):
        """
        :type key: int
        :rtype: None
        """
        self.hashset.add(key)

    def remove(self, key):
        """
        :type key: int
        :rtype: None
        """
        if key in self.hashset:
            self.hashset.remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        return key in self.hashset


class MyHashSet2(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.cap = 10000
        self.size = 0
        self.set = [None] * self.cap

    def hash(self, key):
        return key % self.cap

    def add(self, key):
        """
        :type key: int
        :rtype: void
        """
        if self.contains(key):
            return

        hash_key = self.hash(key)
        if not self.set[hash_key]:
            self.set[hash_key] = []
        self.set[hash_key].append(key)  # chaining if collision

    def remove(self, key):
        """
        :type key: int
        :rtype: void
        """
        if not self.contains(key):
            return

        hash_key = self.hash(key)
        self.set[hash_key].remove(key)

    def contains(self, key):
        """
        Returns true if this set contains the specified element
        :type key: int
        :rtype: bool
        """
        hash_key = self.hash(key)
        if not self.set[hash_key]:
            return False
        for k in self.set[hash_key]:
            if k == key:
                return True
        return False

# Few methods in handling collision
# 1. Chaining, solution above
# 2. Open addressing, look for next free slot
# 3. Double hashing, use another hash function


obj = MyHashSet()
print(obj.remove(19))
print(obj.add(14))
print(obj.remove(19))
print(obj.remove(9))
print(obj.add(0))
print(obj.add(3))
print(obj.add(4))
print(obj.add(0))
print(obj.remove(9))