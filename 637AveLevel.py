"""
Given a non-empty binary tree, return the average value of the nodes on each level
in the form of an array.
"""

from TreeNode import *
class Solution(object):
    def averageOfLevels(self, root):
        """
        :type root: TreeNode
        :rtype: List[float]
        """
        ret = []
        level = [root]
        while level:
            currentLevel = []
            nextLevel = []
            for node in level:
                currentLevel.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(sum(currentLevel)/len(currentLevel))
            level = nextLevel
        return ret


A = [3, 9, 20, 15, 7]
root = TreeNode().BuildTree(A)
# root.printLevelorder()
print(Solution().averageOfLevels(root))