"""
Given a string of numbers and operators, return all possible results from computing all the
different possible ways to group numbers and operators. The valid operators are +, - and *.
"""
class Solution(object):
    def diffWaysToCompute(self, input):
        """
        :type input: str
        :rtype: List[int]
        """
        if input.isdigit():
            return [int(input)]
        res = []
        for i in range(len(input)):
            if input[i] in "-+*":
                res1 = self.diffWaysToCompute(input[:i])
                res2 = self.diffWaysToCompute(input[i + 1:])
                for j in res1:
                    for k in res2:
                        res.append(self.helper(j, k, input[i]))
        return res

    def helper(self, m, n, op):
        if op == "+":
            return m + n
        elif op == "-":
            return m - n
        else:
            return m * n


input = "2-1-1"
# input = "2*3-4*5"
print(Solution().diffWaysToCompute(input))