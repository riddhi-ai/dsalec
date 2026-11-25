# insert, traversal ,delete node, min max ,search (key),level-order-traversal, count leaf nodes , count non-leaf node
#recursive code

class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST:
    def __init__(self):
        self.root = None
        self.count=0
        self.countnonleaf=0

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

    def get_successor(self, root):
        # Find the smallest node in the right subtree.
        successor = root.right
        while successor.left is not None:
            successor = successor.left
        return successor

    def del_node(self, root, value):
        self.root = self._delete(root, value)

    def _delete(self, root, value):
        if root is None:
            return None

        if value < root.data:
            root.left = self._delete(root.left, value)
        elif value > root.data:
            root.right = self._delete(root.right, value)
        else:
            # Zero or one child
            if root.left is None:           #node with right child only
                return root.right
            if root.right is None:          #node with left child only
                return root.left

            # Two children - Node has both left and right child
            successor = self.get_successor(root)
            root.data = successor.data
            root.right = self._delete(root.right, successor.data)

        return root

    # Left → Root → Right
    def inorder(self, root):
        if root is None:
            return

        self.inorder(root.left)
        if root.left is None and root.right is None:   #to count leaf nodes
                    self.count+=1
        if root.left is not None and root.right is not None:  # to count non leaf nodes
                          self.countnonleaf+=1
        print(root.data, end=" ")
        self.inorder(root.right)
       

    # Root → Left → Right
    def preorder(self, root):
        if root is None:
            return

        print(root.data, end=" ")
        self.preorder(root.left)
        self.preorder(root.right)

    # Left → Right → Root
    def postorder(self, root):
        if root is None:
            return

        self.postorder(root.left)
        self.postorder(root.right)
        print(root.data, end=" ")


    def search (self,key):
        temp= self.root
        while temp:
            if temp.data == key:
                return True
            elif key <temp.data:
                temp=temp.left
            else:
                temp=temp.right
        return False

    def findminmax(self):
        if self.root is None:
            print("\nTree is empty")
            return

        temp = self.root
        while temp.left:
            temp = temp.left
        print("\nMin:", temp.data)

        temp = self.root
        while temp.right:
            temp = temp.right
        print("Max:", temp.data)


b1 = BST()
b1.insert(Node(100))
b1.insert(Node(10))
b1.insert(Node(450))
b1.insert(Node(4))
b1.insert(Node(65))
b1.insert(Node(300))
b1.insert(Node(500))
b1.insert(Node(50))

print("Inorder:")
b1.inorder(b1.root)

print("\nPreorder:")
b1.preorder(b1.root)

print("\nPostorder:")
b1.postorder(b1.root)

b1.findminmax()

b1.del_node(b1.root, 4)
print("\nAfter Deletion:")
b1.inorder(b1.root)
print()

print("\n Total Number of Leaf Nodes:", b1.count) 
print("\n Total Number of Non Leaf Nodes:", b1.countnonleaf) 

if b1.search(50):
    print("\n Found the node")
else :
    print("\n NOT found")


if b1.search(150):
    print("\n Found the node")
else :
    print("\n Node not found")

