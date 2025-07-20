class Node:
    def __init__(self, val):
        self.val = val
        self.next = None

class linkedlist:
    def __init__(self):
        self.head = None

    def insert(self, val):

        new_node = Node(val)
        new_node.next = self.head
        self.head = new_node

    def printlist(self):
        curr = self.head
        print("List: ")
        while curr:
            print(curr.val, end=" -> ")
            curr= curr.next
        print("None")

ll = linkedlist()
ll.insert(3)
ll.insert(4)
ll.insert(5)
ll.printlist()