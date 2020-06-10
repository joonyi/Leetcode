"""
Given a binary tree, determine if it is a valid binary search tree (BST).

Assume a BST is defined as follows:

The left subtree of a node contains only nodes with keys less than the node's key.
The right subtree of a node contains only nodes with keys greater than the node's key.
Both the left and right subtrees must also be binary search trees.
"""
from TreeNode import TreeNode
class Solution(object):
    def isValidBST(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """
        def dfs(node, lower=float('-inf'), upper=float('inf')):
            if not node:
                return True
            if node.val <= lower or node.val >= upper:
                return False
            return dfs(node.left, lower, node.val) and dfs(node.right, node.val, upper)

        return dfs(root)

    def isValidBST2(self, root):
        stack, inorder = [], float('-inf')
        while stack or root: # inorder traversal iterative
            while root:
                stack.append(root)
                root = root.left
            root = stack.pop()
            # If next element in inorder traversal
            # is smaller than the previous one
            # that's not BST.
            if root.val <= inorder:
                return False
            inorder = root.val
            root = root.right

        return True

# A = [2,1,3]
# A = [5,1,4,None,None,3,6]
# A = [0, -1]
# A = [1,1]
A = [10,5,15,None,None,6,20]
root = TreeNode(None).BuildTree(A)
print(Solution().isValidBST2(root))