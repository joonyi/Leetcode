"""
Design your implementation of the circular queue. The circular queue is a linear data structure
in which the operations are performed based on FIFO (First In First Out) principle and the
last position is connected back to the first position to make a circle. It is also called "Ring Buffer".

One of the benefits of the circular queue is that we can make use of the spaces in front of the queue.
In a normal queue, once the queue becomes full, we cannot insert the next element even if there is a
space in front of the queue. But using the circular queue, we can use the space to store new values.

Your implementation should support following operations:

MyCircularQueue(k): Constructor, set the size of the queue to be k.
Front: Get the front item from the queue. If the queue is empty, return -1.
Rear: Get the last item from the queue. If the queue is empty, return -1.
enQueue(value): Insert an element into the circular queue. Return true if the operation is successful.
deQueue(): Delete an element from the circular queue. Return true if the operation is successful.
isEmpty(): Checks whether the circular queue is empty or not.
isFull(): Checks whether the circular queue is full or not.
"""


class MyCircularQueue(object):
    def __init__(self, k):
        """
        Initialize your data structure here. Set the size of the queue to be k.
        :type k: int
        """
        self.front = 0
        self.rear = 0
        self.k = k + 1
        self.queue = [None] * self.k

    def enQueue(self, value):
        """
        Insert an element into the circular queue. Return true if the operation is successful.
        :type value: int
        :rtype: bool
        """
        if self.isFull():
            return False
        else:
            self.queue[self.rear] = value
            self.rear = (self.rear - 1) % self.k
            return True

    def deQueue(self):
        """
        Delete an element from the circular queue. Return true if the operation is successful.
        :rtype: bool
        """
        if self.isEmpty():
            return False
        else:
            self.front = (self.front - 1) % self.k
            return True

    def Front(self):
        """
        Get the front item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[self.front]

    def Rear(self):
        """
        Get the last item from the queue.
        :rtype: int
        """
        if self.isEmpty():
            return -1
        else:
            return self.queue[(self.rear + 1) % self.k]

    def isEmpty(self):
        """
        Checks whether the circular queue is empty or not.
        :rtype: bool
        """
        return self.front == self.rear

    def isFull(self):
        """
        Checks whether the circular queue is full or not.
        :rtype: bool
        """
        return (self.front + 1) % self.k == self.rear


# Your MyCircularQueue object will be instantiated and called as such:
k = 4
value = 2
obj = MyCircularQueue(8)
print(obj.enQueue(3))
print(obj.enQueue(9))
print(obj.enQueue(5))
print(obj.enQueue(0))
print(obj.deQueue())
print(obj.deQueue())

print(obj.isEmpty())
print(obj.isEmpty())
print(obj.Rear())
print(obj.Rear())
print(obj.deQueue())



