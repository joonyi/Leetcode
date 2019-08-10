from TreeNode import *
class Solution(object):
    def isSymmetric(self, root):
        """
        :type root: TreeNode
        :rtype: bool
        """

        level = [root]
        while level:
            currentNode = []
            nextLevel = []
            for node in level:
                if node:
                    currentNode.append(node.val)
                else:
                    currentNode.append(None)
                    continue
                if node.left:
                    nextLevel.append(node.left)
                else:
                    nextLevel.append(None)
                if node.right:
                    nextLevel.append(node.right)
                else:
                    nextLevel.append(None)

            i, j = 0, len(currentNode) - 1
            while i < j:
                if currentNode[i] != currentNode[j]:
                    return False
                i += 1
                j -= 1

            level = nextLevel

        return True


# A = [1,2,2,3,4,4,3]
A = [1,2,2,None,3,None,3]
root = TreeNode().BuildTree(A)
print(Solution().isSymmetric2(root))