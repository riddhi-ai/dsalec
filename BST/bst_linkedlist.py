class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def insert(root, data):
    if root is None:
        return Node(data)

    if data < root.data:
        root.left = insert(root.left, data)
    elif data > root.data:
        root.right = insert(root.right, data)

    return root

def del_node(self,rt, value):
    if rt is None:
        return rt
    if value < rt.data:   #left subtree
        rt.left = self.del_node(rt.left,value)
    elif value>=rt.data:    #right subtree
        rt.right=self.del_node(rt.right,value)
    else:
        if rt.left is None:
            return rt.right
        if rt.right is None:
            return rt.left
        
    #when node has both left and right child
    succ=self.get_successor(rt)
    rt.data = succ.data
    rt.right = self.del_node(rt.right,succ.data)
    return rt
    


# Left → Root → Right
def inorder(root):
    if root is None:
        return

    inorder(root.left)
    print(root.data, end=" ")
    inorder(root.right)


# Root → Left → Right
def preorder(root):
    if root is None:
        return

    print(root.data, end=" ")
    preorder(root.left)
    preorder(root.right)


# Left → Right → Root
def postorder(root):
    if root is None:
        return

    postorder(root.left)
    postorder(root.right)
    print(root.data, end=" ")


# Build the BST
root = None
for value in [50, 30, 70, 20, 40, 60, 80]:
    root = insert(root, value)

print("Inorder:", end=" ")
inorder(root)
print()

print("Preorder:", end=" ")
preorder(root)
print()

print("Postorder:", end=" ")
postorder(root)
print()