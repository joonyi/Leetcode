"""
Given two binary trees, write a function to check if they are the same or not.

Two binary trees are considered the same if they are structurally identical and
the nodes have the same value.
"""
from TreeNode import TreeNode
class Solution(object):
    def isSameTree(self, p, q):
        """
        :type p: TreeNode
        :type q: TreeNode
        :rtype: bool
        """
        if p and q:
            return p.val == q.val and self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        return p is q

    def isSameTree2(self, p, q):
        if not p and not q:
            return True
        if not p or not q:
            return False

        if p.val == q.val:
            return self.isSameTree(p.left, q.left) and self.isSameTree(p.right, q.right)
        else:
            return False

A = [1,2,3]
B = [1,2,3]
tree1 = TreeNode(None).BuildTree(A)
tree2 = TreeNode(None).BuildTree(B)
print(Solution().isSameTree(tree1, tree2))