class TreeNode(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def BuildTree(self, A):
        root = TreeNode(A[0])
        nodeQueue = [root]
        front = 0
        index = 1
        while index < len(A):
            node = nodeQueue[front]
            front = front + 1

            item = A[index]
            index = index + 1
            if item != None:
                node.left = TreeNode(item)
                nodeQueue.append(node.left)

            if index >= len(A):
                break

            item = A[index]
            index = index + 1
            if item != None:
                node.right = TreeNode(item)
                nodeQueue.append(node.right)
        return root

    # Root, Left, Right by level
    def printLevelorder(self):
        if not self:
            return []
        ret = []
        level = [self]
        while level:
            currentNode = []
            nextLevel = []
            for node in level:
                currentNode.append(node.val)
                if node.left:
                    nextLevel.append(node.left)
                if node.right:
                    nextLevel.append(node.right)
            ret.append(currentNode)
            level = nextLevel
        print(ret)

