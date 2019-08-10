"""
Given a string, find the first non-repeating character in it and return it's index.
If it doesn't exist, return -1.

Examples:
s = "leetcode"
return 0.

s = "loveleetcode",
return 2.

Note: You may assume the string contain only lowercase letters.
"""
from collections import OrderedDict
class Solution(object):
    def firstUniqChar(self, s):
        """
        :type s: str
        :rtype: int
        """
        dict = OrderedDict()
        for char in s:
            if char not in dict:
                dict[char] = 1
            else:
                dict[char] += 1

        # print(dict)
        for key, val in dict.items():
            if val == 1:
                return s.find(key)

        return -1

    # Check which 26 char appear one time in s
    # return to lowest index
    def firstUniqChar2(self, s):
        letters = 'abcdefghijklmnopqrstuvwxyz'
        lst = [s.index(l) for l in letters if s.count(l) == 1]
        if len(lst) > 0:
            return min(lst)
        else:
            return -1

s = "leetcode"
print(Solution().firstUniqChar2(s))