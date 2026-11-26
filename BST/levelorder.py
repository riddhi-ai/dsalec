# insert, traversal ,delete node, min max ,search (key),level-order-traversal, count leaf nodes , count non-leaf node
#count no. of nodes in left/right subtree , count total number of nodes
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

    def level_order(self,root):
         if root is None:
              print ("BST is empty")
         arr=[]
         cnt=0
         arr.append(root)
         while (cnt <len(arr)):
              temp=arr[cnt]
              cnt+=1
              print(temp.data, end=" ")
              if temp.left:
                   arr.append(temp.left)
              if temp.right:
                   arr.append(temp.right)

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


print("\n Total Number of Leaf Nodes:", b1.count) 
print("\n Total Number of Non Leaf Nodes:", b1.countnonleaf) 

print("\n Level order:")
b1.level_order(b1.root)