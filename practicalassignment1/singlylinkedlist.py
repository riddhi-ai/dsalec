class Node:
        def __init__(self,data):
            self.data=data
            self.next=None
class LinkedList:
        def __init__(self):
            self.head=None

    #Append
        def append(self,data):
            new=Node(data)  # new node

            if self.head is None:  #to check if list is empty
                self.head=new       #if head is empty then list is empty
                return

            temp= self.head         #moves to last node
            while temp.next :
                temp=temp.next
            temp.next=new       #connects to new node


    #Traverse and Print

        def display(self):
                temp=self.head  #start with the first node
                while temp: #traverse through every node
                    print(temp.data,end=" -> ")  #prints node's value
                    temp=temp.next  #moves to the next node
                print("Null")  

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

        # Delete alternate nodes (keeping 1st, 3rd, 5th)
        def delete_alternate(self):
            temp = self.head
            while temp and temp.next:
                temp.next = temp.next.next
                temp = temp.next





ll=LinkedList()

ll.append(20)
ll.append(25)
ll.append(30)
ll.append(35)
ll.append(40)

print("Original List is:")
ll.display()

print("Original list:")
ll.display()

ll.insert(25, 3)
print("After insertion:")
ll.display()

ll.delete_alternate()
print("After deleting alternate nodes:")
ll.display()
