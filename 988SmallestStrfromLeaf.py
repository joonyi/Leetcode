from TreeNode import TreeNode
import sys
class Solution(object):
    def smallestFromLeaf(self, root):
        """
        :type root: TreeNode
        :rtype: str
        """
        if not root:
            return root

        def sum_to_leaf(root, res, path):
            path = str(root.val) + ',' + path
            if root.left == None and root.right == None:
                res.append(path)
            if root.left:
                sum_to_leaf(root.left, res, path)
            if root.right:
                sum_to_leaf(root.right, res, path)

        res = []
        path = ''
        sum_to_leaf(root, res, path)

        min_index = self.MinIndex(res)
        output = ''
        d = {}
        char = ['a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q','r',
                's','t','u','v','w','x','y','z']
        for i in range(26):
            d[str(i)] = char[i]
        word = res[min_index].rsplit(',')
        for char in word:
            if char:
                output = output + d[char]
        return output

    def MinIndex(self, A):
        val, min_i = 0, 0
        min_val = sys.maxsize
        for i, path in enumerate(A):
            for j in range(len(path)):
                if path[j] != ',':
                    val = val*10 + int(path[j])

            if val < min_val:
                min_val = val
                min_i = i
            val = 0

        return min_i

    # Dfs with stack
    def smallestFromLeaf2(self, root):
        if root == None:
            return ""
        res = 8500 * "z"
        chrs = "abcdefghijklmnopqrstuvwxyz"
        stack = [(root, "")]
        while len(stack) > 0:
            node, path = stack.pop()
            cur = chrs[node.val]
            if node.left == None and node.right == None:
                res = min(res, cur + path)
            if node.left != None:
                stack.append((node.left, cur + path))
            if node.right != None:
                stack.append((node.right, cur + path))
        return res

    # Dfs with recursion
    def smallestFromLeaf3(self, root):
        self.ans = "~"

        def dfs(node, A):
            if node:
                A.append(chr(node.val + ord('a')))
                if not node.left and not node.right:
                    self.ans = min(self.ans, "".join(reversed(A)))

                dfs(node.left, A)
                dfs(node.right, A)
                A.pop()

        dfs(root, [])
        return self.ans


A = [3,9,20,None,None,15,7]
root = TreeNode().BuildTree(A)
print(Solution().smallestFromLeaf3(root))