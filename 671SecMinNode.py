"""
Given a non-empty special binary tree consisting of nodes with the non-negative value,
where each node in this tree has exactly two or zero sub-node. If the node has two sub-nodes,
then this node's value is the smaller value among its two sub-nodes. More formally,
the property root.val = min(root.left.val, root.right.val) always holds.

Given such a binary tree, you need to output the second minimum value in the set made of
all the nodes' value in the whole tree.

If no such second minimum value exists, output -1 instead.
"""

from TreeNode import TreeNode
class Solution:
    def findSecondMinimumValue(self, root: TreeNode) -> int:
        # O(n)
        def traverse(root):
            if root:
                res.add(root.val)
                traverse(root.left)
                traverse(root.right)

        res = set()
        traverse(root)
        return sorted(res)[1] if len(res) > 1 else -1

    def findSecondMinimumValue2(self, root: TreeNode) -> int:
        # Fastest
        def traverse(node):
            if node:
                if self.minV < node.val < self.secMin:
                    self.secMin = node.val
                elif node.val == self.minV:
                    traverse(node.left)
                    traverse(node.right)

        self.minV = root.val
        self.secMin = float('inf')
        traverse(root)
        return self.secMin if self.secMin < float('inf') else -1

    def findSecondMinimumValue3(self, root: TreeNode) -> int:
        def traverse(root):
            if not root:
                return -1
            if root.val > self.minV:
                return root.val
            leftMin = traverse(root.left)
            rightMin = traverse(root.right)
            if leftMin == -1 or rightMin == -1:  #  at leaf or no lesser number
                return max(leftMin, rightMin)
            else:
                return min(leftMin, rightMin)

        self.minV = root.val
        return traverse(root)



A = [2,2,5,None,None,5,7]  # 5
# A = [2,2,2]  # -1
A = [1,1,3,1,1,3,4,3,1,1,1,3,8,4,8,3,3,1,6,2,1]  # 2
root = TreeNode(None).BuildTree(A)
print(Solution().findSecondMinimumValue2(root))

