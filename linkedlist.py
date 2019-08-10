class ListNode(object):
    def __init__(self, val, next=None):
        self.val = val
        self.next = next

def printNode(node):
    while node:
        print(node.val, end=" ")
        node = node.next
    print()

def createLinkedList(val):
    head = tail = ListNode(val[0])
    for i in range(1,len(val)):
        tail.next = ListNode(val[i])
        tail = tail.next
    return head