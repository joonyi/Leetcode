"""
Given a nested list of integers represented as a string, implement a parser to deserialize it.

Each element is either an integer, or a list -- whose elements may also be integers or other lists.

Note: You may assume that the string is well-formed:
String is non-empty.
String does not contain white spaces.
String contains only digits 0-9, [, - ,, ].
"""
# """
# This is the interface that allows for creating nested lists.
# You should not implement it, or speculate about its implementation
# """
#class NestedInteger(object):
#    def __init__(self, value=None):
#        """
#        If value is not specified, initializes an empty list.
#        Otherwise initializes a single integer equal to value.
#        """
#
#    def isInteger(self):
#        """
#        @return True if this NestedInteger holds a single integer, rather than a nested list.
#        :rtype bool
#        """
#
#    def add(self, elem):
#        """
#        Set this NestedInteger to hold a nested list and adds a nested integer elem to it.
#        :rtype void
#        """
#
#    def setInteger(self, value):
#        """
#        Set this NestedInteger to hold a single integer equal to value.
#        :rtype void
#        """
#
#    def getInteger(self):
#        """
#        @return the single integer that this NestedInteger holds, if it holds a single integer
#        Return None if this NestedInteger holds a nested list
#        :rtype int
#        """
#
#    def getList(self):
#        """
#        @return the nested list that this NestedInteger holds, if it holds a nested list
#        Return None if this NestedInteger holds a single integer
#        :rtype List[NestedInteger]
#        """

class Solution(object):
    def deserialize(self, s):
        nums = set('1234567890-')
        stack = []
        i = 0
        while i < len(s):
            if s[i] == '[':
                stack.append(s[i])
            elif s[i] in nums:
                int_s = s[i]
                while i < len(s) - 1 and s[i + 1] in nums:
                    i += 1
                    int_s += s[i]
                stack.append(int(int_s))
            elif s[i] == ']':
                lst = []
                while stack[-1] != '[':
                    lst.append(stack.pop())
                stack.pop()
                lst.reverse()
                stack.append(lst)
            i += 1
        return stack[0]

    def deserialize2(self, s):
        def nestedInteger():
            num = ''
            while s[-1] in '1234567890-':
                num += s.pop()
            if num:
                return NestedInteger(int(num))
            s.pop()
            lst = NestedInteger()
            while s[-1] != ']':
                lst.add(nestedInteger())
                if s[-1] == ',':
                    s.pop()
            s.pop()
            return lst

        s = list(' ' + s[::-1])
        return nestedInteger()


# s = "[123,[456,[789]]]"
s = "324"
print(Solution().deserialize(s))


