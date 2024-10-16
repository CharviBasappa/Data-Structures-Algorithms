class TreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

# Inorder traversal: Left, Root, Right
def inorder_traversal(root):
    if root:
        inorder_traversal(root.left)
        print(root.data, end=" ")
        inorder_traversal(root.right)

# Preorder traversal: Root, Left, Right
def preorder_traversal(root):
    if root:
        print(root.data, end=" ")
        preorder_traversal(root.left)
        preorder_traversal(root.right)

# Postorder traversal: Left, Right, Root
def postorder_traversal(root):
    if root:
        postorder_traversal(root.left)
        postorder_traversal(root.right)
        print(root.data, end=" ")

# Example usage
if __name__ == "__main__":
    # Creating the following binary tree:
    #        1
    #       / \
    #      2   3
    #     / \
    #    4   5

    root = TreeNode(1)
    root.left = TreeNode(2)
    root.right = TreeNode(3)
    root.left.left = TreeNode(4)
    root.left.right = TreeNode(5)

    print("Inorder Traversal:")
    inorder_traversal(root)
    print("\nPreorder Traversal:")
    preorder_traversal(root)
    print("\nPostorder Traversal:")
    postorder_traversal(root)


    #Inorder:- Left, Root, Right
    #Preorder:- Root, Left, Right
    #Postorder:- Left, Right, Root
