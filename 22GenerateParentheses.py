"""
Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:
[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]
"""
class Solution:
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        ret = []
        open = n
        close = 0
        self.parenthesis(ret, "", open, close)
        return ret

    def parenthesis(self, ret, path, open, close):
        if open == 0 and close == 0:
            ret.append(path)
            return

        if open > 0:
            self.parenthesis(ret, path+"(", open-1, close+1)
        if close > 0:
            self.parenthesis(ret, path+")",open, close-1)

    def generateParenthesis2(self, n):
        def generate(p, left, right, parens=[]):
            if left:
                generate(p + '(', left - 1, right)
            if right > left:
                generate(p + ')', left, right - 1)
            if not right:
                parens += p, # Wow, what a trick. Comma for multiple assignment, so that equivalent to parens.append(p)
            return parens

        return generate('', n, n)


n = 3
print(Solution().generateParenthesis2(n))