"""
Design a HashMap without using any built-in hash table libraries.

To be specific, your design should include these functions:

put(key, value) : Insert a (key, value) pair into the HashMap. If the value already exists in the HashMap, update the value.
get(key): Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key.
remove(key) : Remove the mapping for the value key if this map contains the mapping for the key.
"""

class ListNode:
    def __init__(self, key, val):
        self.pair = (key, val)
        self.next = None

class MyHashMap:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        # Each index is a chain of linked list
        self.m = 1000
        self.h = [None] * self.m

    def put(self, key: int, value: int) -> None:
        """
        value will always be non-negative.
        """
        index = key % self.m
        if self.h[index] == None:
            self.h[index] = ListNode(key, value)
        else:
            cur = self.h[index]
            while True:
                if cur.pair[0] == key:
                    cur.pair = (key, value)  # update
                    return
                if cur.next == None:
                    break
                cur = cur.next
            cur.next = ListNode(key, value)

    def get(self, key: int) -> int:
        """
        Returns the value to which the specified key is mapped, or -1 if this map contains no mapping for the key
        """
        index = key % self.m
        cur = self.h[index]
        while cur:
            if cur.pair[0] == key:
                return cur.pair[1]
            else:
                cur = cur.next
        return -1

    def remove(self, key: int) -> None:
        """
        Removes the mapping of the specified value key if this map contains a mapping for the key
        """
        index = key % self.m
        cur = prev = self.h[index]
        if not cur: return
        if cur.pair[0] == key:
            self.h[index] = cur.next
        else:
            cur = cur.next
            while cur:
                if cur.pair[0] == key:
                    prev.next = cur.next
                    break
                else:
                    cur, prev = cur.next, prev.next

class MyHashMap2(object):
    # Just use array
    def __init__(self):
        self.table = [-1] * 1000001

    def put(self, key, value):
        self.table[key] = value

    def get(self, key):
        return self.table[key]

    def remove(self, key):
        self.table[key] = -1


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
print(obj.put(1, 1))
print(obj.put(2, 2))
print(obj.get(1))           # returns 1
print(obj.get(3))            # returns -1 (not found)
print(obj.put(2, 1))         # update the existing value
print(obj.get(2))            # returns 1
print(obj.remove(2))         # remove the mapping for 2
print(obj.get(2))            # returns -1
