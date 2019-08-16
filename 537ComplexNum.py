"""
Given two strings representing two complex numbers.
You need to return a string representing their multiplication. Note i2 = -1 according to the definition.
"""
class Solution(object):
    def complexNumberMultiply(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        def FormatInput(s):
            s = s.split("+")
            re = int(s[0])
            im = complex(s[1][:-1] + "j")
            return re + im

        product = FormatInput(a) * FormatInput(b)
        re = str(int(product.real)) + "+"
        im = str(int(product.imag)) + "i"

        return re + im

    def complexNumberMultiply2(self, a, b):
        a1, a2 = map(int, a[:-1].split('+'))
        b1, b2 = map(int, b[:-1].split('+'))
        return '%d+%di' % (a1 * b1 - a2 * b2, a1 * b2 + a2 * b1)


# a, b = "1+1i", "1+1i" # "0+2i
a, b = "1+-1i", "1+-1i" # "0+-2i"
# a, b = "1+0i", "1+0i"
# a, b = "20+22i", "-18+-10i" # "-140+-596i"
print(Solution().complexNumberMultiply2(a, b))