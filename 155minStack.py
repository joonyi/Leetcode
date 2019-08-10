"""
Design a stack that supports push, pop, top, and retrieving the minimum element in constant time.

push(x) -- Push element x onto stack.
pop() -- Removes the element on top of the stack.
top() -- Get the top element.
getMin() -- Retrieve the minimum element in the stack.

Example:
MinStack minStack = new MinStack();
minStack.push(-2);
minStack.push(0);
minStack.push(-3);
minStack.getMin();   --> Returns -3.
minStack.pop();
minStack.top();      --> Returns 0.
minStack.getMin();   --> Returns -2.
"""


class MinStack(object):
    def __init__(self):
        self.stack = []

    def push(self, x):
        self.stack.append(x)

    def pop(self):
        del self.stack[-1]

    def top(self):
        return self.stack[-1]

    def getMin(self):
        # TLE
        # elem = self.stack[0]
        # for i in range(1,len(self.stack)):
        #     if self.stack[i] < elem:
        #         elem = self.stack[i]
        # return elem
        return min(self.stack)

obj = MinStack()
obj.push(-2)
obj.push(0)
obj.push(-3)
param_1 = obj.getMin()
obj.pop()
param_2 = obj.top()
param_3 = obj.getMin()
print(param_1,param_2,param_3)