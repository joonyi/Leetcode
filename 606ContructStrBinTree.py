"""
You need to construct a string consists of parenthesis and integers from a binary tree
with the preorder traversing way.

The null node needs to be represented by empty parenthesis pair "()". And you need to omit
all the empty parenthesis pairs that don't affect the one-to-one mapping relationship between
the string and the original binary tree.
Example 1:
Input: Binary tree: [1,2,3,4]
       1
     /   \
    2     3
   /
  4
Output: "1(2(4))(3)"
Explanation: Originallay it needs to be "1(2(4)())(3()())",
but you need to omit all the unnecessary empty parenthesis pairs.
And it will be "1(2(4))(3)".

Example 2:
Input: Binary tree: [1,2,3,null,4]
       1
     /   \
    2     3
     \
      4

Output: "1(2()(4))(3)"
Explanation: Almost the same as the first example,
except we can't omit the first parenthesis pair to break the one-to-one mapping
relationship between the input and the output.
"""
from TreeNode import TreeNode
class Solution(object):
    def tree2str(self, t):
        if not t:
            return ""

        ret = str(t.val)
        left = self.tree2str(t.left)
        right = self.tree2str(t.right)

        if not left and not right:
            return ret
        if not left:
            return ret + "()" + "(" + right + ")"
        if not right:
            return ret + "(" + left + ")"
        return ret + "(" + left + ")" + "(" + right + ")"

    def tree2str2(self, t):
        if not t:
            return ""
        ret = str(t.val)
        if t.left:
            ret += "(" + self.tree2str2(t.left) + ")"
        elif t.right:
            ret += "()"
        if t.right:
            ret += "(" + self.tree2str2(t.right) + ")"
        return ret


A = [1,2,3,4]
tree = TreeNode().BuildTree(A)
print(Solution().tree2str(tree))
