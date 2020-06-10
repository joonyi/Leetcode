"""
Given an absolute path for a file (Unix-style), simplify it. Or in other words,
convert it to the canonical path.

In a UNIX-style file system, a period . refers to the current directory.
Furthermore, a double period .. moves the directory up a level.

Note that the returned canonical path must always begin with a slash /, and there must be
only a single slash / between two directory names. The last directory name (if it exists)
must not end with a trailing /. Also, the canonical path must be the shortest string representing
the absolute path.
"""
class Solution(object):
    def simplifyPath(self, path):
        """
        :type path: str
        :rtype: str
        """
        dir = [p for p in path.split("/") if p != "." and p != ""]
        stack = []
        for p in dir:
            if p == "..":
                if stack:
                    stack.pop()
            else:
                stack.append(p)
        return "/" + "/".join(stack)

# path = "/home/" # /home
path = "/../" # /
# path = "/home//foo/" # /home/foo
# path = "/a/./b/../../c/"
# path = "/a/../../b/../c//.//"
# path = "/a//b////c/d//././/.."
print(Solution().simplifyPath(path))