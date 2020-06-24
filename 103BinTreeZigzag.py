"""
Given a binary tree, return the zigzag level order traversal of its nodes' values.
(ie, from left to right, then right to left for the next level and alternate between).

For example:
Given binary tree [3,9,20,null,null,15,7],

"""
from typing import List
from TreeNode import TreeNode
class Solution:
    def zigzagLevelOrder(self, root: TreeNode) -> List[List[int]]:
        """"""
        if not root:
            return []

        res = []
        level = [root]
        n = 1
        while level:
            currentNode = []
            nextLevel = []
            for node in level:
                currentNode.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            if n % 2 == 1:
                res.append(currentNode)
            else:
                res.append(currentNode[::-1])
            level = nextLevel
            n += 1

        return res


A = [3,9,20,None,None,15,7]
root = TreeNode(None).BuildTree(A)
print(Solution().zigzagLevelOrder(root))
