class Node:
    def __init__(self, val):
        self.val = val
        self.next = None 

class LinkedList:
    def __init__(self):
        self.head = None 

    def insert(self, val):

        new_node = Node(val) 
        new_node.next = self.head 
        self.head = new_node 
        

    def print_list(self):
        curr = self.head
        while curr:
            print(curr.val, end=" -> ")
            curr = curr.next

ll = LinkedList()
ll.insert(3)
ll.insert(2)
ll.insert(4)
ll.insert(2)
ll.insert(1)
ll.insert(6)
ll.print_list()  # 6 -> 1 -> 2 -> 4 -> 2 -> 3 ->