class node:
    def __init__(self, data, priority):
        self.data = data
        self.priority = priority
        self.next = None


class PriorityQueue:
    def __init__(self):
        self.front = None

    def enqueue(self, new_node):
        if self.front is None or new_node.priority < self.front.priority:
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
            print("Node Deleted:", temp.data)
            self.front = self.front.next
            temp.next = None
        else:
            print("Queue is empty")

    def display(self):
        if self.front is None:
            print("Queue is empty")
            return

        temp = self.front
        while temp:
            print(f"{temp.data} (priority: {temp.priority})", end=" -> ")
            temp = temp.next
        print("None")


pq = PriorityQueue()
pq.enqueue(node(100, 2))
pq.enqueue(node(90, 3))
pq.enqueue(node(90, 3))
pq.enqueue(node(90, 3))

pq.display()
pq.dequeue()
pq.display()