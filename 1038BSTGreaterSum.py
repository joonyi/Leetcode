"""
Given the root of a binary search tree with distinct values, modify it so that every node
has a new value equal to the sum of the values of the original tree that are greater than or
equal to node.val.

As a reminder, a binary search tree is a tree that satisfies these constraints:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from TreeNode import TreeNode
class Solution(object):
    def bstToGst(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        def GreaterSum(root, accum):
            if root == None:
                return accum

            root.val += GreaterSum(root.right, accum)
            accum = root.val

            return GreaterSum(root.left, accum)


        GreaterSum(root, 0)

        return root

    val = 0
    def bstToGst2(self, root):
        if root.right:
            self.bstToGst2(root.right)
        root.val = self.val = self.val + root.val
        if root.left:
            self.bstToGst2(root.left)
        return root


A = [4,1,6,0,2,5,7,None,None,None,3,None,None,None,8]
tree = TreeNode().BuildTree(A)
tree = Solution().bstToGst2(tree)
tree.printLevelorder()