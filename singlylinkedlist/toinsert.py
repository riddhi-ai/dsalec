# singly linear linked list

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None

class SLL:
    def __init__(self):
        self.head = None

    def append(self, new_node):
        if self.head is None:
            self.head = new_node
        else:
            temp = self.head
            while temp.next:
                temp = temp.next
            temp.next = new_node

    def insert(self, new_node, pos):
        # Insert at beginning
        if pos == 1:
            new_node.next = self.head
            self.head = new_node
            return

        # Traverse to the node before the desired position
        p = 1
        temp = self.head
        while temp and p != pos - 1:
            temp = temp.next
            p += 1

        if temp is None:
            print("Position out of range")
            return

        new_node.next = temp.next
        temp.next = new_node

    def print(self):
        temp = self.head
        while temp:
            print(temp.data, end=" - ")
            temp = temp.next
        print("None")


# Usage
list1 = SLL()
list1.append(Node(10))
list1.append(Node(20))
list1.append(Node(30))
list1.append(Node(40))

list1.insert(Node(25), 3)   # Insert at position 3
list1.insert(Node(5), 1)    # Insert at head

list1.print()
