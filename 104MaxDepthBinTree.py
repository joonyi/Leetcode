"""
Given a binary tree, find its maximum depth.

The maximum depth is the number of nodes along the longest path
from the root node down to the farthest leaf node.

Note: A leaf is a node with no children.

Example:
Given binary tree [3,9,20,null,null,15,7],

    3
   / \
  9  20
    /  \
   15   7
return its depth = 3.
"""
class TreeNode(object):
    def __init__(self, x):
        self.val = x
        self.left = None
        self.right = None

class Solution(object):
    def maxDepth(self, root):
        if not root:
            return 0

        return 1+max(self.maxDepth(root.left),self.maxDepth(root.right))

    def maxDepth2(self, root):
        if not root:
            return 0

        queue = [root]
        level = 0
        while queue:
            currentNode = []
            for node in queue:
                if node.left:
                    currentNode.append(node.left)
                if node.right:
                    currentNode.append(node.right)
            queue = currentNode
            level += 1
        return level


root = TreeNode(1)
root.left = TreeNode(2)
root.right = TreeNode(3)
root.left.left = TreeNode(4)
root.left.right = TreeNode(5)
print(Solution().maxDepth2(root))