class node:
    def __init__(self,data,priority):
        self.data=data
        self.priority=priority
        self.next=None

class PriorityQueue:
    def __init__(self):
        self.front=None

    def enqueue(self,new_node):
        if self.front is None or new_node.priority < self.front.priority:
            new_node.next=self.front
            self.front=new_node
        else:
            temp=self.front

            while temp.next and temp.next.priority <= new_node.priority:
                temp=temp.next

            new_node.next=temp.next
            temp.next=new_node
