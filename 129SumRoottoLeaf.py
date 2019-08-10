from TreeNode import TreeNode
class Solution(object):
    def sumNumbers(self, root):
        """
        :type root: TreeNode
        :rtype: int
        """
        if not root:
            return root

        res = []
        path = 0
        self.sum_to_leaf(root, res, path)
        return sum(res)

    def sum_to_leaf(self, root, res, path):
        path = path * 10 + root.val
        if root.left == None and root.right == None:
            res.append(path)
        if root.left:
            self.sum_to_leaf(root.left, res, path)
        if root.right:
            self.sum_to_leaf(root.right, res, path)



A = []
root = TreeNode().BuildTree(A)
print(Solution().sumNumbers([]))