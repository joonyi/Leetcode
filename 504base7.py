"""
Given an integer, return its base 7 string representation.

Example 1:
Input: 100
Output: "202"

Example 2:
Input: -7
Output: "-10"

Note: The input will be in range of [-1e7, 1e7].
"""

class Solution:
    def convertToBase7(self, num):
        """
        :type num: int
        :rtype: str
        """
        digit = 1
        result = 0
        convertBack = 0 # for negative
        if num < 0:
            num = num * -1
            convertBack = 1

        while num > 0:
            result += (num % 7) * digit
            digit *= 10
            num = num // 7

        if convertBack == 1:
            result = result * -1

        return str(result)

num = -7
print(Solution().convertToBase7(num))