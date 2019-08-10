"""
Implement a basic calculator to evaluate a simple expression string.

The expression string contains only non-negative integers, +, -, *, / operators and empty spaces .
The integer division should truncate toward zero.
"""
class Solution(object):
    def calculate(self, s):
        """
        :type s: str
        :rtype: int
        """
        if len(s) == 0: return 0
        elif len(s) == 1: return int(s[0])
        stack = []
        n1, n2 = 0, 0
        i = 0
        signed = 1
        while i < len(s):
            if s[i] == " ":
                i += 1
                continue
            n2 = n1
            n1 = s[i]
            if n1 == "+":
                stack.append(signed*int(n2))
                signed = 1
            elif n1 == "-":
                stack.append(signed * int(n2))
                signed = -1
            elif n1 == "*":
                i += 1
                while s[i] == " ": i += 1
                n1 = s[i]
                stack.append(signed*int(n2)*int(n1))
            elif n1 == "/":
                i += 1
                while s[i] == " ": i += 1
                n1 = s[i]
                stack.append(signed*int(int(n2)/int(n1)))
            i += 1
        return sum(stack)

    def calculate2(self, s):
        stack = []
        n = 0
        i = 0
        while i < len(s):
            if s[i].isdigit():
                n = n * 10 + int(s[i])
            elif s[i] == "+" or s[i] == "-":
                stack.append(n)
                stack.append(s[i])
                n = 0
            elif s[i] == "*":
                i += 1
                while s[i] == " ": i += 1
                n = n * int(s[i])
            elif s[i] == "/":
                i += 1
                while s[i] == " ": i += 1
                n = n // int(s[i])
            i += 1

        stack.append(n)
        res = stack[0]
        for i in range(1, len(stack), 2):
            if stack[i] == '+':
                res += stack[i+1]
            elif stack[i] == '-':
                res -= stack[i+1]

        return res


# s = "3-2*2"
# s = " 3/2 "
# s = " 3+5 / 2 "
s = "1*2-3/4+5*6-7*8+9/10"
print(Solution().calculate2(s))