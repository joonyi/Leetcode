"""
Given a string which contains only lowercase letters, remove duplicate letters so that
every letter appears once and only once. You must make sure your result is the smallest
in lexicographical order among all possible results.
"""
class Solution(object):
    def removeDuplicateLetters(self, s):
        """
        :type s: str
        :rtype: str
        """
        # Not working
        res  = []
        def recurse(S, n):
            if n < 0:
                res.append(S)
                return S
            if S.count(S[n]) > 1:
                dups = self.findDups(S, S[n])
                while dups:
                    S = recurse(S[:-1], n - 1)
                    dups.pop()
            else:
                S = recurse(S, n - 1)

        recurse(list(s), len(s) - 1)
        return res

    def findDups(self, S, c):
        res = []
        for i in range(len(S)):
            if S[i] == c:
                res.append(i)
        return res


    def removeDuplicateLetters2(self, s):
        rindex = {c: i for i, c in enumerate(s)}  # right most index
        result = ''
        for i, c in enumerate(s):
            if c not in result:
                # c < result[-1:] character smaller
                # i < rindex[result[-1]] there are duplicates behind
                while c < result[-1:] and i < rindex[result[-1]]:
                    result = result[:-1]
                result += c
        return result


    def removeDuplicateLetters3(self, s):
        # Greedy solution  the leftmost letter in the answer is the smallest s[i]
        for ch in sorted(set(s)):
            suffix = s[s.index(ch):]
            if set(suffix) == set(s):  # check if unique ch before s[s.index(ch):]
                tmp = self.removeDuplicateLetters3(suffix.replace(ch, ''))
                return ch + tmp
        return ''


    def removeDuplicateLetters4(self, s):
        '''
        count the frequency of every letter
        Maintain a monotone stack, if current letter is not in the stack, we need to check if top of stack, if stack's top is large and its count is more than 1, meaning there are letters behind, we should pop, until the top is less than current
        If current letter is already in the stack, just decrease its count
        '''
        import collections
        if not s:
            return ""
        stack = []
        cnt = collections.Counter(s)
        for ch in s:
            if ch not in stack:
                #  ch <= stack[-1] current ch is smaller
                #  cnt[stack[-1]] > 1 there are letters behind
                while stack and ch <= stack[-1] and cnt[stack[-1]] > 1:
                    cnt[stack.pop()] -= 1
                stack.append(ch)
            else:
                cnt[ch] -= 1
        return "".join(stack)


# s = "bcabc"
# s = "acbabc"
s = "cbacdcbc"
print(Solution().removeDuplicateLetters2(s))