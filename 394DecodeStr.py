"""
Given an encoded string, return it's decoded string.

The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets
is being repeated exactly k times. Note that k is guaranteed to be a positive integer.

You may assume that the input string is always valid; No extra white spaces, square brackets
are well-formed, etc.

Furthermore, you may assume that the original data does not contain any digits and that digits
are only for those repeat numbers, k. For example, there won't be input like 3a or 2[4].
"""
class Solution(object):
    def decodeString(self, s):
        stack = []
        n = 0
        res = ''
        for c in s:
            if c == '[':
                stack.append(res)
                stack.append(n)
                res = ''
                n = 0
            elif c == ']':
                repeat = stack.pop()
                prev = stack.pop()
                res = prev + repeat * res
            elif c.isdigit():
                n = n * 10 + int(c) # might more than 1 digit
            else:
                res += c
        return res

    def decodeString2(self, s):
        # Idea two stack, one for count, one for result till now
        res = ''
        cntStack = []
        resStack = []
        i = 0
        while i < len(s):
            if s[i].isdigit():
                cnt = 0
                while s[i].isdigit(): # get all the digits
                    cnt = int(s[i])
                    i += 1
                cntStack.append(cnt)
            elif s[i] == '[':
                resStack.append(res)
                res = ''
                i += 1
            elif s[i] == ']':
                tmp = resStack.pop()
                repeat = cntStack.pop()
                for _ in range(repeat):
                    tmp += res
                res = tmp
                i += 1
            else:
                res += s[i]
                i += 1

        return res


# s = "3[a]2[bc]"
# s = "3[a2[c]]"
s = "2[abc]3[cd]ef"
print(Solution().decodeString(s))