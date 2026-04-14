"""
Write a Python program to insert a node with value 6 into the following binary tree. With the following specific
requirements:
    1) Write the InsertPreorder function to insert node 6 into the tree using the Preorder- DFS traversal method.
    2) Write a function to display the tree using the Postorder - DFS traversal method.
"""

class Node:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None


def insertPreorder(node, value):
    if node is None:
        return Node(value)

    if node.left is None:
        node.left = Node(value)
        return True
    if node.right is None:
        node.right = Node(value)
        return True

    if insertPreorder(node.left, value):
        return True
    if insertPreorder(node.right, value):
        return True

    return False


def printPostorder(node):
    if node is None:
        return

    printPostorder(node.left)
    printPostorder(node.right)
    print(node.value, end=" ")


root = Node(2)
root.left = Node(3)
root.right = Node(4)
root.left.left = Node(5)

print("Original Tree (Postorder):")
printPostorder(root)

insertPreorder(root, 6)

print("\n\nTree after inserting 6 (Postorder):")
printPostorder(root)

