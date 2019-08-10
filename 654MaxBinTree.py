"""
Given an integer array with no duplicates. A maximum tree building on this array is defined as follow:

The root is the maximum number in the array.
The left subtree is the maximum tree constructed from left part subarray divided by the maximum number.
The right subtree is the maximum tree constructed from right part subarray divided by the maximum number.
Construct the maximum tree by the given array and output the root node of this tree.
"""
from TreeNode import *
class Solution(object):
    def constructMaximumBinaryTree(self, nums):
        """
        :type nums: List[int]
        :rtype: TreeNode
        """
        if not nums:
            return None
        elif len(nums) == 1:
            return TreeNode(nums[0])

        max_idx = 0
        max_num = nums[0]
        for i in range(1, len(nums)):
            if nums[i] > max_num:
                max_num = nums[i]
                max_idx = i

        root = TreeNode(max_num)
        i, j = 0, len(nums) - 1
        if i < max_idx:
            root.left = TreeNode(nums[i])
            i += 1
            while i < max_idx:
                self.Insert(root.left, nums[i], "right")
                i += 1

        if j > max_idx:
            root.right = TreeNode(nums[j])
            j -= 1
            while j > max_idx:
                self.Insert(root.right, nums[j], "left")
                j -= 1

        return root

    def Insert(self, root, z, side):
        tail = None
        node = TreeNode(z)
        x = root
        while x != None:  # x travel to leaf
            tail = x
            if x.left:
                x = x.left
            else:
                x = x.right

        if side == "left":
            tail.left = node # insert node
        else:
            tail.right = node




# nums = [3,2,1,6,0,5]
nums = [3,2,1]
root = Solution().constructMaximumBinaryTree(nums)
root.printLevelorder()