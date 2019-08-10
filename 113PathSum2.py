"""
Given a binary tree and a sum, find all root-to-leaf paths
where each path's sum equals the given sum.

Note: A leaf is a node with no children.
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \    / \
7    2  5   1
Return:
[
   [5,4,11,2],
   [5,8,4,5]
]
"""
from BST import *
class Solution(object):
    def pathSum(self, root, sum):
        if not root:
            return []
        ret = []
        self.dfs(root, sum, [], ret)
        return ret

    def dfs(self, root, sum, path, ret):
        if not root:
            return
        if not root.left and not root.right and sum == root.val:
            path.append(root.val)
            ret.append(path)
        self.dfs(root.left, sum-root.val, path+[root.val], ret)
        self.dfs(root.right, sum-root.val, path+[root.val], ret)

    def pathSum2(self, root, sum):
        if not root:
            return []
        if not root.left and not root.right and sum == root.val:
            return [[root.val]]
        tmp = self.pathSum2(root.left, sum - root.val) + self.pathSum2(root.right, sum - root.val)
        return [[root.val] + i for i in tmp]

    def pathSum3(self, root, sum):
        res, stack = [], [(root, sum, [])]
        while stack:
            node, sum, path = stack.pop()
            if node:
                if node.val == sum and not node.left and not node.right:
                    res.append(path + [node.val])
                stack.append((node.right, sum - node.val, path + [node.val]))
                stack.append((node.left, sum - node.val, path + [node.val]))
        return res

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.left = TreeNode(5)
root.right.right.right = TreeNode(1)
sum = 22
print(Solution().pathSum3(root, sum))