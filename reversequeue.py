# reverse queue using stack
class Node:
    def __init__(self, value):
        self.data = value
        self.next = None


class Stack:
    #(push print)
    
    def __init__(self):
        self.top = None

    def push(self, value):
        new_node = Node(value)
        new_node.next = self.top
        self.top = new_node

    def pop(self):
        if self.top is None:
            return None

        value = self.top.data
        self.top = self.top.next
        return value

    def display(self):
        temp = self.top
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


class LQueue:
    def __init__(self):
        self.front = None
        self.rear = None

    def enqueue(self, value):
        new_node = Node(value)

        if self.front is None:
            self.front = self.rear = new_node
        else:
            self.rear.next = new_node
            self.rear = new_node

    def dequeue(self):
        if self.front is None:
            print("Queue is empty")
            return None

        value = self.front.data
        self.front = self.front.next

        if self.front is None:
            self.rear = None

        return value

    def display(self):
        temp = self.front
        while temp:
            print(temp.data, end=" ")
            temp = temp.next
        print()


def reverse_queue(q1):
    st1 = Stack()

    # Move queue values into stack
    while q1.front is not None:
        st1.push(q1.dequeue())

    # Move stack values back into queue
    while st1.top is not None:
        q1.enqueue(st1.pop())


que = LQueue()
que.enqueue(15)
que.enqueue(67)
que.enqueue(55)
que.enqueue(100)
que.enqueue(88)

print("Original queue:")
que.display()

reverse_queue(que)
print("Reversed queue:")
que.display()

