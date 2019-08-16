"""
Given a column title as appear in an Excel sheet, return its corresponding column number.
For example:

    A -> 1
    B -> 2
    C -> 3
    ...
    Z -> 26
    AA -> 27
    AB -> 28

Example 1:
Input: "A"
Output: 1

Example 2:
Input: "AB"
Output: 28

Example 3:
Input: "ZY"
Output: 70
"""

class Solution(object):
    def titleToNumber(self, s):
        """
        :type s: str
        :rtype: int
        """
        # Observe that this is basically the same thing as converting between base 26 and base 10.
        # For s = "BCM" the final solution would be (2 x 26 x 26) + (3 x 26) + (13)
        s = s[::-1]
        sum = 0
        for exp, char in enumerate(s):
            sum += (ord(char) - 65 + 1) * (26 ** exp)
        return sum

    def titleToNumber2(self, s):
        res = 0
        for i in s:
            res = res * 26 + ord(i) - ord('A') + 1
        return res

s = "AB"
print(Solution().titleToNumber2(s))

