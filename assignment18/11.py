class Node:
    def __init__(self, pid, name, priority):
        self.pid = pid
        self.name = name
        self.priority = priority
        self.next = None


class PriorityQueue:  #creates an empty priority queue
    def __init__(self):
        self.front = None

    # 1 to Add Process
    def enqueue(self, pid, name, priority):
        new_node = Node(pid, name, priority)

        if self.front is None or priority < self.front.priority:
            new_node.next = self.front
            self.front = new_node
        else:
            temp = self.front

            while temp.next and temp.next.priority <= priority:
                temp = temp.next

            new_node.next = temp.next
            temp.next = new_node

    # 2 Execute Process
    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Executing:", self.front.pid, self.front.name)
            self.front = self.front.next

    # 3 to View Next Process
    def display_next(self):
        if self.front is None:
            print("Queue is empty")
        else:
            print("Next Process:", self.front.pid,
                  self.front.name, self.front.priority)

    # 4 to Display All Processes
    def display_all(self):
        if self.front is None:
            print("Queue is empty")
        else:
            temp = self.front

            while temp:
                print(temp.pid, temp.name, temp.priority)
                temp = temp.next

    # 5 to Count Processes
    def count(self):
        temp = self.front
        c = 0

        while temp:
            c += 1
            temp = temp.next

        print("Total Processes:", c)


# Main Program
pq = PriorityQueue()

pq.enqueue(101, "Backup", 3)
pq.enqueue(102, "Keyboard Input", 2)
pq.enqueue(103, "System Update", 1)
pq.enqueue(104, "Cleanup", 4)

print("All Processes:")
pq.display_all()

print("\nNext Process:")
pq.display_next()

print("\nExecuting Process:")
pq.dequeue()

print("\nRemaining Processes:")
pq.display_all()

print("\nProcess Count:")
pq.count()