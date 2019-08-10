"""
Given a string, determine if it is a palindrome, considering only alphanumeric characters
and ignoring cases.

Note: For the purpose of this problem, we define empty string as valid palindrome.
"""
class Solution(object):
    def isPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        text = ''
        for c in s:
            if c.isalnum():
                text += c.lower()

        i = 0
        j = len(text) - 1
        while i < j:
            if text[i] == text[j]:
                i += 1
                j -= 1
            else:
                return False

        return True

    def isPalindrome2(self, s):
        i, j = 0, len(s)-1
        while i < j:
            while i < j and not s[i].isalnum():
                i += 1
            while i < j and not s[j].isalnum():
                j -= 1
            if s[i].lower() != s[j].lower():
                return False
            i += 1
            j -= 1

        return True


s = "A man, a plan, a canal: Panama"
# s = "race a car"
print(Solution().isPalindrome2(s))