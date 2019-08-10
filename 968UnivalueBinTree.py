"""
A binary tree is univalued if every node in the tree has the same value.

Return true if and only if the given tree is univalued.
"""
from TreeNode import *
class Solution(object):
    def isUnivalTree(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def check(root, x):
            if not root:
                return True
            return root.val == x and check(root.left, x) and check(root.right, x)

        return check(root, root.val)


# A = [1,1,1,1,1,None,1]
A = [2,2,2,5,2]
root = TreeNode().BuildTree(A)
print(Solution().isUnivalTree(root))