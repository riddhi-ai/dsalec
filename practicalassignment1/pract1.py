
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class LinkedList:
    def __init__(self):
        self.head = None

    # 1. Create linked list (append)
    def append(self, data):
        new = Node(data)
        if self.head is None:
            self.head = new
            return
        temp = self.head
        while temp.next:
            temp = temp.next
        temp.next = new

    # 2. Traverse and print
    def display(self):
        temp = self.head
        while temp:
            print(temp.data, end=" -> ")
            temp = temp.next
        print("NULL")

    # 3. Insert at a specific position (1-based)
    def insert(self, data, pos):
        new = Node(data)
        if pos == 1:
            new.next = self.head
            self.head = new
            return
        temp = self.head
        for i in range(pos - 2):
            if temp is None:
                print("Invalid position")
                return
            temp = temp.next
        if temp is None:
            print("Invalid position")
            return
        new.next = temp.next
        temp.next = new

    # 4. Delete alternate nodes (keep 1st, 3rd, 5th...)
    def delete_alternate(self):
        temp = self.head
        while temp and temp.next:
            temp.next = temp.next.next
            temp = temp.next


ll = LinkedList()

ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
ll.append(50)

print("Original list:")
ll.display()

ll.insert(25, 3)
print("After insertion:")
ll.display()

ll.delete_alternate()
print("After deleting alternate nodes:")
ll.display()
