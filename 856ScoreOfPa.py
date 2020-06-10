"""
Given a balanced parentheses string S, compute the score of the string based on the following rule:

1. () has score 1
2. AB has score A + B, where A and B are balanced parentheses strings.
3. (A) has score 2 * A, where A is a balanced parentheses string.
"""
class Solution(object):
    def scoreOfParentheses(self, S):
        """
        :type S: str
        :rtype: int
        """
        def dfs(i, j):
            res = bal = 0
            for k in range(i, j):
                if S[k] == '(':
                    bal += 1
                else:
                    bal -= 1
                if bal == 0:
                    if k - i == 1:
                        res += 1
                    else:
                        res += 2 * dfs(i+1, k)
                    i = k + 1
            return res

        return dfs(0, len(S))

    def scoreOfParentheses2(self, S):
        """
        Our goal is to maintain the score at the current depth we are on.
        When we see an opening bracket, we increase our depth, and our score at the new depth is 0.
        When we see a closing bracket, we add twice the score of the previous deeper part
        """
        stack = [0]  # The score of the current frame
        for x in S:
            if x == '(':
                stack.append(0) # zero so that () will give +1
            else:
                v = stack.pop()
                stack[-1] += max(2 * v, 1)

        return stack.pop()

    def scoreOfParentheses3(self, S):
        ans = bal = 0
        for i, x in enumerate(S):
            if x == '(':
                bal += 1
            else:
                bal -= 1
                if S[i - 1] == '(':
                    ans += 1 << bal
        return ans



# S = "()"
# S = "(())"
# S = "()()"
S = "(()(()))"
print(Solution().scoreOfParentheses3(S))