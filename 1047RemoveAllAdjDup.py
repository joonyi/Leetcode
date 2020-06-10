"""
Given a string S of lowercase letters, a duplicate removal consists of choosing two adjacent
and equal letters, and removing them.

We repeatedly make duplicate removals on S until we no longer can.

Return the final string after all such duplicate removals have been made.  It is guaranteed the
answer is unique.
"""


class Solution(object):
    def removeDuplicates(self, S):
        """
        :type S: str
        :rtype: str
        """
        stack = []
        for c in S:
            if not stack:
                stack.append(c)
                continue

            if c != stack[-1]:
                stack.append(c)
            else:
                stack.pop()

        return ''.join(stack)

S = "abbaca"
S = "a"
print(Solution().removeDuplicates(S))