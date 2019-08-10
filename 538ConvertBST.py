"""
Given a Binary Search Tree (BST), convert it to a Greater Tree such that every key
of the original BST is changed to the original key plus sum of all keys greater than
the original key in BST.

Input: The root of a Binary Search Tree like this:
              5
            /   \
           2     13
Output: The root of a Greater Tree like this:
             18
            /   \
          20     13
"""
from BST import *
class Solution(object):
    # Idea: Travel to the max node
    # When recurse back, add max val to all nodes
    def convertBST(self, root):
        self.cur_sum = 0
        self.travel(root)
        return root

    def travel(self, root):
        if not root:
            return
        if root.right:
            self.travel(root.right)

        root.val += self.cur_sum
        self.cur_sum = root.val

        if root.left:
            self.travel(root.left)


root = TreeNode(5)
root.left = TreeNode(2)
root.right = TreeNode(13)
ret = Solution().convertBST(root)
printPreorder(ret)