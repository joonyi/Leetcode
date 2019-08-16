"""
Given the root node of a binary search tree (BST) and a value to be inserted into the tree,
insert the value into the BST. Return the root node of the BST after the insertion.
It is guaranteed that the new value does not exist in the original BST.

Note that there may exist multiple valid ways for the insertion, as long as the tree remains
a BST after insertion. You can return any of them.
"""
from TreeNode import TreeNode
class Solution(object):
    def insertIntoBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if root == None:
            return TreeNode(val)

        if val < root.val:
            root.left = self.insertIntoBST(root.left, val)
        else:
            root.right = self.insertIntoBST(root.right, val)

        return root

A = [4,2,7,1,3]
tree = TreeNode(None).BuildTree(A)
tree.printLevelorder()
tree = Solution().insertIntoBST(tree, 5)
tree.printLevelorder()