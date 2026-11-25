"""
class Node:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None


class BST():
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
    def get_successor(self,temp):
        temp=temp.right
        while temp is not None and temp.left is not None:
            temp=temp.left
        return temp

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

    """
"""
    def print_tree(root, level=0):
        if root is None:
            return

        print_tree(root.right, level + 1)
        print("    " * level + str(root.data))
        print_tree(root.left, level + 1)

    print("BST before traversal:")
    print_tree(root)

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
    """
"""
    b1=BST()
    b1.insert(Node(100))
    b1.insert(Node(10))
    b1.insert(Node(450))
    b1.insert(Node(4))
    b1.insert(Node(65))
    b1.insert(Node(300))
    b1.insert(Node(500))
    b1.insert(Node(50))
    print("\n Inorder:")
    b1.inorder(b1.root)
    #print("\No of node:", b1.cnt)
    print("\n Preorder:")
    b1.preorder(b1.root)
    print("\n Postorder:")
    b1.postorder(b1.root)
    #b1.findminmax()
    b1.del_node(b1.root,4)
    print("After Deletion:")
    b1.inorder(b1.root)

    """
    """