class Node:
    def __init__(self, value):
        self.data = value
        self.prev = None
        self.next = None

class LinkedList:
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
            new_node.prev = temp

    def insert(self, new_node, pos):
        if pos == 1:   # insert at head
            new_node.next = self.head
            if self.head:
                self.head.prev = new_node
            self.head = new_node
        else:
            p = 1
            temp = self.head
            while p != pos-1 and temp:
                temp = temp.next
                p += 1
            if not temp: return   # position out of range
            new_node.next = temp.next
            if temp.next:
                temp.next.prev = new_node
            temp.next = new_node
            new_node.prev = temp

    def print_forward(self):
        temp = self.head
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.next
        print("None")

    def print_backward(self):
        temp = self.head
        if not temp: return
        while temp.next:   # go to last node
            temp = temp.next
        while temp:
            print(temp.data, end=" <-> ")
            temp = temp.prev
        print("None")

    def print_list(self):   # ✅ new method
        temp = self.head
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Usage
list1 = LinkedList()
n1 = Node(10)
n2 = Node(20)
n3 = Node(30)

list1.append(n1)
list1.append(n2)
list1.append(n3)

print("Forward:")
list1.print_forward()

print("Backward:")
list1.print_backward()

print("List:")
list1.print_list()

# Insert at position 6 (ignored, out of range)
list1.insert(Node(80), 6)
list1.print_list()

# Insert at position 2 (valid)
list1.insert(Node(15), 2)
list1.print_list()
