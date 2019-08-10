# Given a tree, rearrange the tree in in-order so that the leftmost node
# in the tree is now the root of the tree, and every node has no left child
# and only 1 right child
from BST import TreeNode
class Solution(object):
    def increasingBST(self, root, tail=None):
        if root is None:
            return tail
        res = self.increasingBST(root.left, root)
        root.left = None
        root.right = self.increasingBST(root.right, tail)
        return res

    def increasingBST2(self, root):
        """
        :type root: TreeNode
        :rtype: TreeNode
        """
        tree = TreeNode()
        self.InOrder(root, tree)
        return tree

    def InOrder(self, root, tree):
        if root:
            self.InOrder(root.left, tree)
            tree.append(root.val)
            self.InOrder(root.right, tree)



tree = TreeNode()
a = [5,3,6,2,4,None,8,1,None,None,None,7,9]
# b = [i for i in range(2,10)]
for i in a:
    tree.append(i)

tree.printLevelorder(tree)
flatten = Solution().increasingBST(tree)
tree.printLevelorder(flatten)