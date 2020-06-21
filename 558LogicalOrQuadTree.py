"""
A Binary Matrix is a matrix in which all the elements are either 0 or 1.

Given quadTree1 and quadTree2. quadTree1 represents a n * n binary matrix and quadTree2
represents another n * n binary matrix.

Return a Quad-Tree representing the n * n binary matrix which is the result of
logical bitwise OR of the two binary matrixes represented by quadTree1 and quadTree2.

Notice that you can assign the value of a node to True or False when isLeaf is False,
and both are accepted in the answer.
"""
from QuadTree import Node

class Solution:
    def intersect(self, quadTree1: 'Node', quadTree2: 'Node') -> 'Node':
        if quadTree1.isLeaf:
            return quadTree1.val and quadTree1 or quadTree2
        elif quadTree2.isLeaf:
            return quadTree2.val and quadTree2 or quadTree1
        else:
            tLeft = self.intersect(quadTree1.topLeft, quadTree2.topLeft)
            tRight = self.intersect(quadTree1.topRight, quadTree2.topRight)
            bLeft = self.intersect(quadTree1.bottomLeft, quadTree2.bottomLeft)
            bRight = self.intersect(quadTree1.bottomRight, quadTree2.bottomRight)
            if tLeft.isLeaf and tRight.isLeaf and bLeft.isLeaf and bRight.isLeaf and tLeft.val == tRight.val == bLeft.val == bRight.val:
                node = Node(tLeft.val, True, None, None, None, None)
            else:
                node = Node(False, False, tLeft, tRight, bLeft, bRight)
        return node


A = [[0, 1], [1, 1], [1, 1], [1, 0], [1, 0]]
quadTree1 = Node(None, None).BuildTree(A)
A = [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
quadTree2 = Node(None, None).BuildTree(A)

# A = [[0,0],[1,0],[1,0],[1,1],[1,1]]
# quadTree1 = Node(None, None).BuildTree(A)
# A = [[0,0],[1,1],[1,1],[1,0],[1,1]]
# quadTree2 = Node(None, None).BuildTree(A)


root = Solution().intersect(quadTree1, quadTree2)
root.printLevelorder()

