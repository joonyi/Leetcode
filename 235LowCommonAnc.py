"""
Given a binary search tree (BST), find the lowest common ancestor (LCA) of two given nodes in the BST.

According to the definition of LCA on Wikipedia: “The lowest common ancestor is defined
between two nodes p and q as the lowest node in T that has both p and q as descendants
(where we allow a node to be a descendant of itself).”
"""
from TreeNode import *
class Solution(object):
    def lowestCommonAncestor(self, root, p, q):
        """
        :type root: TreeNode
        :type p: TreeNode
        :type q: TreeNode
        :rtype: TreeNode
        """
        """
        Start traversing the tree from the root node.
        If both the nodes p and q are in the right subtree, then continue the 
            search with right subtree starting step 1.
        If both the nodes p and q are in the left subtree, then continue the 
            search with left subtree starting step 1.
        If both step 2 and step 3 are not true, this means we have found the 
            node which is common to node p's and q's subtrees. and hence we 
            return this common node as the LCA.
        """
        # If both p and q are greater than parent
        if p.val > root.val and q.val > root.val:
            return self.lowestCommonAncestor(root.right, p, q)
        # If both p and q are lesser than parent
        elif p.val < root.val and q.val < root.val:
            return self.lowestCommonAncestor(root.left, p, q)
        # We have found the split point, i.e. the LCA node.
        else:
            return root

    def lowestCommonAncestor2(self, root, p, q):
        # Traverse the tree
        while root:
            if p.val > root.val and q.val > root.val:
                # If both p and q are greater than parent
                root = root.right
            elif p.val < root.val and q.val < root.val:
                # If both p and q are lesser than parent
                root = root.left
            else:
                # We have found the split point, i.e. the LCA node.
                return root

p, q = TreeNode(2), TreeNode(8)
A = [6,p,q,0,4,7,9,None,None,3,5]
root = TreeNode().BuildTree(A)
print(Solution().lowestCommonAncestor2(root, p, q))