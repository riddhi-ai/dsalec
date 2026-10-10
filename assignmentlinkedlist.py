# Node class
class Node:
    def __init__(self, data):
        self.data = data      # store value
        self.next = None      # pointer to next node

# Linked List class
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

    # 2. Traverse and print
    def print_list(self):
        temp = self.head
        while temp:
            print(temp.data, end=" - ")
            temp = temp.next
        print("None")

    # 3. Insert at specific position
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

    # 4. Find middle node
    def find_middle(self):
        slow = self.head
        fast = self.head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        if slow:
            print("Middle node:", slow.data)

    # 5. Delete node by value
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

    # 6. Reverse list
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


# Usage Example
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)
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



"""
class Node:
    def __init__ (self,data):
        self.data=next #stores value of next
        self.next=none #pointer to next node

#to create a linkedlist class
class LinkedList:
    def __init__(self):
        self.head=none #to start empty

        #to append node at end 
        def append(self,data):
            new_node=node(data)
            if not self.head:
                self.head = new_node
                return
            temp=self.head
            while temp.next:
                temp=temp.next
            temp.next=new_node


    def print_linkedlist(self):
        temp=self.head
        while temp:
            print(temp.data,end=" ")
            temp=temp.next
        print(None)

    
    def insert_linkedlist(self,data,pos):
        new_node = Node(data)
        if pos ==1:
            new_node.next=self.head

    






"""