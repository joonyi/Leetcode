"""
Given a non-negative integer num represented as a string, remove k digits from
the number so that the new number is the smallest possible.

Note:
The length of num is less than 10002 and will be ≥ k.
The given num does not contain any leading zero.
"""

class Solution(object):
    def removeKdigits(self, num, k):
        """
        :type num: str
        :type k: int
        :rtype: str
        """
        res = []
        keep = len(num) - k
        for i in range(len(num)):
            while len(res) > 0 and res[-1] > num[i] and k > 0:
                res.pop()
                k -= 1
            res.append(num[i])

        res = res[:keep]

        # delete leading zero
        s = 0
        while s < len(res) - 1 and res[s] == "0":
            s += 1
        res = "".join(res[s:])

        if res == "":
            return "0"
        else:
            return res


    def removeKdigits2(self, num, k):
        res = []
        for i in range(len(num)):
            while len(res) > 0 and res[-1] > num[i] and k > 0:
                res.pop()
                k -= 1
            res.append(num[i])

        a = res[:-k or None]
        aa = ''.join(res[:-k or None]).lstrip('0')
        return ''.join(res[:-k or None]).lstrip('0') or '0'

    def removeKdigits3(self, num, k):
        while k > 0:
            k -= 1
            i = 0
            while i < len(num) - 1:
                # Compare with right digit
                if num[i] > num[i + 1]:
                    break
                i += 1
            num = num[:i] + num[i + 1:]  # remove current digit if right digit is smaller

        if len(num) == 0:
            return "0"
        else:
            return str(int(num))

num, k = "1432219", 3  # 1219
# num, k = "10200", 1  # 200
# num, k = "10", 2
# num, k = "9", 1
print(Solution().removeKdigits3(num, k))
