"""
Given the root node of a binary search tree, return the sum of values of all nodes with value
between L and R (inclusive).

The binary search tree is guaranteed to have unique values.
"""
from TreeNode import TreeNode
class Solution(object):
    def rangeSumBST(self, root, L, R):
        """
        :type root: TreeNode
        :type L: int
        :type R: int
        :rtype: int
        """
        if not root:
            return root

        def Traverse(root, L, R):
            if not root:
                return
            if root.val < L:
                Traverse(root.right, L, R)
            elif root.val > R:
                Traverse(root.left, L, R)
            else:
                self.sum += root.val
                Traverse(root.right, L, R)
                Traverse(root.left, L, R)

        self.sum = 0
        Traverse(root, L, R)
        return self.sum

    def rangeSumBST2(self, root, L, R):
        def Traverse(root):
            if not root:
                return
            if L <= root.val <= R:
                self.sum += root.val
            if L < root.val:
                Traverse(root.left)
            if root.val < R:
                Traverse(root.right)

        self.sum = 0
        Traverse(root)
        return self.sum

A, L, R = [10,5,15,3,7,None,18], 7 ,15
A, L, R = [10,5,15,3,7,13,18,1,None,6], 6, 10
root = TreeNode(None).BuildTree(A)
print(Solution().rangeSumBST2(root, L, R))