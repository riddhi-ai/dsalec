class Queue:
    def __init__(self):
        self.items = []

    # 1. Enqueue Operation
    def enqueue(self, val):
        self.items.append(val)
        print(f"Enqueued {val} into queue.")

    # 2. Dequeue Operation
    def dequeue(self):
        if self.is_empty():
            print("Queue Underflow! Queue is empty.")
            return None
        return self.items.pop(0)

    # 3. Display Operation
    def display(self):
        if self.is_empty():
            print("Queue is empty.")
        else:
            print("Queue elements (front to rear):", self.items)

    def is_empty(self):
        return len(self.items) == 0


# 4. Reverse Queue using Stack
def reverse_queue(q):
    if q.is_empty():
        print("Queue is empty! Nothing to reverse.")
        return

    stack = []
    # Dequeue all elements from queue and push into stack
    while not q.is_empty():
        stack.append(q.dequeue())

    # Pop elements from stack and enqueue back into queue
    while len(stack) > 0:
        q.enqueue(stack.pop())


# 5. Merge Two Queues into One
def merge_queues(q1, q2):
    merged_q = Queue()
    
    # Copy all items from q1 and q2
    for item in q1.items:
        merged_q.items.append(item)
    for item in q2.items:
        merged_q.items.append(item)
        
    return merged_q


# 6. Check if Two Queues are Identical
def are_identical(q1, q2):
    return q1.items == q2.items


# --- Menu Driven Code ---
if __name__ == "__main__":
    q1 = Queue()
    q2 = Queue()

    while True:
        print("\n--- LINEAR QUEUE MENU ---")
        print("1. Enqueue (into Q1)")
        print("2. Dequeue (from Q1)")
        print("3. Display (Q1)")
        print("4. Reverse Queue (Q1) using Stack")
        print("5. Merge Q1 & Q2 into a new Queue")
        print("6. Check if Q1 and Q2 are Identical")
        print("7. Add elements to Q2 (for testing merge/identical)")
        print("8. Exit")

        choice = input("Enter choice (1-8): ").strip()

        if choice == '1':
            val_input = input("Enter value(s) to enqueue (space separated): ")
            for val in val_input.split():
                q1.enqueue(val)
        elif choice == '2':
            val = q1.dequeue()
            if val is not None:
                print(f"Dequeued value: {val}")
        elif choice == '3':
            q1.display()
        elif choice == '4':
            reverse_queue(q1)
            print("Queue Q1 reversed successfully!")
        elif choice == '5':
            merged = merge_queues(q1, q2)
            print("Merged Queue Result:")
            merged.display()
        elif choice == '6':
            if are_identical(q1, q2):
                print("Queues Q1 and Q2 are IDENTICAL.")
            else:
                print("Queues Q1 and Q2 are NOT identical.")
        elif choice == '7':
            val_input = input("Enter value(s) for Q2 (space separated): ")
            for val in val_input.split():
                q2.enqueue(val)
        elif choice == '8':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")