class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        res = ''
        vowels = 'aeiouAEIOU'
        i, j = 0, len(s)-1
        while i < len(s):
            if s[i] in vowels:
                while s[j] not in vowels:
                    j -= 1
                res += s[j]
                j -= 1
            else:
                res += s[i]
            i += 1

        return res

    # This one faster
    def reverseVowels2(self, s):
        """
        :type s: str
        :rtype: str
        """
        input = list(s)
        left = 0
        right = len(s) - 1
        vowels = ['a', 'e', 'i', 'o', 'u', 'A', 'E', 'I', 'O', 'U']
        while left < right:
            if input[left] in vowels and input[right] in vowels:
                input[left], input[right] = input[right], input[left]
                left += 1
                right -= 1
            if input[left] not in vowels:
                left += 1
            if input[right] not in vowels:
                right -= 1

        return "".join(input)

# A = "hello"
A = "leetcode"
print(Solution().reverseVowels(A))