class Solution(object):
    def intToRoman(self, num):
        """
        :type num: int
        :rtype: str
        """
        res = ''
        unit = ["","I","II","III","IV","V","VI","VII","VIII","IX"]
        ten = ["","X","XX","XXX","XL","L","LX","LXX","LXXX","XC"]
        hund = ["","C","CC","CCC","CD","D","DC","DCC","DCCC","CM"]
        thou = ["","M","MM","MMM"]
        u = 0
        while num > 0:
            d = num % 10
            if u == 0:
                res += unit[d]
            elif u == 1:
                res = ten[d] + res
            elif u == 2:
                res = hund[d] + res
            else:
                res = thou[d] + res

            u += 1
            num //= 10

        return res

num = 58
print(Solution().intToRoman(num))