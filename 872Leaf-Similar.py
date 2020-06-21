"""
Consider all the leaves of a binary tree.  From left to right order, the values of those leaves
form a leaf value sequence.

For example, in the given tree above, the leaf value sequence is (6, 7, 4, 9, 8).
Two binary trees are considered leaf-similar if their leaf value sequence is the same.
Return true if and only if the two given trees with head nodes root1 and root2 are leaf-similar.
"""
from TreeNode import TreeNode

class Solution(object):
    def leafSimilar(self, root1, root2):
        """
        :type root1: TreeNode
        :type root2: TreeNode
        :rtype: bool
        """
        def recurse(root, res):
            if not root:
                return None
            left = recurse(root.left, res)
            right = recurse(root.right, res)
            if not left and not right:
                res.append(root.val)
            return root.val

        res1 = []
        res2 = []
        recurse(root1, res1)
        recurse(root2, res2)
        return res1 == res2

    def leafSimilar2(self, root1, root2):
        def recurse(root):
            if not root:
                return []
            elif not root.left and not root.right:
                return [root.val]
            else:
                return recurse(root.left) + recurse(root.right)

        return recurse(root1) == recurse(root2)



A = B = [3,5,1,6,2,9,8,None, None, 7,4]
# A, B = [1], [2]
root1 = TreeNode(None).BuildTree(A)
root2 = TreeNode(None).BuildTree(B)
print(root1.printLevelorder())
print(Solution().leafSimilar2(root1, root2))
