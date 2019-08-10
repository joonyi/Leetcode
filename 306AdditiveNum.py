"""
Additive number is a string whose digits can form additive sequence.

A valid additive sequence should contain at least three numbers. Except for the first two numbers,
each subsequent number in the sequence must be the sum of the preceding two.

Given a string containing only digits '0'-'9', write a function to determine if it's an additive number.

Note: Numbers in the additive sequence cannot have leading zeros, so sequence 1, 2, 03 or 1, 02, 3
is invalid.
"""


class Solution(object):
    def isAdditiveNumber(self, num):
        """
        :type num: str
        :rtype: bool
        """
        L = len(num)
        # choose the first number A
        for i in range(1, L//2 + 1):
            # A cannot start with a 0 if its length is more than 1
            if num[0] == '0' and i > 1:
                break
            # choose the second number B
            j = i + 1
            while L - j >= j - i and L - j >= i:
                # B cannot start with a 0 if its length is more than 1
                if num[i] == '0' and j -i >= 2:
                    break
                num1 = int(num[:i]) # A
                num2 = int(num[i:j]) # B
                substr = num[j:] # remaining string

                j += 1

                if self.isAdditive(substr, num1, num2):
                    return True
        return False

    def isAdditive(self, substr, num1, num2):
        if substr == "":
            return True

        total = num1 + num2
        s = str(total)

        if not substr.startswith(s):
            return False

        return self.isAdditive(substr[len(s):], num2, total)

    def isAdditiveNumber2(self, num):
        import itertools
        n = len(num)
        for i, j in itertools.combinations(range(1, n), 2):
            a, b = num[:i], num[i:j]
            if a != str(int(a)) or b != str(int(b)):
                continue
            # if a != str(int(a)):
            #     a = str(int(a))
            while j < n:
                c = str(int(a) + int(b))
                if not num.startswith(c, j):
                    break
                j += len(c)
                a, b = b, c
            if j == n:
                return True
        return False

# num = "113358" # False
# num = "199100199"
# num = "211738"
# num = "0235813"
num = "101"
print(Solution().isAdditiveNumber(num))