"""
You need to find the largest value in each row of a binary tree.
"""
from TreeNode import TreeNode
class Solution(object):
    def largestValues(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return root

        queue = [root]
        res = [root.val]
        while queue:
            levelVal = []
            nextLevel = []
            for node in queue:
                if node.left:
                    levelVal.append(node.left.val)
                    nextLevel.append(node.left)
                if node.right:
                    levelVal.append(node.right.val)
                    nextLevel.append(node.right)
            queue = nextLevel
            if levelVal:
                res.append(max(levelVal))

        return res

    def largestValues2(self, root):
        maxes = []
        row = [root]

        while any(row):
            maxes.append(max(node.val for node in row))
            # row = [kid for node in row for kid in (node.left, node.right) if kid] equivalent tp next 5 line
            kids = []
            for node in row:
                for kid in (node.left, node.right):
                    if kid:
                        kids += kid,
            row = kids
        return maxes


A = [1,3,2,5,3,None,9]

root = TreeNode(None).BuildTree(A)
print(Solution().largestValues2([]))

