"""
Given an array where elements are sorted in ascending order, convert it to a height balanced BST.

For this problem, a height-balanced binary tree is defined as a binary tree in which
the depth of the two subtrees of every node never differ by more than 1.
"""
from TreeNode import *
class Solution(object):
    def sortedArrayToBST(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        i, j = mid - 1, mid + 1

        if len(nums) == 1:
            return root
        elif len(nums) == 2:
            root.left = TreeNode(nums[i])
            return root

        while i >= 0:
            self.Insert(root, nums[i])
            i -= 1
        while j < len(nums):
            self.Insert(root, nums[j])
            j += 1

        return root

    def Insert(self, root, z):
        tail = None
        node = TreeNode(z)
        x = root
        while x != None:  # x travel to leaf
            tail = x
            if z < x.val:
                x = x.left
            else:
                x = x.right

        if node.val < tail.val:  # insert node
            tail.left = node
        else:
            tail.right = node

Not working
nums = [0,1,2,3,4,5]
print(Solution().sortedArrayToBST(nums))
