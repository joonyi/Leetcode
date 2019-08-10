class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        A = 0
        B = 0
        for i in range(-1, -(len(a)+1), -1):
            if a[i] == "1":
                A +=  2**-(i+1)
        for i in range(-1, -(len(b) + 1), -1):
            if b[i] == "1":
                B += 2**-(i+1)
        C = A + B
        if C == 0:
            return "0"
        res = ""
        while C > 0:
            if C % 2 == 1:
                res = "1" + res
            else:
                res = "0" + res
            C //= 2

        return res

print(Solution().addBinary("1","2"))