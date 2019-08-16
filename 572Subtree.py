"""
Given two non-empty binary trees s and t, check whether tree t has exactly the same structure
and node values with a subtree of s. A subtree of s is a tree consists of a node in s and all
of this node's descendants. The tree s could also be considered as a subtree of itself.
"""
from TreeNode import  TreeNode
class Solution(object):
    def isSubtree(self, s, t):
        """
        :type s: TreeNode
        :type t: TreeNode
        :rtype: bool
        """
        res = []
        self.InOderTraversal(s, res)
        tree1 = '.'.join(res)
        res = []
        self.InOderTraversal(t, res)
        tree2 = '.'.join(res)
        return tree2 in tree1

    def InOderTraversal(self, root, res):
        if root:
            res.append('#' + str(root.val))
            self.InOderTraversal(root.left, res)
            self.InOderTraversal(root.right, res)
        else:
            res.append("None")

    def isSubtree2(self, s, t):
        if not s: return False
        return self.isSameTree(s, t) or self.isSubtree2(s.left, t) or self.isSubtree2(s.right, t)

    def isSameTree(self, s, t):
        if not s and not t:
            return True
        if not s or not t:
            return False

        if s.val == t.val:
            return self.isSameTree(s.left, t.left) and self.isSameTree(s.right, t.right)
        else:
            return False

    def isSubtree3(self, s, t): # Merkel Tree
        from hashlib import sha256
        def hash_(x):
            S = sha256()
            S.update(x.encode('utf-8'))
            return S.hexdigest()

        def merkle(node):
            if not node:
                return '#'
            m_left = merkle(node.left)
            m_right = merkle(node.right)
            node.merkle = hash_(m_left + str(node.val) + m_right)
            return node.merkle

        merkle(s)
        merkle(t)

        def dfs(node):
            if not node:
                return False
            return (node.merkle == t.merkle or dfs(node.left) or dfs(node.right))

        return dfs(s)


A = [3,4,5,1,2] #T
B = [4,1,2]
# A = [3,4,5,1,2,None,None,0] #F
# B = [4,1,2]
# A = [1,2,3]
# B = [2,3]
# A = [12]
# B = [2]
s = TreeNode(None).BuildTree(A)
t = TreeNode(None).BuildTree(B)
print(Solution().isSubtree3(s, t))