"""
Given a string, you need to reverse the order of characters in each word within a
sentence while still preserving whitespace and initial word order.
"""

class Solution(object):
    def reverseWords(self, s):
        """
        :type s: str
        :rtype: str
        """
        word = ""
        sentence = ""
        for c in s:
            if c != " ":
                word = c + word
            else:
                sentence += word + " "
                word = ""

        sentence += word
        return sentence

    # This is very fast
    def reverseWords2(self, s):
        return " ".join(i[::-1] for i in s.split())

s = "Let's take LeetCode contest"
print(Solution().reverseWords(s))