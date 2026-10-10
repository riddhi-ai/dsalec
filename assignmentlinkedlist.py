"""
Assignment1: Create a Singly Linear Linked List with following operations
1.	Create Linked List
2.	Traverse and print the node values
3.	Insert node at a specific position
4.	Find Middle node and print its value
5.	Delete node
6.	Reverse list
7.	Calculate the sum of every two consecutive node values.
"""

# Node class
class Node:
    def __init__(self, data):
        self.data = data      # store value
        self.next = None      # pointer to next node

# to create a Linked List class 
# Creates nodes one by one and connects each new node to the end of the list
class LinkedList:
    def __init__(self):
        self.head = None      # start empty

    # 1. Append node at end
    def append(self, data):
        new_node = Node(data)
        if not self.head:     # if list empty
            self.head = new_node
            return
        temp = self.head    
        while temp.next:      # go till last node
            temp = temp.next
        temp.next = new_node

    # 2. to Traverse and print 
    # the node values starts at head, prints each node's value, and moves using temp = temp.next
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" - ")
            temp = temp.next
        print("None")

    # 3. to Insert at specific position 
    #Connects the new node to the next node then connects the previous node to the new node. Position starts at 1.
    def insert(self, data, pos):
        new_node = Node(data)
        if pos == 1:          # insert at head
            new_node.next = self.head
            self.head = new_node
            return
        temp = self.head
        for _ in range(pos-2):
            if not temp: return
            temp = temp.next
        new_node.next = temp.next
        temp.next = new_node

    # 4.to Find middle node Uses two pointers: slow moves one node at a time, 
    # while fast moves two nodes at a time. When fast reaches the end, slow is at the middle.
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print("Middle node:", slow.data)

    # 5.to Delete node by value Changes the previous node's next pointer to skip the node being deleted.
    def delete(self, key):
        temp = self.head
        if temp and temp.data == key:
            self.head = temp.next
            return
        prev = None
        while temp and temp.data != key:
            prev = temp
            temp = temp.next
        if temp:
            prev.next = temp.next

    # 6.to Reverse list 
    # Reverses each link using three pointers: prev, current, and nxt
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next
            current.next = prev
            prev = current
            current = nxt
        self.head = prev

    # 7. Sum of every two consecutive nodes
    def sum_pairs(self):
        temp = self.head
        while temp and temp.next:
            s = temp.data + temp.next.data
            print(f"Sum of {temp.data} + {temp.next.data} = {s}")
            temp = temp.next.next


# Example
ll = LinkedList()
ll.append(50)
ll.append(18)
ll.append(26)
ll.append(78)
ll.append(50)

print("Original list:")
ll.print_list()

ll.insert(15, 2)          # insert 15 at position 2
ll.print_list()

ll.find_middle()          # find middle node

ll.delete(30)             # delete node with value 30
ll.print_list()

ll.reverse()              # reverse list
print("Reversed list:")
ll.print_list()

ll.sum_pairs()            # sum of consecutive pairs



