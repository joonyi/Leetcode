"""
Given a string which consists of lowercase or uppercase letters, find the length of the
longest palindromes that can be built with those letters.

This is case sensitive, for example "Aa" is not considered a palindrome here.

Note:
Assume the length of given string will not exceed 1,010.
"""
class Solution(object):
    def longestPalindrome(self, s):
        """
        :type s: str
        :rtype: int
        """
        import collections
        count = collections.Counter(s)
        length = 0
        for i, val in count.items():
            if val >= 2:
                if val % 2 == 0:
                    length += val
                    count[i] -= val
                else:
                    length += val - 1
                    count[i] = count[i] - (val - 1)

        for i, val in count.items():
            if val == 1:
                return length + 1

        return length

    def longestPalindrome2(self, s):
        import collections
        ans = 0
        count = collections.Counter(s)
        for v in count.values():
            ans += v // 2 * 2 # if v even, ans add all, if v odd, ans add v - 1
            if ans % 2 == 0 and v % 2 == 1: # when v is odd, ans is even, there is an unique center, so add 1
                ans += 1
        return ans

s = "abccccdd"
# s = "ccc"
print(Solution().longestPalindrome2(s))