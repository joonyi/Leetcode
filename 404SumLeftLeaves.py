"""
Find the sum of all left leaves in a given binary tree.
"""
from TreeNode import TreeNode
class Solution(object):
    def sumOfLeftLeaves(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return 0

        def Traverse(root, left):
            if not root:
                return 0
            if not root.left and not root.right and left == 1:
                self.sum += root.val
                return

            if root.left:
                Traverse(root.left, 1)
            if root.right:
                Traverse(root.right, 0)

        self.sum = 0
        Traverse(root.left, 1)
        Traverse(root.right, 0)
        return self.sum

    def sumOfLeftLeaves2(self, root):
        # Cleaner code
        if not root: return 0
        res = 0
        if root.left:
            if not root.left.left and not root.left.right:
                res += root.left.val
            else:
                res += self.sumOfLeftLeaves2(root.left)
        res += self.sumOfLeftLeaves2(root.right)
        return res


A = [3,9,20,None,None,15,7]
# A = [1]
root = TreeNode(None).BuildTree(A)
print(Solution().sumOfLeftLeaves2(root))
