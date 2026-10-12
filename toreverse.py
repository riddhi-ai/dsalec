#Node class
class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

#Linked List class
class LinkedList:
    def __init__(self):
        self.head = None

    #Append a new node at the end
    def append(self, data):
        new_node = Node(data)
        if self.head is None:
            self.head = new_node
            return
        last = self.head
        while last.next:
            last = last.next
        last.next = new_node

    #Delete a node by value
    def delete(self, data):
        temp = self.head

        #If head node itself holds the data
        if temp and temp.data == data:
            self.head = temp.next
            temp = None
            return

        #Search for the node to delete
        prev = None
        while temp and temp.data != data:
            prev = temp
            temp = temp.next

        #If data not found
        if temp is None:
            return

        #Unlink the node
        prev.next = temp.next
        temp = None

    #Reverse the linked list
    def reverse(self):
        prev = None
        current = self.head
        while current:
            nxt = current.next   #to store next node
            current.next = prev  #to reverse the link
            prev = current       #to move prev forward
            current = nxt        #to move current forward
        self.head = prev

    #Print the list
    def print_list(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

# example
ll = LinkedList()
ll.append(10)
ll.append(20)
ll.append(30)
ll.append(40)

print("Original:")
ll.print_list()

ll.reverse()
print("Reversed:")
ll.print_list()

ll.delete(30)
print("After deleting 30:")
ll.print_list()
