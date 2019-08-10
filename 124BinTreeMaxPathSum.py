from TreeNode import TreeNode
import sys
class Solution(object):
    def maxPathSum(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        left = -sys.maxsize
        right = -sys.maxsize
        if root.left:
            left = self.PathSum(root.left, left, right)
        if root.right:
            right = self.PathSum(root.right, left, right)
        max_val = max(root.val, left, right)
        if root.val + left + right > max_val:
            max_val = root.val + left + right
        if root.val + left > max_val:
            max_val = root.val + left
        if root.val + right > max_val:
            max_val = root.val + right

        return max_val

    # this recurse is bad bcs put left, right in the if condition
    # better to recurse one more layer and return 0
    def PathSum(self, root, left, right):
        if root.left == None and root.right == None:
            return root.val
        if root.left:
            left = self.PathSum(root.left, left, right)
        if root.right:
            right = self.PathSum(root.right, left, right)
        max_val = self.FindMax(root.val, left, right)
        return max_val

    def FindMax(self, a, b, c):
        max_val = a
        if a + b + c > max_val:
            max_val = a + b + c
        if a + b > max_val:
            max_val = a + b
        if a + c > max_val:
            max_val = a + c

        return max_val

    # better recurse technique
    # use global max
    # max(x, 0) to cut off any negative route
    def maxPathSum2(self, root):
        def maxend(node):
            if not node:
                return 0
            left = maxend(node.left)
            right = maxend(node.right)
            self.max = max(self.max, left + node.val + right)
            return max(node.val + max(left, right), 0) # zero to cut off negative
            # return node.val + max(left, right)

        self.max = -sys.maxsize
        maxend(root)
        return self.max


tree = TreeNode()
A = [2,-1]
tree = tree.BuildTree(A)
tree.printLevelorder(tree)
print(Solution().maxPathSum2(tree))