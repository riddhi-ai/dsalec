class Node:
    def __init__(self, score):
        self.score = score
        self.left = None
        self.right = None


def insert(root, score):
    if root is None:
        return Node(score)

    if score < root.score:
        root.left = insert(root.left, score)
    else:
        root.right = insert(root.right, score)

    return root


def inorder(root, scores):
    if root is not None:
        inorder(root.left, scores)
        scores.append(root.score)
        inorder(root.right, scores)


def search(root, score):
    if root is None:
        return False
    if score == root.score:
        return True
    if score < root.score:
        return search(root.left, score)
    return search(root.right, score)


root = None
for score in [45, 78, 32, 89, 56, 92, 67, 34, 85, 73, 61, 98]:
    root = insert(root, score)

while True:
    print("""
1. Insert a score
2. Display scores in ascending order
3. Find highest and lowest scores
4. Count students scoring above 50
5. Search for a score
6. Find average score
7. Exit
""")
    choice = input("Enter your choice: ").strip()

    if choice == "7":
        break

    if choice in ("1", "5"):
        try:
            score = int(input("Enter score (0–100): "))
        except ValueError:
            print("Enter a whole number.")
            continue

        if not 0 <= score <= 100:
            print("Score must be between 0 and 100.")
        elif choice == "1":
            root = insert(root, score)
            print("Score inserted.")
        elif search(root, score):
            print("Score found.")
        else:
            print("Score not found.")

    elif choice in ("2", "3", "4", "6"):
        scores = []
        inorder(root, scores)

        if choice == "2":
            print("Ascending order:", scores)
        elif choice == "3":
            print("Highest score:", scores[-1])
            print("Lowest score:", scores[0])
        elif choice == "4":
            print("Students scoring above 50:",
                  sum(1 for score in scores if score > 50))
        else:
            print("Average score:", sum(scores) / len(scores))

    else:
        print("Invalid choice. Enter a number from 1 to 7.")