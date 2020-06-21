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
        left = mid - 1
        right = mid + 1
        root = node = TreeNode(nums[mid])
        while left > -1:
            node.left = TreeNode(nums[left])
            node = node.left
            left -= 1
        node = root
        while right < len(nums):
            node.right = TreeNode(nums[right])
            node = node.right
            right += 1
        return root

    def sortedArrayToBST2(self, nums):
        if not nums:
            return None

        mid = len(nums) // 2
        root = TreeNode(nums[mid])
        root.left = self.sortedArrayToBST2(nums[:mid])
        root.right = self.sortedArrayToBST2(nums[mid + 1:])

        return root

nums = [0,1,2,3,4,5]
# nums = [-10,-3,0,5,9]

root = Solution().sortedArrayToBST2(nums)
root.printLevelorder()
