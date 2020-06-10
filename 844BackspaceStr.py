"""
Given two strings S and T, return if they are equal when both are typed into empty text editors.
# means a backspace character.
"""
class Solution(object):
    def backspaceCompare(self, S, T):
        """
        :type S: str
        :type T: str
        :rtype: bool
        """
        # Build string. The redundant code could be avoided with function
        back = 0
        s = ''
        i = len(S) - 1
        while i > -1:
            if S[i] == '#':
                back += 1
                i -= 1
                continue
            if back == 0:
                s += S[i]
            else:
                back -= 1
            i -= 1

        back = 0
        t = ''
        i = len(T) - 1
        while i > -1:
            if T[i] == '#':
                back += 1
                i -= 1
                continue
            if back == 0:
                t += T[i]
            else:
                back -= 1
            i -= 1

        return s == t

    def backspaceCompare2(self, S, T):
        # Build stack
        res = []
        for s in S:
            if not res:
                if s != '#':
                    res.append(s)
            else:
                if s != '#':
                    res.append(s)
                else:
                    res.pop()

        res2 = []
        for t in T:
            if not res2:
                if t != '#':
                    res2.append(t)
            else:
                if t != '#':
                    res2.append(t)
                else:
                    res2.pop()
        return res == res2

# Another idea is two pointer

# S, T = 'ab#c', 'ad#c' #T
# S, T = "ab##", "c#d#" #T
# S, T = "a##c", "#a#c" #T
S, T = "a#c", "b" #F
S, T = "y#fo##f", "y#f#o##f"
print(Solution().backspaceCompare2(S, T))



