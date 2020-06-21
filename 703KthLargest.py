"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

Your Kth Largest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.

"""
import heapq
class KthLargest(object):
    """
    Create a pq - keep it only having the k-largest elements by popping off small elements.
    With only k elements, the smallest item (self.pool[0]) will always be the kth largest.

    If a new value is bigger than the smallest, it should be added into your heap.
    If it's bigger than the smallest (that are already the kth largest), it will certainly be within the kth largest of the stream.
    """
    def __init__(self, k, nums):
        self.pool = nums
        self.k = k
        self.size = len(self.pool)
        heapq.heapify(self.pool)
        while self.size > k:
            heapq.heappop(self.pool)
            self.size -= 1

    def add(self, val):
        if self.size < self.k:
            heapq.heappush(self.pool, val)  # Pop and return the smallest item from the heap, and also push the new item
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

class KthLargest2(object):
    # This not working
    def __init__(self, k, nums):
        nums.sort(reverse=True)
        self.pool = nums[:k]
        self.k = k

    def add(self, val):
        if self.k == len(self.pool) and self.pool[-1] >= val:
            return self.pool[-1]

        left = 0
        right = len(self.pool) - 1
        while left < right:
            mid = (left + right) // 2
            if self.pool[mid] < val:
                right = mid
            else:
                left = mid + 1
        self.pool.insert(left, val)
        if len(self.pool) > self.k:
            self.pool.pop()
        return self.pool[-1]


from typing import List
class KthLargest3:
    def __init__(self, k: int, nums: List[int]):
        self.arr = sorted(nums)
        self.k = k

    def add(self, val: int) -> int:
        self.arr.append(val)
        self.arr.sort()
        return self.arr[-self.k]



k, nums = 2, [0]
obj = KthLargest(k,nums)
print(obj.add(-1))  # -1
print(obj.add(1))  # 0
print(obj.add(-2))  # 0
print(obj.add(-4))  # 0
print(obj.add(3))  # 1
