"""
Given a binary tree, return all root-to-leaf paths.
Note: A leaf is a node with no children.

Input:

   1
 /   \
2     3
 \
  5

Output: ["1->2->5", "1->3"]
Explanation: All root-to-leaf paths are: 1->2->5, 1->3
"""
from BST import *
class Solution(object):
    def binaryTreePaths(self, root):
        if not root:
            return []
        ret = []
        self.dfs(root, "", ret)
        return ret

    def dfs(self, root, path, ret):
        if not root.left and not root.right:
            path += str(root.val)
            ret.append(path)
        if root.left:
            self.dfs(root.left, path+str(root.val)+"->", ret)
        if root.right:
            self.dfs(root.right, path+str(root.val)+"->", ret)

root = TreeNode(1)
root.left = TreeNode(2)
root.left.right = TreeNode(5)
root.right = TreeNode(3)
print(Solution().binaryTreePaths(root))