# Reverse queue using stack

class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    def __init__(self):
        self.top = None

    def push(self, new_node):
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        value = self.top.data
        self.top = self.top.next
        return value

    def print(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, element):
        new_node = Node(element)

        if self.rear is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.is_empty():
            print("Queue is empty")
            return None

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def is_empty(self):
        return self.front is None

    def printQueue(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def reverse_queue(q1):
    st1 = Stack()

    while not q1.is_empty():
        st1.push(Node(q1.dequeue()))

    while st1.top is not None:
        q1.enqueue(st1.pop())


# Create a queue
myQueue = LQueue()
myQueue.enqueue(11)
myQueue.enqueue(58)
myQueue.enqueue(22)

print("Original queue: ", end="")
myQueue.printQueue()

reverse_queue(myQueue)

print("Reversed queue: ", end="")
myQueue.printQueue()