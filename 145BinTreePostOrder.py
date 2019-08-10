"""
Given a binary tree, return the postorder traversal of its nodes' values.

Follow up: Recursive solution is trivial, could you do it iteratively?
"""
from TreeNode import *
class Solution(object):
    def postorderTraversal(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        def Travel(root, res):
            if root:
                Travel(root.left, res)
                Travel(root.right, res)
                res.append(root.val)

        res = []
        Travel(root, res)
        return res

    def postorderTraversal2(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        traversal, stack = [], [root]
        while stack:
            node = stack.pop()
            if node:
                # pre-order, right first
                traversal.append(node.val)
                stack.append(node.left)
                stack.append(node.right)

        # reverse result
        return traversal[::-1]


A = [1,None,2,3] # 321
root = TreeNode().BuildTree(A)
print(Solution().postorderTraversal2(root))
