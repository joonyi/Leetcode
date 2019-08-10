"""
Given a binary tree and a sum, determine if the tree has a root-to-leaf path
such that adding up all the values along the path equals the given sum.

Note: A leaf is a node with no children.

Example:
Given the below binary tree and sum = 22,
      5
     / \
    4   8
   /   / \
  11  13  4
 /  \      \
7    2      1
return true, as there exist a root-to-leaf path 5->4->11->2 which sum is 22.
"""
from BST import *
class Solution(object):
    def hasPathSum(self, root, sum):
        if not root:
            return False
        if not root.left and not root.right and root.val == sum:
            return True
        sum -= root.val
        return self.hasPathSum(root.left, sum) or self.hasPathSum(root.right, sum)

    # BFS with queue
    def hasPathSum2(self, root, sum):
        if not root:
            return False
        queue = [(root, sum - root.val)]
        while queue:
            curr, val = queue.pop(0)
            if not curr.left and not curr.right:
                if val == 0:
                    return True
            if curr.left:
                queue.append((curr.left, val - curr.left.val))
            if curr.right:
                queue.append((curr.right, val - curr.right.val))
        return False

    def hasPathSum3(self, root, sum):
        ret = []
        self.dfs(root, sum, ret)
        return any(ret)

    def dfs(self, root, target, ret):
        if root:
            if not root.left and not root.right:
                if root.val == target:
                    ret.append(True)
            if root.left:
                self.dfs(root.left, target-root.val, ret)
            if root.right:
                self.dfs(root.right, target-root.val, ret)

root = TreeNode(5)
root.left = TreeNode(4)
root.right = TreeNode(8)
root.left.left = TreeNode(11)
root.right.left = TreeNode(13)
root.right.right = TreeNode(4)
root.left.left.left = TreeNode(7)
root.left.left.right = TreeNode(2)
root.right.right.right = TreeNode(1)
sum = 22
print(Solution().hasPathSum3(root,sum))