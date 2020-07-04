"""
The thief has found himself a new place for his thievery again. There is only one entrance
to this area, called the "root." Besides the root, each house has one and only one parent house.
After a tour, the smart thief realized that "all houses in this place forms a binary tree".
It will automatically contact the police if two directly-linked houses were broken into on
the same night.

Determine the maximum amount of money the thief can rob tonight without alerting the police.
"""

from TreeNode import TreeNode
class Solution:
    def rob(self, root: TreeNode) -> int:
        # TLE
        if not root:
            return 0

        level = [root]
        odd = even = toggle = 0
        while level:
            nextLevel = []
            for node in level:
                if toggle:
                    odd += node.val
                else:
                    even += node.val

                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)

            toggle ^= 1
            level = nextLevel

        return max(odd, even)

    def rob2(self, root: TreeNode) -> int:
        def robSub(root):
            if not root:
                return [0,0]
            left = robSub(root.left)
            right = robSub(root.right)

            now = max(left) + max(right)
            later = root.val + left[0] + right[0]
            return [now, later]
        res = robSub(root)
        return max(res)

"""
Input: [3,4,5,1,3,null,1]
 input tree            dp tree:
     3                  [3+3+1,4+5]
    / \                /        \
   4   5            [4,3]      [5,1]
  / \   \          /     \          \
 1   2   1      [1,0]    [2,0]     [1,0]
                / \       /  \        /  \
           [0,0] [0,0] [0,0] [0,0]  [0,0] [0,0]

"""
A = [3,2,3,None,3,None,1]  # 7
A = [3,4,5,1,3,None,1]  # 9
root = TreeNode(None).BuildTree(A)
print(Solution().rob2(root))



