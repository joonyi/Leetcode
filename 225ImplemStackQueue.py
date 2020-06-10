class MyStack(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.stack = []

    def push(self, x):
        """
        Push element x onto stack.
        :type x: int
        :rtype: None
        """
        self.stack.append(x)

    def pop(self):
        """
        Removes the element on top of the stack and returns that element.
        :rtype: int
        """
        q = []
        while self.stack:
            q.append(self.stack.pop())
        res = q.pop(0)
        while q:
            self.stack.append(q.pop())
        return res

    def top(self):
        """
        Get the top element.
        :rtype: int
        """
        q = []
        while self.stack:
            q.append(self.stack.pop())
        res = q[0]
        while q:
            self.stack.append(q.pop())
        return res

    def empty(self):
        """
        Returns whether the stack is empty.
        :rtype: bool
        """
        return not self.stack

class MyStack2(object):
    def __init__(self):
        import collections
        self._queue = collections.deque()

    def push(self, x):
        # "push to front" by pushing to back and then rotating the queue until the new element is at the front
        # Only one queue
        q = self._queue
        q.append(x)
        for _ in range(len(q) - 1):
            q.append(q.popleft())

    def pop(self):
        return self._queue.popleft()

    def top(self):
        return self._queue[0]

    def empty(self):
        return not len(self._queue)

# Your MyStack object will be instantiated and called as such:
obj = MyStack()
print(obj.push(1))
# print(obj.push(2))
# print(obj.push(3))
# print(obj.top())
print(obj.pop())
print(obj.empty())