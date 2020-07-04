"""
Given a string containing only three types of characters: '(', ')' and '*', write a function to check whether this string is valid. We define the validity of a string by these rules:

1. Any left parenthesis '(' must have a corresponding right parenthesis ')'.
2. Any right parenthesis ')' must have a corresponding left parenthesis '('.
3. Left parenthesis '(' must go before the corresponding right parenthesis ')'.
4. '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or
an empty string.
5. An empty string is also valid.
"""


class Solution:
    def checkValidString(self, s: str) -> bool:
        """
        [lo, hi] => number of ")" to balance
        When you met "(", you know you need one only one ")" to balance, lo = 1 and hi = 1.
        When you met "(*(", you know you need one/two/three ")" to balance, lo = 1 and hi = 3
        """
        lo = hi = 0
        for c in s:
            lo += 1 if c == '(' else -1
            hi += 1 if c != ')' else -1
            if hi < 0:  # hi -ve means ( appear before )
                break
            lo = max(lo, 0)

        return lo == 0

    def checkValidString2(self, s: str) -> bool:
        bal = 0
        #  check from left to right, take all '*'s as '(', to see whether can match all ')'s
        for c in s:
            if c == '(' or c == "*":
                bal += 1
            elif bal == 0:
                return False
            else:
                bal -= 1

        if bal == 0: return True

        bal = 0
        # check from right to left, take all '*'s as ')', to see whether can match all '('s
        for c in s[::-1]:
            if c == ")" or c == "*":
                bal += 1
            elif bal == 0:
                return False
            else:
                bal -= 1
        return True


s = "()"
s = "(*)"
# s = "(*))"
# s = "(***)"

print(Solution().checkValidString2(s))
