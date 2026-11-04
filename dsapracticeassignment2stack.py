class Stack:
    def __init__(self):
        self.items = []

    # 1. Push Operation
    def push(self, val):
        self.items.append(val)
        print(f"Pushed {val} onto stack.")

    # 2. Pop Operation
    def pop(self):
        if self.is_empty():
            print("Stack Underflow! Stack is empty.")
            return None
        return self.items.pop()

    # 3. Display Operation
    def display(self):
        if self.is_empty():
            print("Stack is empty.")
        else:
            print("Stack elements (top to bottom):", self.items[::-1])

    def is_empty(self):
        return len(self.items) == 0


# 4. Reverse String using Stack
def reverse_string(text):
    s = Stack()
    # Push all characters onto internal list
    for char in text:
        s.items.append(char)
    
    reversed_str = ""
    while not s.is_empty():
        reversed_str += s.items.pop()
    
    return reversed_str


# 5. Reverse Stack using another Stack
def reverse_stack(original_stack):
    if original_stack.is_empty():
        print("Stack is empty! Nothing to reverse.")
        return

    temp_stack = Stack()
    
    # Move elements to temporary stack (reverses order)
    while not original_stack.is_empty():
        temp_stack.items.append(original_stack.items.pop())
        
    # Copy back reversed elements to original stack
    original_stack.items = temp_stack.items


# --- Menu Driven Code ---
if __name__ == "__main__":
    my_stack = Stack()
    
    while True:
        print("\n--- STACK MENU ---")
        print("1. Push")
        print("2. Pop")
        print("3. Display")
        print("4. Reverse String using Stack")
        print("5. Reverse Stack using another Stack")
        print("6. Exit")
        
        choice = input("Enter choice (1-6): ").strip()
        
        if choice == '1':
            val_input = input("Enter value(s) to push (space separated): ")
            # Splitting allows pushing multiple numbers individually
            for val in val_input.split():
                my_stack.push(val)
        elif choice == '2':
            val = my_stack.pop()
            if val is not None:
                print(f"Popped value: {val}")
        elif choice == '3':
            my_stack.display()
        elif choice == '4':
            text = input("Enter a string: ")
            print("Reversed String:", reverse_string(text))
        elif choice == '5':
            reverse_stack(my_stack)
            print("Stack reversed successfully!")
        elif choice == '6':
            print("Exiting program.")
            break
        else:
            print("Invalid choice! Try again.")