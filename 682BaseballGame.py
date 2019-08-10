"""
You're now a baseball game point recorder.

Given a list of strings, each string can be one of the 4 following types:

Integer (one round's score): Directly represents the number of points you get in this round.
"+" (one round's score): Represents that the points you get in this round are the sum of the last two valid round's points.
"D" (one round's score): Represents that the points you get in this round are the doubled data of the last valid round's points.
"C" (an operation, which isn't a round's score): Represents the last valid round's points you get were invalid and should be removed.
Each round's operation is permanent and could have an impact on the round before and the round after.

You need to return the sum of the points you could get in all the rounds.
"""

class Solution(object):
    def calPoints(self, ops):
        """
        :type ops: List[str]
        :rtype: int
        """
        stack = []
        sum = 0
        for op in ops:
            try:
                op = int(op)
                stack.append(op)
                sum += op
            except:
                if op == "C":
                    last = stack.pop()
                    sum -= last
                elif op == "D":
                    stack.append(stack[-1]*2)
                    sum += stack[-1]
                elif op == "+":
                    stack.append(stack[-1]+stack[-2])
                    sum += stack[-1]
        return sum

    def calPoints2(self, ops):
        stack = []
        sum = 0
        for op in ops:
            if op == "C":
                last = stack.pop()
                sum -= last
            elif op == "D":
                stack.append(stack[-1] * 2)
                sum += stack[-1]
            elif op == "+":
                stack.append(stack[-1] + stack[-2])
                sum += stack[-1]
            else:
                stack.append(int(op))
                sum += stack[-1]
        return sum

ops = ["5","-2","4","C","D","9","+","+"]
print(Solution().calPoints2(ops))



