"""
Given two integers representing the numerator and denominator of a fraction,
return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.
"""


class Solution(object):
    def fractionToDecimal(self, numerator, denominator):
        """
        :type numerator: int
        :type denominator: int
        :rtype: str
        """
        res = ""
        if numerator / denominator < 0:
            res += "-"
        if numerator % denominator == 0:
            return str(numerator / denominator)
        numerator = abs(numerator)
        denominator = abs(denominator)
        res += str(numerator / denominator)
        res += "."
        numerator %= denominator
        i = len(res)
        table = {}
        while numerator != 0:
            if numerator not in table.keys():
                table[numerator] = i
            else:
                i = table[numerator]
                res = res[:i] + "(" + res[i:] + ")"
                return res
            numerator = numerator * 10
            res += str(numerator / denominator)
            numerator %= denominator
            i += 1
        return res

    def fractionToDecimal2(self, numerator, denominator):
        n, remainder = divmod(abs(numerator), abs(denominator))
        sign = '-' if numerator * denominator < 0 else ''
        result = [sign + str(n), '.']
        stack = []
        while remainder not in stack: # if remainder repeat, so does dividend
            stack.append(remainder)
            n, remainder = divmod(remainder * 10, abs(denominator)) # this is how we do division. multiply 10 then divide again
            result.append(str(n))

        idx = stack.index(remainder)
        result.insert(idx + 2, '(')
        result.append(')')
        return ''.join(result).replace('(0)', '').rstrip('.')

numerator = 2
denominator = 1
print(Solution().fractionToDecimal2(numerator, denominator))