"""
Given a Binary Search Tree as shown below. Use Python to implement the program including the following requirements
(any tree traversal algorithm can be used):
    1) Write a function to input the tree values from the keyboard
    2) Calculate the sum of the values of the tree nodes with the condition that those nodes are divisible by 5.
    3) Write a function to print the values of the tree to the screen
"""

class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key

def insert(root, key):
    if root is None:
        return Node(key)
    else:
        if root.val < key:
            root.right = insert(root.right, key)
        else:
            root.left = insert(root.left, key)
    return root

def createTree():
    user_Input = input("Please enter the tree values (note: separate the values by spaces): ").split()

    root = None
    for x in user_Input:
        root = insert(root, int(x))
    return root

def sum(root):
    if root is None:
        return 0

    current_val = 0
    if root.val % 5 == 0:
        current_val = root.val

    return current_val + sum(root.left) + sum(root.right)


def print_tree(root):
    if root:
        print_tree(root.left)
        print(root.val, end=" ")
        print_tree(root.right)


if __name__ == "__main__":
    my_tree = createTree()

    print("\nTree values (In-order traversal):")
    print_tree(my_tree)

    total = sum(my_tree)
    print(f"\nSum of nodes divisible by 5: {total}")