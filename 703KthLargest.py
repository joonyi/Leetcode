"""
Design a class to find the kth largest element in a stream. Note that it is the kth largest element
in the sorted order, not the kth distinct element.

Your Kth Largest class will have a constructor which accepts an integer k and an integer array nums,
which contains initial elements from the stream. For each call to the method KthLargest.add,
return the element representing the kth largest element in the stream.

"""
import heapq
class KthLargest(object):
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
            heapq.heappush(self.pool, val)
            self.size += 1
        elif val > self.pool[0]:
            heapq.heapreplace(self.pool, val)
        return self.pool[0]

class KthLargest2(object):
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


k = 2
nums = [0]
obj = KthLargest2(k,nums)
print(obj.add(-1))
print(obj.add(1))
print(obj.add(-2))
print(obj.add(-4))
print(obj.add(3))
