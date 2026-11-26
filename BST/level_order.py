class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None

    # INSERT
    def insert(self, node):
        self.root = self._insert(self.root, node)

    def _insert(self, root, node):
        if root is None:
            return node

        if node.data < root.data:
            root.left = self._insert(root.left, node)
        elif node.data > root.data:
            root.right = self._insert(root.right, node)

        return root

    # SEARCH
    def search(self, root, key):
        if root is None:
            return False

        if root.data == key:
            return True

        if key < root.data:
            return self.search(root.left, key)

        return self.search(root.right, key)

    # MINIMUM
    def minimum(self, root):
        while root.left:
            root = root.left
        return root.data

    # MAXIMUM
    def maximum(self, root):
        while root.right:
            root = root.right
        return root.data

    # DELETE
    def get_successor(self, root):
        temp = root.right
        while temp.left:
            temp = temp.left
        return temp

    def delete(self, root, key):
        if root is None:
            return root

        if key < root.data:
            root.left = self.delete(root.left, key)

        elif key > root.data:
            root.right = self.delete(root.right, key)

        else:
            if root.left is None:
                return root.right

            if root.right is None:
                return root.left

            successor = self.get_successor(root)
            root.data = successor.data
            root.right = self.delete(root.right, successor.data)

        return root

    # INORDER
    def inorder(self, root):
        if root:
            self.inorder(root.left)
            print(root.data, end=" ")
            self.inorder(root.right)

    # PREORDER
    def preorder(self, root):
        if root:
            print(root.data, end=" ")
            self.preorder(root.left)
            self.preorder(root.right)

    # POSTORDER
    def postorder(self, root):
        if root:
            self.postorder(root.left)
            self.postorder(root.right)
            print(root.data, end=" ")

    # LEVEL ORDER (LEVEL WISE)
    def level_order(self, root):
        if root is None:
            return

        queue = [root]
        level = 0

        while queue:
            size = len(queue)

            print(f"Level {level} :", end=" ")

            for i in range(size):
                temp = queue.pop(0)

                print(temp.data, end=" ")

                if temp.left:
                    queue.append(temp.left)

                if temp.right:
                    queue.append(temp.right)

            print()
            level += 1

    # COUNT LEAF NODES
    def count_leaf(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 1

        return self.count_leaf(root.left) + self.count_leaf(root.right)

    # COUNT NON LEAF NODES
    def count_nonleaf(self, root):
        if root is None:
            return 0

        if root.left is None and root.right is None:
            return 0

        return 1 + self.count_nonleaf(root.left) + self.count_nonleaf(root.right)

    # COUNT TOTAL NODES
    def count_nodes(self, root):
        if root is None:
            return 0

        return 1 + self.count_nodes(root.left) + self.count_nodes(root.right)


# DRIVER CODE
b1 = BST()

for x in [100, 10, 450, 4, 2, 7, 500, 300]:
    b1.insert(Node(x))

print("Inorder:")
b1.inorder(b1.root)

print("\n\nPreorder:")
b1.preorder(b1.root)

print("\n\nPostorder:")
b1.postorder(b1.root)

print("\n\nLevel Order:")
b1.level_order(b1.root)

print("\nMinimum =", b1.minimum(b1.root))
print("Maximum =", b1.maximum(b1.root))

print("Search 300 =", b1.search(b1.root, 300))
print("Search 600 =", b1.search(b1.root, 600))

print("Leaf Nodes =", b1.count_leaf(b1.root))
print("Non Leaf Nodes =", b1.count_nonleaf(b1.root))

print("Total Nodes =", b1.count_nodes(b1.root))
