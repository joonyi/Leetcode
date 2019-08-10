"""
Given a string s consists of upper/lower-case alphabets and empty space characters ' ',
return the length of last word in the string.

If the last word does not exist, return 0.

Note: A word is defined as a character sequence consists of non-space characters only.

Example:
Input: "Hello World"
Output: 5
"""
class Solution:
    def lengthOfLastWord(self, s):
        """
        :type s: str
        :rtype: int
        """

        s = list(s)
        # Trim the trailing space
        for _ in range(len(s)):
            if s[-1] == ' ':
                del (s[-1])

        if ' ' not in s:
            return len(s)
        else:
            i = -1
            word = []
            while s[i] != ' ':
                word.append(s[i])
                i -= 1
            return len(word)

    # rstrip trim the trailing space
    # strip trim leading and trailing space
    def lengthOfLastWord2(self, s):
        s = list(s.strip())
        if ' ' not in s:
            return len(s)
        else:
            i = -1
            word = []
            while s[i] != ' ':
                word.append(s[i])
                i -= 1
            return len(word)

    def lengthOfLastWord3(self, s):
        length = 0
        tail = len(s) - 1
        while tail >= 0 and s[tail] == ' ':
            tail -= 1
        while tail >= 0 and s[tail] != ' ':
            length += 1
            tail -= 1
        return length

    # worked??
    def lengthOfLastWord4(self, s):
        index = s.find(' ')
        return len(s) - index


input = "     "
print(Solution().lengthOfLastWord4(input))