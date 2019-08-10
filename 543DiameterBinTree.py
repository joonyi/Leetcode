"""
Given a binary tree, you need to compute the length of the diameter of the tree.
The diameter of a binary tree is the length of the longest path between any two nodes
in a tree. This path may or may not pass through the root.

Example:
Given a binary tree
          1
         / \
        2   3
       / \
      4   5
Return 3, which is the length of the path [4,2,1,3] or [5,2,1,3].
Note: The length of path between two nodes is represented by the number of edges between them.
"""
from BST import *
class Solution(object):
    def diameterOfBinaryTree(self, root):
        if not root:
            return 0
        self.ans = 0
        self.depth(root, self.ans)
        return self.ans

    def depth(self, root, ans):
        if not root:
            return 0
        left = self.depth(root.left, ans)
        right = self.depth(root.right, ans)
        self.ans = max(self.ans, left+right)
        return 1 + max(left, right)

    # This solution is more clean
    # self.diameter is to remember the highest number of nodes used in some path
    def diameterOfBinaryTree2(self, root):

        self.diameter = 0

        def depth(root):
            if not root:
                return 0
            left, right = depth(root.left), depth(root.right)
            self.diameter = max(self.diameter, left + right)
            return 1 + max(left, right)

        depth(root)
        return self.diameter

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(2)
root.left.right = TreeNode(3)
print(Solution().diameterOfBinaryTree2(root))