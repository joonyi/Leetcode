"""
Given a binary tree, determine if it is height-balanced.

For this problem, a height-balanced binary tree is defined as:
a binary tree in which the depth of the two subtrees of every node never differ by more than 1.

Example 1:
Given the following tree [3,9,20,null,null,15,7]:

    3
   / \
  9  20
    /  \
   15   7
Return true.

Example 2:
Given the following tree [1,2,2,3,3,null,null,4,4]:

       1
      / \
     2   2
    / \
   3   3
  / \
 4   4
Return false.
"""
from TreeNode import *
class Solution(object):
    def isBalanced(self, root):
        res = []
        self.depth(root, res)
        return all(res)

    def depth(self, root, res):
        if root is None:
            return 0

        left = self.depth(root.left, res)
        right = self.depth(root.right, res)
        if abs(left - right) <= 1:
            res.append(True)
        else:
            res.append(False)
        return max(left, right) + 1

    # Top down, check balance for each node O(n^2)
    def isBalanced2(self, root):
        if root == None:
            return True

        left = self.height(root.left)
        right = self.height(root.right)
        return abs(left - right) <= 1 and self.isBalanced2(root.left) and self.isBalanced2(root.right)

    def height(self, root):
        if root == None: return 0
        return max(self.height(root.left), self.height(root.right)) + 1

    def isBalanced3(self, root):
        if not root: return True
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        if abs(left - right) > 1:
            return False
        return self.isBalanced3(root.left) and self.isBalanced3(root.right)

    def get_height(self, root):
        if not root: return 0
        left = self.get_height(root.left)
        right = self.get_height(root.right)
        return max(left, right) + 1

    def isBalanced4(self, root):
        def check(root):
            if root is None:
                return 0
            left = check(root.left)
            right = check(root.right)
            if left == -1 or right == -1 or abs(left - right) > 1:
                return -1
            return 1 + max(left, right)

        return check(root) != -1

# A = [3,9,20,None,None,15,7] # True
A = [1,2,2,3,3,None,None,4,4] # False
# A = [1,2,2,3,None,None,3,4,None,None,4] # False
# A = [1,2,2,3,3,None,None,4,4] # False
root = TreeNode().BuildTree(A)
print(Solution().isBalanced3(root))



