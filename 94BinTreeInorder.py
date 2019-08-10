"""
Given a binary tree, return the inorder traversal of its nodes' values.
"""
from TreeNode import *
class Solution(object):
    def inorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def Travel(root, res):
            if root:
                Travel(root.left, res)
                res.append(root.val)
                Travel(root.right, res)

        res = []
        Travel(root, res)
        return res

    def inorderTraversal2(self, root):
        res, stack = [], []
        while True:
            while root:
                stack.append(root)
                root = root.left
            if not stack:
                return res
            node = stack.pop()
            res.append(node.val)
            root = node.right

A = [1,None,2,3] # 132
root = TreeNode().BuildTree(A)
print(Solution().inorderTraversal2(root))