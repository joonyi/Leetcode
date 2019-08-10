"""
Given a binary tree, check whether it is a mirror of itself
(ie, symmetric around its center).

For example, this binary tree [1,2,2,3,4,4,3] is symmetric:
    1
   / \
  2   2
 / \ / \
3  4 4  3
But the following [1,2,2,null,3,null,3] is not:
    1
   / \
  2   2
   \   \
   3    3
"""

class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        def isSym(left, right):
            if not left and not right: return True
            if left and right and left.val == right.val:
                return isSym(left.left, right.right) and isSym(left.right, right.left)
            return False

        return isSym(root, root)

    def isSymmetric2(self, root):
        if not root:
            return True
        queue = []
        queue.append((root.left, root.right))
        while queue:
            l, r = queue.pop(0)
            if not l and not r:
                continue
            if not l or not r:
                return False
            if l.val != r.val:
                return False
            # node1.left and node2.right are symmetric nodes in structure
            # node1.right and node2.left are symmetric nodes in structure
            queue.append((l.left, r.right))
            queue.append((l.right, r.left))
        return True

    def isSymmetric3(self, root):
        if root is None:
            return True
        else:
            return self.isMirror(root.left, root.right)

    def isMirror(self, left, right):
        if left is None and right is None:
            return True
        if left is None or right is None:
            return False

        if left.val == right.val:
            outPair = self.isMirror(left.left, right.right)
            inPair = self.isMirror(left.right, right.left)
            return outPair and inPair
        else:
            return False

root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(2)
root.left.left = TreeNode(3)
root.left.right = TreeNode(4)
root.right.left = TreeNode(4)
root.right.right = TreeNode(3)

print(Solution().isSymmetric3(root))
