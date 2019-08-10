class Solution(object):
    def myAtoi(self, str):
        """
        :type str: str
        :rtype: int
        """

        s1 = ''
        signed = '+'
        for s in str: # strip whitespace
            if '0' <= s <= '9':
                s1 += s
            elif s == '-':
                signed = '-'

        if not s1:
            return s1
        if s1[0] < '0' or s1[0] > '9':
            return 0

        if signed == '-':
            s1 = '-' + s1

        convert = int(s1)
        if  convert <= -2*31:
            return -2147483648
        elif convert >= 2**32:
            return 2**32
        else:
            return convert



# str = "42"
# str = "   -42"
# str = "4193 with words"
str = "words and 987"
# str = "-91283472332"
# str = ""
print(Solution().myAtoi(str))

