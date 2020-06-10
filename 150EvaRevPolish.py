"""
Evaluate the value of an arithmetic expression in Reverse Polish Notation.

Valid operators are +, -, *, /. Each operand may be an integer or another expression.

Note:
Division between two integers should truncate toward zero.
The given RPN expression is always valid. That means the expression would always evaluate to a
result and there won't be any divide by zero operation.
"""
class Solution(object):
    def evalRPN(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        stack = []
        for t in tokens:
            if not stack:
                stack.append(int(t))
                continue

            if t == '+':
                a = stack.pop()
                b = stack.pop()
                stack.append(a + b)
            elif t == '*':
                a = stack.pop()
                b = stack.pop()
                stack.append(a * b)
            elif t == '/':
                a = stack.pop()
                b = stack.pop()
                stack.append(int(b / a))
            elif t == '-':
                a = stack.pop()
                b = stack.pop()
                stack.append(b - a)
            else:
                stack.append(int(t))

        return stack[0]

    def evalRPN2(self, tokens):
        """
        :type tokens: List[str]
        :rtype: int
        """
        if len(tokens) < 1:
            return None
        ops = {
            '+': lambda y, x: x + y,
            '-': lambda y, x: x - y,
            '*': lambda y, x: x * y,
            '/': lambda y, x: int(x / y)
        }
        result = []
        for token in tokens:
            if token in ops.keys():
                result.append(ops[token](result.pop(), result.pop()))
            else:
                result.append(int(token))
        return result[0]

# tokens = ["2", "1", "+", "3", "*"] #9
# tokens = ["4", "13", "5", "/", "+"] #6
tokens = ["10", "6", "9", "3", "+", "-11", "*", "/", "*", "17", "+", "5", "+"] #22
# tokens = ["4", "3", "-"]
print(Solution().evalRPN(tokens))