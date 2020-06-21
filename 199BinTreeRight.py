"""
Given a binary tree, imagine yourself standing on the right side of it,
return the values of the nodes you can see ordered from top to bottom.

"""

from TreeNode import TreeNode
class Solution(object):

    def rightSideView(self, root):
        """
        :type root: TreeNode
        :rtype: List[int]
        """
        if not root:
            return []

        res = []
        level = [root]
        while level:
            currentNode = []
            nextLevel = []
            for node in level:
                currentNode.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            res.append(currentNode[-1])
            level = nextLevel

        return res

    def rightSideView2(self, root):
        # Compute the right view of both right and left left subtree, then combine them with trick
        if not root:
            return []
        right = self.rightSideView2(root.right)
        left = self.rightSideView2(root.left)
        return [root.val] + right + left[len(right):]  # deeper left subtree will get viewed

    def rightSideView3(self, root):
        # Collect view from right first, then go left, this time only add when left tree deeper
        # len(view) represents depth of tree
        def collect(node, depth):
            if node:
                if depth == len(view):
                    view.append(node.val)
                collect(node.right, depth + 1)
                collect(node.left, depth + 1)

        view = []
        collect(root, 0)
        return view

    def rightSideView4(self, root):
        def recurse(root, level, res):
            if not root:
                return []
            if len(res) < level:  # len(res) represents depth, only add when new level depth
                res.append(root.val)
            recurse(root.right, level + 1, res)
            recurse(root.left, level + 1, res)

        res = []
        recurse(root, 1, res)
        return res


nums = [1,2,3,None,5,None,4]  # [1,3,4]
# nums = [1,2]  # [1,2]
root = TreeNode(None).BuildTree(nums)
TreeNode.printLevelorder(root)
print(Solution().rightSideView4(root))