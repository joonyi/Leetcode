class Solution(object):
    def romanToInt(self, s):
        """
        :type s: str
        :rtype: int
        """
        if not s: return None
        total = 0
        prev = ''
        sym = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(len(s)):
            if prev == "I" and (s[i] == "V" or s[i] == "X"):
                total += sym[s[i]] - sym["I"] - sym["I"]
            elif prev == "X" and (s[i] == "L" or s[i] == "C"):
                total += sym[s[i]] - sym["X"] - sym["X"]
            elif prev == "C" and (s[i] == "D" or s[i] == "M"):
                total += sym[s[i]] - sym["C"] - sym["C"]
            else:
                total += sym[s[i]]

            prev = s[i]


        return total


# s = "III"
# s = "IV"
# s = "IX"
# s = "LVIII"
s = "MCMXCIV"
print(Solution().romanToInt(s))