# Root, Left, Right
def printPreorder(root):
    if root:
        print(root.val, end=' ')
        printPreorder(root.left)
        printPreorder(root.right)

# Left, Right, Root
def printPostorder(root):
    if root:
        printPostorder(root.left)
        printPostorder(root.right)
        print(root.val, end=' ')

class BinarySearchTree(object):
    def __init__(self, x=None):
        self.val = x
        self.left = None
        self.right = None

    def append(self, val):
        if val == None:
            return
        node = BinarySearchTree(val)
        self.addNode(node)

    def addNode(self, node):
        if self.val == None:
            self.val = node.val
        elif node.val < self.val:
            if self.left == None:
                self.left = node
            else:
                self.left.addNode(node)
        elif node.val > self.val:
            if self.right == None:
                self.right = node
            else:
                self.right.addNode(node)

    def search(self, val):
        found = self.searchTree(val)
        left, right = None, None
        if found:
            if found.left:
                left = found.left.val
            if found.right:
                right = found.right.val
            print("Node:{} L:{} R:{}".format(found.val,left,right))
        else:
            print("Not found")

    def searchTree(self, val):
        if val == self.val:
            return self
        elif val < self.val and self.left:
            return self.left.searchTree(val)
        elif val > self.val and self.right:
            return self.right.searchTree(val)

    # Left, Root, Right
    def printInorder(self, root):
        if root:
            self.printInorder(root.left)
            print(root.val, end=' ')
            self.printInorder(root.right)

    # Root, Left, Right by level
    def printLevelorder(self, root):
        if not root:
            return []
        ret = []
        level = [root]
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


def main():
    tree = BinarySearchTree()
    a = [3,6,2,4,8,1,7,9]
    # a = [i for i in range(1,10)]
    for i in a:
        tree.append(i)

    BinarySearchTree().printLevelorder(tree)
    BinarySearchTree().printInorder(tree)

if __name__== "__main__":
    main()