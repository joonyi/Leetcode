"""
Given a string containing just the characters '(' and ')', find the length of the longest valid
(well-formed) parentheses substring.
"""
class Solution(object):
    def longestValidParentheses(self, s):
        """
        :type s: str
        :rtype: int
        """
        maxans = 0
        stack = [-1]
        for i in range(len(s)):
            if s[i] == "(":
                stack.append(i)
            else:
                stack.pop()
                if not stack:
                    stack.append(i)
                else:
                    maxans = max(maxans, i - stack[-1])
        return maxans

    def longestValidParentheses2(self, s):
        left = right = maxlen = 0
        for i in range(len(s)):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                maxlen = max(maxlen, 2 * right)
            elif right > left:
                left = right = 0

        left = right = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == "(":
                left += 1
            else:
                right += 1

            if left == right:
                maxlen = max(maxlen, 2 * left)
            elif left > right:
                left = right = 0

        return maxlen

    def longestValidParentheses3(self, s):
        dp, stack = [0] * (len(s) + 1), []
        for i in range(len(s)):
            if s[i] == '(':
                stack.append(i)
            else:
                if stack:
                    p = stack.pop() # p is the position of '(' which can matches current ')' in the stack
                    dp[i + 1] = dp[p] + i - p + 1 
        return max(dp)

s = "(()"
# s = ")()())"
s = "()(())" # 6
s = "())((())" # 4
print(Solution().longestValidParentheses3(s))