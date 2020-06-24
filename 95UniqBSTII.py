"""
Given an integer n, generate all structurally unique BST's (binary search trees)
that store values 1 ... n.
"""
from typing import List
from TreeNode import TreeNode
class Solution:
    def generateTrees(self, n: int) -> List[TreeNode]:
        def generate(first, last):
            trees = []
            for root in range(first, last + 1):
                lefts = generate(first, root - 1)
                rights = generate(root + 1, last)
                for left in lefts:
                    for right in rights:
                        node = TreeNode(root)
                        node.left = left
                        node.right = right
                        trees += node,
                        # trees.append(node)
            return trees or [None]

        return generate(1, n)

n = 3
root = Solution().generateTrees(n)
print(root)