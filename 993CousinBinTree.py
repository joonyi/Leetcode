"""
In a binary tree, the root node is at depth 0, and children of each depth k node are at depth k+1.
Two nodes of a binary tree are cousins if they have the same depth, but have different parents.

We are given the root of a binary tree with unique values, and the values x and y of two
different nodes in the tree.

Return true if and only if the nodes corresponding to the values x and y are cousins.
"""
from TreeNode import *
class Solution(object):
    def isCousins(self, root, x, y):
        """
        :type root: TreeNode
        :type x: int
        :type y: int
        :rtype: bool
        """
        def dfs(root, parent, x, y, cnt):
            if not root:
                return

            if root.val == x:
                self.parent[0] = parent
                self.h[0] = cnt
            elif root.val == y:
                self.parent[1] = parent
                self.h[1] = cnt
            dfs(root.left, root, x, y, cnt+1)
            dfs(root.right, root, x, y, cnt+1)


        self.h = [0,0]
        self.parent = [0,0]
        cnt = 0
        dfs(root, None, x, y, cnt)
        return (self.parent[0] != self.parent[1]) and (self.h[0] == self.h[1])


# A = [1,2,3,4] # False
# x = 4
# y = 3
# A, x, y = [1,2,3,None,4,None,5], 5, 4 # True
A, x, y = [1,2,3,None,4], 2, 3 # False
root = TreeNode().BuildTree(A)
root.printLevelorder()
print(Solution().isCousins(root, x, y))