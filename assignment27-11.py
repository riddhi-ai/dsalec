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


marks = [45, 78, 32, 89, 56, 92, 67, 34, 85, 73, 61, 98]

root = None
for mark in marks:
    root = insert(root, mark)

scores = []
inorder(root, scores)

print("Ascending order:", scores)
print("Highest score:", scores[-1])
print("Lowest score:", scores[0])
print("Students scoring above 50:", sum(1 for score in scores if score > 50))

target = int(input("Enter a score to search: "))
if search(root, target):
    print("Score found")
else:
    print("Score not found")

print("Average score:", sum(scores) / len(scores))