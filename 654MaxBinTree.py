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
        def BuildTree(nums, root):
            if len(nums) == 1:
                root.val = nums[0]
                return

            (m, i) = max((v, i) for i, v in enumerate(nums)) # max val and index
            root.val = m
            if nums[:i]:
                root.left = TreeNode(None)
                BuildTree(nums[:i], root.left)
            if nums[i + 1:]:
                root.right = TreeNode(None)
                BuildTree(nums[i + 1:], root.right)

        root = TreeNode(None)
        BuildTree(nums, root)
        return root

    def constructMaximumBinaryTree2(self, nums):
        i = nums.index(max(nums)) # max val and index, this one better
        root = TreeNode(nums[i])
        if nums[:i]:
            root.left = self.constructMaximumBinaryTree2(nums[:i])
        if nums[i + 1:]:
            root.right = self.constructMaximumBinaryTree2(nums[i + 1:])
        return root

    def constructMaximumBinaryTree3(self, nums):
        """
        Fastest, O(n)
        We keep track of a stack, and make sure the numbers in stack is in decreasing order.

        For each new num, we make it into a TreeNode first.
        Then:

        0. If stack is empty, we push the node into stack and continue
        1. If new value is smaller than the node value on top of the stack, we append TreeNode as the right node of top of stack.
        2. If new value is larger, we keep poping from the stack until the stack is empty OR top of stack node value is greater than the new value. During the pop, we keep track of the last node being poped.
        After step 2, we either in the situation of 0, or 1, either way, we append last node as left node of the new node.
        After traversing, the bottom of stack is the root node because the bottom is always the largest value we have seen so far (during the traversing of list).

        """
        if not nums:
            return None
        stack = []
        last = None
        for num in nums:
            while stack and stack[-1].val < num:
                last = stack.pop()
            node = TreeNode(num)
            if stack:
                stack[-1].right = node
            if last:
                node.left = last
            stack.append(node)
            last = None
        return stack[0]

nums = [3,2,1,6,0,5]
# nums = [3,2,1]
root = Solution().constructMaximumBinaryTree3(nums)
root.printLevelorder()