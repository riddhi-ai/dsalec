class node:
    def __init__(self, value, pr):
        self.data = value
        self.priority = pr
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if self.front is None:
            self.front = new_node
            return

        if new_node.priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next and temp.next.priority <= new_node.priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    def dequeue(self):
        if self.front:
            temp = self.front
            print("Node deleted:", temp.data)
            self.front = self.front.next
        else:
            print("Queue is empty")

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


# Create priority queue
pq = PriorityQueue()
pq.enqueue(node(100, 2))
pq.enqueue(node(500, 6))
pq.enqueue(node(300, 3))
pq.enqueue(node(600, 1))
pq.enqueue(node(700, 7))

pq.display()

pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()
pq.dequeue()

pq.display()


"""
class PriorityQueue:

    def enqueue(self, new_node):
        new_node.next=temp

    def dequeue(self):
        if self.front:
            temp=self.front
            print("Node Deleted:",temp.data)
            self.front=self.front.next
            temp=None
        else:
            print("Queue is empty")


    def display(self):
        temp=self
        while temp:


pq=PriorityQueue()
pq.enqueue(node(100,2))
pq.enqueue(node(90,3))
pq.enqueue(node(90,3))
pq.enqueue(node(90,3))
pq.dequeue()
"""