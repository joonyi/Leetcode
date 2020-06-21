
class Node:
    def __init__(self, val, isLeaf, topLeft=None, topRight=None, bottomLeft=None, bottomRight=None):
        self.val = val
        self.isLeaf = isLeaf
        self.topLeft = topLeft
        self.topRight = topRight
        self.bottomLeft = bottomLeft
        self.bottomRight = bottomRight

    def BuildTree(self, A):
        root = Node(A[0][1], A[0][0])
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(A):
            node = nodeQueue[front]
            front = front + 1

            item = A[index]
            index = index + 1
            if item != None:
                node.topLeft = Node(item[1], item[0])
                nodeQueue.append(node.topLeft)

            if index >= len(A):
                break

            item = A[index]
            index = index + 1
            if item != None:
                node.topRight = Node(item[1], item[0])
                nodeQueue.append(node.topRight)

            item = A[index]
            index = index + 1
            if item != None:
                node.bottomLeft = Node(item[1], item[0])
                nodeQueue.append(node.bottomLeft)

            item = A[index]
            index = index + 1
            if item != None:
                node.bottomRight = Node(item[1], item[0])
                nodeQueue.append(node.bottomRight)

        return root

    def printLevelorder(self):
        if not self:
            return []
        ret = []
        level = [self]
        while level:
            currentNode = []
            nextLevel = []
            for node in level:
                currentNode.append([node.isLeaf, node.val])
                if node.topLeft:
                    nextLevel.append(node.topLeft)
                if node.topRight:
                    nextLevel.append(node.topRight)
                if node.bottomLeft:
                    nextLevel.append(node.bottomLeft)
                if node.bottomRight:
                    nextLevel.append(node.bottomRight)
            ret.append(currentNode)
            level = nextLevel

        print(ret)


if __name__ == "__main__":
    A = [[0, 1], [1, 1], [1, 1], [1, 0], [1, 0]]
    quadTree1 = Node(None,None).BuildTree(A)
    A = [[0, 1], [1, 1], [0, 1], [1, 1], [1, 0], None, None, None, None, [1, 0], [1, 0], [1, 1], [1, 1]]
    quadTree2 = Node(None,None).BuildTree(A)

    quadTree1.printLevelorder()
    quadTree2.printLevelorder()
