"""
Given a binary tree, find the length of the longest path where each node in the path has
the same value. This path may or may not pass through the root.

The length of path between two nodes is represented by the number of edges between them.
"""
from TreeNode import TreeNode
class Solution(object):
    def longestUnivaluePath(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        # The longest path is equal  to the longest possible left extending arrow + right extending arrow
        def search(root):
            if root == None:
                return 0

            left_len = search(root.left)
            right_len = search(root.right)
            left_arrow = right_arrow = 0
            if root.left and root.left.val == root.val:
                left_arrow = left_len + 1
            if root.right and root.right.val == root.val:
                right_arrow = right_len + 1
            self.longest = max(self.longest, left_arrow + right_arrow)
            return max(left_arrow, right_arrow)

        self.longest = 0
        search(root)
        return self.longest

    def longestUnivaluePath2(self, root):
        # Idea is to traverse to the leaf first
        def search(root, val):
            if root == None: return 0
            left = search(root.left, root.val)
            right = search(root.right, root.val)
            self.longest = max(self.longest, left + right)
            if val == root.val:
                return max(left, right) + 1
            return 0

        self.longest = 0
        search(root, root.val)
        return self.longest


# A = [5,4,5,1,1,None,5]
A = [1,4,5,4,4,None,5]
tree = TreeNode().BuildTree(A)
print(Solution().longestUnivaluePath2(tree))