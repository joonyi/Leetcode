"""
Given the root node of a binary search tree (BST) and a value. You need to find the node
in the BST that the node's value equals the given value. Return the subtree rooted with that node.
If such node doesn't exist, you should return NULL.
"""
from TreeNode import TreeNode
class Solution(object):
    def searchBST(self, root, val):
        """
        :type root: TreeNode
        :type val: int
        :rtype: TreeNode
        """
        if not root:
            return root # faster than return None, why?

        if val == root.val:
            return root
        elif val < root.val:
            return self.searchBST(root.left, val)
        else:
            return self.searchBST(root.right, val)



A = [4,2,7,1,3]
tree = TreeNode(None).BuildTree(A)
tree.printLevelorder()
tree = Solution().searchBST(tree, 5)
tree.printLevelorder()