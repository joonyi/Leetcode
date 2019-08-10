"""
Given an n-ary tree, return the level order traversal of its nodes' values.
(ie, from left to right, level by level).

For example, given a 3-ary tree:
"""
class Solution(object):
    def levelOrder(self, root):
        """
        :type root: Node
        :rtype: List[List[int]]
        """
        if not root: return None

        queue = [root]
        res = []
        while queue:
            tmp = []
            nxt_level = []
            for node in queue:
                tmp.append(node.val)
                for child in node.children:
                    nxt_level.append(child)

            queue = nxt_level
            res.append(tmp)

        return res

    def levelOrder2(self, root):
        q, ret = [root], []
        while any(q):
            ret.append([node.val for node in q])
            q = [child for node in q for child in node.children if child]
        return ret