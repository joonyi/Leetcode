"""
Given a binary tree, return the tilt of the whole tree.

The tilt of a tree node is defined as the absolute difference between
the sum of all left subtree node values and the sum of all right subtree node values.
Null node has tilt 0.

The tilt of the whole tree is defined as the sum of all nodes' tilt.
"""
from TreeNode import *
class Solution(object):
    def findTilt(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        def dfs(root, res):
            if not root:
                return 0

            left = dfs(root.left, res)
            right = dfs(root.right, res)
            tilt = abs(left - right)
            res.append(tilt)
            return left + right + root.val

        res = []
        dfs(root, res)
        return sum(res)

    def findTilt2(self, root):
        self.tilt = 0

        def dfs(root):
            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            self.tilt += abs(left-right)
            return left + right + root.val

        dfs(root)
        return self.tilt


A = [1,2,3]
# A = [1,2,3,4,None,5] # expect 11
# A = [1,2,None,3,4] # expect 10
root = TreeNode().BuildTree(A)
root.printLevelorder()
print(Solution().findTilt2(root))
