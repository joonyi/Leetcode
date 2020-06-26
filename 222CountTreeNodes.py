"""
Given a complete binary tree, count the number of nodes.

Note:
Definition of a complete binary tree from Wikipedia:
In a complete binary tree every level, except possibly the last, is completely filled,
and all nodes in the last level are as far left as possible. It can have between 1 and 2h nodes
inclusive at the last level h.
"""

from TreeNode import TreeNode
class Solution:
    def countNodes(self, root: TreeNode) -> int:
        if not root:
            return 0
        cnt = 1 + self.countNodes(root.left) + self.countNodes(root.right)
        return cnt

    def countNodes2(self, root: TreeNode) -> int:
        def traverse(root):
            if root:
                self.cnt += 1
                traverse(root.left)
                traverse(root.right)

        self.cnt = 0
        traverse(root)
        return self.cnt

    def countNodes3(self, root: TreeNode) -> int:
        """
        Compare the depth between left sub tree and right sub tree.
        - If it is equal, it means the left sub tree is a full binary tree
        - It it is not, it means the right sub tree is a full binary tree
        """
        nodes = 0
        h = self.leftHeight(root)
        while root:
            if self.leftHeight(root.right) == h - 1:
                nodes += 1 << h  # 2**h
                root = root.right
            else:
                nodes += 1 << h - 1  # 2**(h-1)
                root = root.left
            h -= 1
        return nodes

    def leftHeight(self, root):
        if not root:
            return -1
        return 1 + self.leftHeight(root.left)


A = [1,2,3,4,5,6]
root = TreeNode(None).BuildTree(A)
print(Solution().countNodes3(root))
