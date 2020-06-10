"""
Your friend is typing his name into a keyboard.  Sometimes, when typing a character c,
the key might get long pressed, and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.  Return True if it is possible that it was your
friends name, with some characters (possibly none) being long pressed.
"""
class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        i = 0
        prev = ''
        for c in typed:
            if i < len(name) and c == name[i]:
                i += 1
            elif c == prev:
                continue
            else:
                return False
            prev = c

        return i == len(name)

    def isLongPressedName2(self, name, typed):
        # Group into blocks
        """
        For example, 'aaleex' is a long-pressed version of 'alex': because when considering the
        groups [('a', 2), ('l', 1), ('e', 2), ('x', 1)] and [('a', 1), ('l', 1), ('e', 1), ('x', 1)],
        they both have the key 'alex', and the count [2,1,2,1] is at least [1,1,1,1] when making an
        element-by-element comparison (2 >= 1, 1 >= 1, 2 >= 1, 1 >= 1).
        """
        import itertools
        g1 = [(k, len(list(grp))) for k, grp in itertools.groupby(name)]
        g2 = [(k, len(list(grp))) for k, grp in itertools.groupby(typed)]
        if len(g1) != len(g2):
            return False

        return all(k1 == k2 and v1 <= v2 for (k1, v1), (k2, v2) in zip(g1, g2))

name, typed = "alex", "aaleex" #T
# name, typed = "saeed", "ssaaedd" #F
# name, typed = "leelee", "lleeelee" #T
# name, typed = "laiden", "laiden" #T
# name, typed = "vtkgn", "vttkgnn" #T
# name, typed = "pyplrz", "ppyypllr" #F
print(Solution().isLongPressedName2(name, typed))