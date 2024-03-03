"""
LinkedLists
    - have nodes
    
Nodes
    - have data
    - have a reference to another Node
"""


# Node Class
class Node:
    # Initialize Node
    def __init__(self, data=0):
        self.data = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None

    # Insert at Beginning
    def insert_at_beginning(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        else:
            new_node.next = self.head
            self.head = new_node

    # Insert at a Specific Index
    def insert_at_specific_index(self, data, index):
        new_node = Node(data)
        current_node = self.head
        position = 0
        if position == index:
            self.insert_at_beginning(data)
        else:
            while current_node != None and position + 1 != index:
                position += 1
                current_node = current_node.next
            if current_node != None:
                new_node.next = current_node.next
                current_node.next = new_node
            else:
                print("Index does not exist.")

    # Insert at End
    def insert_at_end(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        current_node = self.head
        while current_node.next:
            current_node = current_node.next
        current_node.next = new_node

    # Update Node
    def update_node(self, val, index):
        current_node = self.head
        position = 0
        if position == index:
            current_node.data = val
        else:
            while current_node != None and position != index:
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.data = val
            else:
                print("Index does not exist")

    # Delete First Node
    def delete_first_node(self):
        if self.head == None:
            return
        else:
            self.head = self.head.next

    # Delete Last Node
    def delete_last_node(self):
        if self.head is None:
            return
        current_node = self.head
        while current_node.next.next:
            current_node = current_node.next
        current_node.next = None

    # Delete Node at given Index
    def delete_node_at_index(self, index):
        if self.head == None:
            return
        current_node = self.head
        position = 0
        if position == index:
            self.delete_first_node()
        else:
            while current_node != None and position + 1 != index:
                position += 1
                current_node = current_node.next
            if current_node != None:
                current_node.next = current_node.next.next
            else:
                print("Index does not exist")

    # Delete a LinkedList Node of a given Data
    def delete_node_with_data(self, val):
        current_node = self.head
        if current_node.data == val:
            self.delete_first_node()
            return
        while current_node is not None and current_node.next.data != val:
            current_node = current_node.next
        if current_node is None:
            return
        else:
            current_node.next = current_node.next.next

    # Traverse, Print the Data at Each Node
    def print_ll(self):
        current_node = self.head
        while current_node:
            if current_node.next is None:
                print(current_node.data)
            else:
                print(current_node.data + "->", end="")
            current_node = current_node.next

    # Get Length of LinkedList
    def get_ll_length(self):
        ll_length = 0
        if self.head:
            current_node = self.head
            while current_node:
                ll_length += 1
                current_node = current_node.next
            return ll_length
        else:
            return 0

    # Reverse LinkedList
    # 1 -> 2 -> 3 -> 4 -> 5 to 1 <- 2 <- 3 <- 4 <- 5
    def reverse_ll(self):
        if self.head is None:
            return
        current_node = self.head
        if current_node.next is None:
            return
        prev = None
        while current_node.next is not None:
            temp = current_node.next
            current_node.next = prev
            prev = current_node
            current_node = temp
        current_node.next = prev
        self.head = current_node


my_linked_list = LinkedList()
my_linked_list.insert_at_end("c")
my_linked_list.insert_at_beginning("b")
my_linked_list.insert_at_beginning("a")
my_linked_list.print_ll()
my_linked_list.reverse_ll()
my_linked_list.print_ll()
