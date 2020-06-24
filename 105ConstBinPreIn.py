"""
Given preorder and inorder traversal of a tree, construct the binary tree.
"""

from typing import List
from TreeNode import TreeNode
class Solution:
    def buildTree(self, preorder: List[int], inorder: List[int]) -> TreeNode:
        """"""
        if inorder:
            ind = inorder.index(preorder.pop(0))
            root = TreeNode(inorder[ind])
            root.left = self.buildTree(preorder, inorder[:ind])
            root.right = self.buildTree(preorder, inorder[ind + 1:])
            return root

    def buildTree2(self, preorder, inorder):
        if not preorder:
            return None

        root = TreeNode(preorder[0])
        stack = []
        stack.append(root)

        pre = 1
        ino = 0
        while (pre < len(preorder)):
            curr = TreeNode(preorder[pre])
            pre += 1
            prev = None
            while stack and stack[-1].val == inorder[ino]:
                prev = stack.pop()
                ino += 1

            # Add to tree
            if prev:
                prev.right = curr
            else:
                stack[-1].left = curr

            stack.append(curr)
        return root

"""
Preorder traversing implies that PRE[0] is the root node.
Then we can find this PRE[0] in IN, say it's IN[5].
Now we know that IN[5] is root, so we know that IN[0] - IN[4] is on the left side, 
IN[6] to the end is on the right side.

Recursively doing this on subarrays, we can build a tree out of it :
"""

preorder = [3,9,20,15,7]
inorder = [9,3,15,20,7]
print(Solution().buildTree2(preorder, inorder))
