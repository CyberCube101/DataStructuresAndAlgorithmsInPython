''' We need 2 classes. A node class and a linked list class
that contain nodes'''

class Node:
    def __init__(self, data):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    def print_list(self):
        cur_node = self.head
        while cur_node:
            print(cur_node.data)
            cur_node = cur_node.next

    def append(self, data):
        new_node = Node(data)  # New Object

        if self.head is None:  # check list is empty, if yes set our new node to the head
            self.head = new_node
            return

        last_node = self.head  # initially at head
        # now we need to move through the list
        while last_node.next:  # while the next pointer does not point to null
            last_node = last_node.next  # ie B pointing to C
        last_node.next = new_node

    def prepend(self, data):  # if we want to put a node to the front
        new_node = Node(data)
        new_node.next = self.head
        self.head = new_node

    def insert_after_node(self, prev_node, data):
        if not prev_node:
            print("Previous node not in list")
            return
        new_node = Node(data)
        new_node.next = prev_node.next
        prev_node.next = new_node


llist = LinkedList()
llist.append("A")
llist.append("B")
llist.append("C")
llist.append("D")
llist.prepend("E")
llist.insert_after_node(llist.head.next, "F")
llist.print_list()
