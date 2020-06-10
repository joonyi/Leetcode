"""
Given a Binary Search Tree and a target number, return true if there exist two elements
in the BST such that their sum is equal to the given target.
"""
from TreeNode import TreeNode
class Solution(object):
    def findTarget(self, root, k):
        """
        :type root: TreeNode
        :type k: int
        :rtype: bool
        """
        def InOrderTraversal(root):
            if res:
                return
            if root:
                InOrderTraversal(root.left)
                x = k - root.val
                if x in target:
                    res.append(True)
                else:
                    target[root.val] = 1
                InOrderTraversal(root.right)

        target = {}
        res = []
        InOrderTraversal(root)
        return any(res)

    def findTarget2(self, root, k):
        def search(root, res, k):
            if not root:
                return False
            if (k - root.val) in res:
                return True
            res.add(root.val)
            return search(root.left, res, k) or search(root.right, res, k)

        res = set()
        return search(root, res, k)

    def findTarget3(self, root, k):
        if not root:
            return False
        bfs, s = [root], set()
        for node in bfs:
            if k - node.val in s:
                return True
            s.add(node.val)
            if node.left:
                bfs.append(node.left)
            if node.right:
                bfs.append(node.right)
        return False

A, k = [5,3,6,2,4,None,7], 9
root = TreeNode(None).BuildTree(A)
print(Solution().findTarget2(root, k))
root.printLevelorder()