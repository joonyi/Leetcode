"""
Given a binary search tree and the lowest and highest boundaries as L and R,
trim the tree so that all its elements lies in [L, R] (R >= L).
You might need to change the root of the tree, so the result should return
the new root of the trimmed binary search tree.

Example 1:
Input:
    1
   / \
  0   2
  L = 1
  R = 2
Output:
    1
      \
       2

Example 2:
Input:
    3
   / \
  0   4
   \
    2
   /
  1
  L = 1
  R = 3
Output:
      3
     /
   2
  /
 1
"""
from BST import *
class Solution(object):
    def trimBST(self, root, L, R):
        if not root: return root
        if root.val < L: return self.trimBST(root.right, L, R)
        if root.val > R: return self.trimBST(root.left, L, R)

        root.left = self.trimBST(root.left, L, R)
        root.right = self.trimBST(root.right, L, R)

        return root

    # When node.val > R, we know the trimmed binary tree must occur to the left of the node.
    # Similarly, when node.val < L, the trimmed binary tree occurs to the right of the node.
    # Otherwise, we will trim both sides of the tree.
    def trimBST2(self, root, L, R):
        def trim(node):
            if node:
                if node.val > R:
                    return trim(node.left)
                elif node.val < L:
                    return trim(node.right)
                else:
                    node.left = trim(node.left)
                    node.right = trim(node.right)
                    return node

        return trim(root)

root = TreeNode(3)
root.left = TreeNode(0)
root.right = TreeNode(4)
root.left.right = TreeNode(2)
root.left.right.left = TreeNode(1)
L, R = 1, 3
printPreorder(Solution().trimBST2(root, L, R))