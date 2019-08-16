"""
Implement function ToLowerCase() that has a string parameter str, and returns the same string in lowercase.
"""

class Solution(object):
    def toLowerCase(self, str):
        """
        :type str: str
        :rtype: str
        """
        res = ''
        for s in str:
            if 65 <= ord(s) <= 90:
                s = chr(ord(s) + 32)
            res += s
        return res

# str = "Hello"
# str = "here"
str = "LOVELY"
print(Solution().toLowerCase(str))