# node class represents each node in the linked list
class Node:
    def __init__(self, data=None, next=None):
        self.data = data # stores the data
        self.next = next # points to the next node

# this class manages the linked list (add,delete,search,display items)
class LinkedList:
    def __init__(self):
        self.head = None # the head points to the first node of the list

    # method for inserting a new node at the end of the list
    def insert_at_end(self, data):
        new_node = Node(data)               # creates a new node with the given data
        if self.head is None:               # if the list is empty
            self.head = new_node            # set the new node as the head of the list
            return                          # exit the function
        current = self.head                 # start from the head of the list
        while current.next:                 # keep going until we reach the last node
            current = current.next          # move to the next node
        current.next = new_node             # link the last node to the new node

    # method for inserting a new node at the start of the list
    def insert_at_start(self, data):
        new_node = Node(data)               # creates a new node with the given data
        new_node.next = self.head           # points the new node to the current head (first node)
        self.head = new_node                # updates head to the new node (new node becomes first)

    def insert_at_index(self, index, data):
        if index < 0:
            print("Invalid index")              # index can't be negative
            return
        if index == 0:
            self.insert_at_start(data)          # if index is 0, insert the node at the start
            return
        new_node = Node(data)                   # creates a new node with the given data
        current = self.head                     # start from the head of the list
        count = 0                               # counter to track the current position
        while current and count < index - 1:    # moves to the node just before where you want to insert the new node
            current = current.next
            count += 1
        if current is None:
            print("Index out of range")         # index provided is too big so user is warned
            return
        new_node.next = current.next            # points new node to the next node
        current.next = new_node                 # links previous node to the new node

    # method for deleting a node at a specified index in the list
    def delete_at_index(self, index):
        if index < 0 or self.head is None:
            print("Invalid index or empty list")        # can't delete if index is negative or list is empty
            return
        if index == 0:
            self.head = self.head.next                   # removes the first node by shifting the head
            return
        current = self.head                             # start from the beginning of the list
        count = 0                                       # counter to keep track of position
        while current.next and count < index - 1:       # moves to the node just before the one to delete
            current = current.next
            count += 1
        if current.next is None:
            print("Index out of range")                 # index provided is too big so user is warned
            return
        current.next = current.next.next                # skips the node at the index to delete it

    # method to search for a value in the list and return its index
    def search(self, value):
        current = self.head                     # start from the beginning of the list
        index = 0                               # initialize index counter
        while current:                          # loops through the list as long as there is a node
            if current.data == value:           # checks if the current node's data matches the value
                return index                    # returns the index if found
            current = current.next              # moves to the next node
            index += 1                          # increments the index counter
        return -1                               # if value not found, returns -1

    # method to display all nodes in the list
    def display(self):
        current = self.head                     # starts from the head (beginning of the list)
        while current:                          # loops through the list as long as there is a node
            print(current.data, end=" -> ")     # prints the current node's data followed by "->"
            current = current.next              # moves to the next node in the list
        print("None")                           # after the loop ends, prints "None" to indicate the end of the list


if __name__ == "__main__":
    ll = LinkedList()
    ll.insert_at_end(10)
    ll.display()
    ll.insert_at_start(5)
    ll.display()
    ll.insert_at_end(15)
    ll.display()
    ll.insert_at_index(1, 8)
    ll.display()
    ll.delete_at_index(2)
    ll.display()
    print("Index of 15:", ll.search(15))
    print("Index of 99:", ll.search(99))
