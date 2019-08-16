"""
We are given the head node root of a binary tree, where additionally every node's value is
either a 0 or a 1.

Return the same tree where every subtree (of the given tree) not containing a 1 has been removed.

(Recall that the subtree of a node X is X, plus every node that is a descendant of X.)
"""
from TreeNode import TreeNode
class Solution(object):
    def pruneTree(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        if not root.left and not root.right and root.val == 0:
            return None

        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)

        if not root.left and not root.right and root.val == 0:
            return None

        return root

    def pruneTree2(self, root): # this one slower but less code
        if root.left:
            root.left = self.pruneTree(root.left)
        if root.right:
            root.right = self.pruneTree(root.right)

        if not root.left and not root.right and root.val == 0:
            return None

        return root

A = [1,None,0,0,1]
# A = [1,0,1,0,0,0,1]
# A = [1,1,0,1,1,0,1,0]
root = TreeNode(None).BuildTree(A)
print(Solution().pruneTree(root))
root.printLevelorder()