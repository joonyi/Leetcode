class MyQueue:
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.queue = []

    def push(self, x: int) -> None:
        """
        Push element x to the back of queue.
        """
        self.queue.append(x)

    def pop(self) -> int:
        """
        Removes the element from in front of queue and returns that element.
        """
        stk2 = []
        while self.queue:
            stk2.append(self.queue.pop())
        res = stk2.pop()
        while stk2:
            self.queue.append(stk2.pop())
        return res


    def peek(self) -> int:
        """
        Get the front element.
        """
        stk2 = []
        while self.queue:
            stk2.append(self.queue.pop())
        res = stk2[-1]
        while stk2:
            self.queue.append(stk2.pop())
        return res

    def empty(self) -> bool:
        """
        Returns whether the queue is empty.
        """
        return not self.queue

# Another idea is maintained an input stack and an output stack
# When pop or peek, move from one stack to another then do the operation

class MyQueue2(object):
    def __init__(self):
        """
        initialize your data structure here.
        """
        self.inStack, self.outStack = [], []

    def push(self, x):
        """
        :type x: int
        :rtype: nothing
        """
        self.inStack.append(x)

    def pop(self):
        """
        :rtype: nothing
        """
        self.move()
        return self.outStack.pop()

    def peek(self):
        """
        :rtype: int
        """
        self.move()
        return self.outStack[-1]

    def empty(self):
        """
        :rtype: bool
        """
        return (not self.inStack) and (not self.outStack)

    def move(self):
        """
        :rtype nothing
        """
        if not self.outStack:
            while self.inStack:
                self.outStack.append(self.inStack.pop())

obj = MyQueue2()
print(obj.push(1))
print(obj.push(2))
print(obj.peek())
print(obj.pop())
print(obj.empty())