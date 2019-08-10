"""
Given a non-empty string s, you may delete at most one character.
Judge whether you can make it a palindrome.
"""
class Solution(object):
    def validPalindrome(self, s):
        """
        :type s: str
        :rtype: bool
        """
        # Brute force TLE
        def isPalindrome(s):
            i, j = 0, len(s) - 1
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

        s1 = ''
        for i in range(len(s)):
            s1 = s[:i] + s[i+1:]
            if isPalindrome(s1): return True
        return False

    def validPalindrome2(self, s):
        def is_pali_range(i, j):
            return all(s[k] == s[j - k + i] for k in range(i, j))

        for i in range(len(s) // 2):
            if s[i] != s[~i]:
                j = len(s) - 1 - i
                return is_pali_range(i + 1, j) or is_pali_range(i, j - 1)
        return True

    def validPalindrome3(self, s):
        # Time: O(n)
        # Space: O(n)
        """
        Whenever there is a mismatch, we can either exclude the character
        at the left or the right pointer. We then take the two remaining
        substrings and compare against its reversed and see if either one is a
        palindrome.
        """

        left, right = 0, len(s) - 1
        while left < right:
            if s[left] != s[right]:
                one, two = s[left:right], s[left + 1:right + 1]
                return one == one[::-1] or two == two[::-1]
            left, right = left + 1, right - 1
        return True



s = "abca"
print(Solution().validPalindrome3(s))
