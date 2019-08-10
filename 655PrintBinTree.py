"""
Print a binary tree in an m*n 2D string array following these rules:

1. The row number m should be equal to the height of the given binary tree.
2. The column number n should always be an odd number.
3. The root node's value (in string format) should be put in the exactly middle of the
first row it can be put. The column and the row where the root node belongs will
separate the rest space into two parts (left-bottom part and right-bottom part).
You should print the left subtree in the left-bottom part and print the right subtree in the
right-bottom part. The left-bottom part and the right-bottom part should have the same size.
Even if one subtree is none while the other is not, you don't need to print anything for the
none subtree but still need to leave the space as large as that for the other subtree.
However, if two subtrees are none, then you don't need to leave space for both of them.
4. Each unused space should contain an empty string "".
5. Print the subtrees following the same rules.
"""

from TreeNode import *
class Solution(object):
    def printTree(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """
        if not root: return None
        queue = [root]
        level = []
        while queue:
            nxt_level = []
            tmp = []
            for node in queue:
                if node == None:
                    tmp.append(None)
                    continue
                else:
                    tmp.append(node.val)

                if node.left:
                    nxt_level.append(node.left)
                else:
                    nxt_level.append(None)

                if node.right:
                    nxt_level.append(node.right)
                else:
                    nxt_level.append(None)
            queue = nxt_level
            level.append(tmp)

        if any(level[-1]) == False:
            level.pop()

        res = [["" for _ in range(2**len(level) - 1)] for _ in range(len(level))]
        n = len(res)

        self.fill(root, res, 0, 0)
if
    def fill(self, node, res, level, pos):
        if not node:
            return
        left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
        index = left_padding + pos * (spacing + 1)
        print(level, index, node.val)
        res[level][index] = str(node.val)
        self.fill(node.left, level + 1, pos << 1)
        self.fill(node.right, level + 1, (pos << 1) + 1)

    def printTree2(self, root):
        """
        :type root: TreeNode
        :rtype: List[List[str]]
        """

        def get_height(node):
            if not node:
                return 0
            return 1 + max(get_height(node.left), get_height(node.right))

        def traverse(node, level, pos):
            if not node:
                return
            left_padding, spacing = 2 ** (rows - level - 1) - 1, 2 ** (rows - level) - 1
            index = left_padding + pos * (spacing + 1)
            print(level, index, node.val)
            res[level][index] = str(node.val)
            traverse(node.left, level + 1, pos << 1)
            traverse(node.right, level + 1, (pos << 1) + 1)

        rows = get_height(root)
        cols = 2 ** rows - 1
        res = [['' for _ in range(cols)] for _ in range(rows)]
        traverse(root, 0, 0)
        return res


# A = [1,2,3,None,4]
# A = [1,2,None]
A = [1,2,3,None,4]
root = TreeNode().BuildTree(A)
print(Solution().printTree2(root))


