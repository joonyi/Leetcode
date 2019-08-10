"""
Your friend is typing his name into a keyboard.
Sometimes, when typing a character c, the key might get long pressed,
and the character will be typed 1 or more times.

You examine the typed characters of the keyboard.
Return True if it is possible that it was your friends name,
with some characters (possibly none) being long pressed.
"""

class Solution(object):
    def isLongPressedName(self, name, typed):
        """
        :type name: str
        :type typed: str
        :rtype: bool
        """
        # Not working
        i, j = 0, 0
        prev = typed[0]
        while i < len(name) and j < len(typed):
            if name[i] == typed[j]:
                prev = typed[j]
                i += 1
                j += 1
            elif typed[j] == prev:
                j += 1

        if i == len(name):
            return True
        else:
            return False


# name = "alex"
# typed = "aaleex"
name = "saeed"
typed = "ssaaedd"
print(Solution().isLongPressedName(name, typed))