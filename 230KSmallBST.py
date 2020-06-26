"""
Given a binary search tree, write a function kthSmallest to find the kth smallest element in it.
"""
from TreeNode import TreeNode
class Solution:
    def kthSmallest(self, root: TreeNode, k: int) -> int:
        def inorder(root):
            return inorder(root.left) + [root.val] + inorder(root.right) if root else []


        res = inorder(root)
        return res[k - 1]

    def kthSmallest2(self, root: TreeNode, k: int) -> int:
        # Iteration solution. Could stop after kth element
        # O(h + k), h is height. For balanced tree h = logN, completely unbalanced h = N
        stack = []
        while True:
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            k -= 1
            if k == 0:
                return root.val
            root = root.right


A, k = [3,1,4,None,2], 1
A, k = [5,3,6,2,4,None,None,1], 3
root = TreeNode(None).BuildTree(A)
print(Solution().kthSmallest(root, k))
