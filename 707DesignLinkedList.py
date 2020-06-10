class ListNode(object):
    def __init__(self, val=None, next=None):
        self.val = val
        self.next = next

class MyLinkedList(object):
    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.head = None
        self.length = 0

    def get(self, index):
        """
        Get the value of the index-th node in the linked list. If the index is invalid, return -1.
        :type index: int
        :rtype: int
        """
        if index < 0 or index >= self.length:
            return -1
        if self.head == None:
            return -1
        cur = self.head
        for i in range(index):
            cur = cur.next
        return cur.val

    def addAtHead(self, val):
        """
        Add a node of value val before the first element of the linked list. After the insertion, the new node will be the first node of the linked list.
        :type val: int
        :rtype: None
        """
        node = ListNode(val)
        node.next = self.head
        self.head = node
        self.length += 1

    def addAtTail(self, val):
        """
        Append a node of value val to the last element of the linked list.
        :type val: int
        :rtype: None
        """
        p = self.head
        if p == None:
            self.head = ListNode(val)
        else:
            while p.next != None:
                p = p.next
            p.next = ListNode(val)

        self.length += 1

    def addAtIndex(self, index, val):
        """
        Add a node of value val before the index-th node in the linked list.
        If index equals to the length of linked list, the node will be appended to the end of linked list.
        If index is greater than the length, the node will not be inserted.
        :type index: int
        :type val: int
        :rtype: None
        """
        if index > self.length:
            return
        elif index <= 0:
            self.addAtHead(val)
        else:
            cur = self.head
            for i in range(index - 1):
                cur = cur.next
            cur.next = ListNode(val, cur.next)
            self.length += 1

    def deleteAtIndex(self, index):
        """
        Delete the index-th node in the linked list, if the index is valid.
        :type index: int
        :rtype: None
        """
        if index < 0 or index >= self.length:
            return
        cur = self.head
        if index == 0:
            self.head = cur.next
        else:
            for i in range(index - 1):
                cur = cur.next
            cur.next = cur.next.next
        self.length -= 1

# Your MyLinkedList object will be instantiated and called as such:
obj = MyLinkedList()
print(obj.addAtHead(1))
print(obj.addAtTail(3))
print(obj.addAtIndex(4,2))
print(obj.get(1))
print(obj.deleteAtIndex(-1))
print(obj.get(1))
