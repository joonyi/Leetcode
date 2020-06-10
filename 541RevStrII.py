"""
Given a string and an integer k, you need to reverse the first k characters for every 2k characters
counting from the start of the string. If there are less than k characters left, reverse all of them.
If there are less than 2k but greater than or equal to k characters, then reverse the
first k characters and left the other as original.
"""
class Solution(object):
    def reverseStr(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: str
        """
        # For every block of 2k characters starting with position i,
        # we want to replace S[i:i+k] with it's reverse.
        a = list(s)
        for i in range(0, len(a), 2 * k):
            a[i:i + k] = reversed(a[i:i + k])
        return "".join(a)


s, k = 'abcdefg', 2
# s, k = 'abc', 3
print(Solution().reverseStr(s, k))