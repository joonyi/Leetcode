"""
Design a data structure that supports all following operations in average O(1) time.

insert(val): Inserts an item val to the set if not already present.
remove(val): Removes an item val from the set if present.
getRandom: Returns a random element from current set of elements. Each element must have
the same probability of being returned.
"""

class RandomizedSet:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.container = []

    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """
        if val in self.container:
            return False

        self.container.append(val)
        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """
        if val in self.container:
            self.container.remove(val)
            return True
        return False

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        from random import randint
        n = randint(0, len(self.container) - 1)
        return self.container[n]


class RandomizedSet2(object):
    # This one fastest
    # Have one more dict to store index for quick remove
    def __init__(self):
        self.nums, self.pos = [], {}

    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False

    def remove(self, val):
        # Get the target val to the list end and pop
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop()
            self.pos.pop(val, 0)
            return True
        return False

    def getRandom(self):
        import random
        n = random.randint(0, len(self.nums) - 1)
        return self.nums[n]


# Your RandomizedSet object will be instantiated and called as such:
obj = RandomizedSet2()
print(obj.insert(1))  # T
print(obj.remove(2))  # F
print(obj.insert(2))  # T
print(obj.getRandom())  # 1 or 2
print(obj.remove(1))  # T
print(obj.insert(2))  # F
print(obj.getRandom())
