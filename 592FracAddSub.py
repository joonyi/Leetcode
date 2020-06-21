"""
Given a string representing an expression of fraction addition and subtraction,
you need to return the calculation result in string format. The final result should be
irreducible fraction. If your final result is an integer, say 2, you need to change it to the
format of fraction that has denominator 1. So in this case, 2 should be converted to 2/1.
"""


class Solution:
    def fractionAddition(self, expression: str) -> str:
        signs = []
        fracs = []
        i = 0
        while i < len(expression):
            if expression[i] == '-' or expression[i] == '+':
                signs.append(expression[i])
                i += 1
            else:
                k = i
                while k < len(expression) and expression[k] != "-"  and expression[k] != "+":
                    k += 1
                fracs.append(expression[i:k ])
                if i == 0:
                    signs.append("+")
                i = k

        sums = [0, 1]
        for s, f in zip(signs, fracs):
            f = f.split("/")
            if s == "-":
                sums[0] = sums[0] * int(f[1]) - sums[1] * int(f[0])
                sums[1] = sums[1] * int(f[1])
            else:
                sums[0] = sums[0] * int(f[1]) + sums[1] * int(f[0])
                sums[1] = sums[1] * int(f[1])

        # Simplify
        n = self.gcd(sums[0], sums[1])
        if n:
            sums[0] //= n
            sums[1] //= n
        elif sums[0] == 0:
            sums[1] = 1

        return str(sums[0]) + "/" + str(sums[1])

    def gcd(self, x, y):
        while y:
            x, y = y, x % y

        return x

    def fractionAddition2(self, expression):
        import math, re
        ints = map(int, re.findall('[+-]?\d+', expression))
        A, B = 0, 1
        for a in ints:
            b = next(ints)
            A = A * b + a * B
            B *= b
            g = math.gcd(A, B)
            A //= g
            B //= g
        return '%d/%d' % (A, B)


# expression = "-1/2+1/2" # 0/1
# expression = "-1/2+1/2+1/3"  # 1/3
# expression = "1/3-1/2"  # -1/6
expression = "5/3+1/3"  # 2/1
expression = "-5/2+10/3+7/9"
print(Solution().fractionAddition2(expression))