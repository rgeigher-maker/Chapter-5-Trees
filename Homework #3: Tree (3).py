"""
Given a Binary Search Tree (BST) as shown below. Use Python to implement the program including the following
requirements (any tree traversal algorithm can be used):
    1) Write a function to input the tree values from the keyboard
    2) Sum of k largest elements in BST: Find Sum Of All Elements greater than or equal to Kth largest Element In BST.
    3) Write a function to print the values of the tree to the screen
"""

class Node:
    def __init__(self, key):
        self.val = key
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, root, key):
        if root is None:
            return Node(key)

        if key < root.val:
            root.left = self.insert(root.left, key)
        else:
            root.right = self.insert(root.right, key)
        return root

    def print_tree(self, root):
        if root:
            self.print_tree(root.left)
            print(root.val, end=" ")
            self.print_tree(root.right)

    def sum_k(self, root, k):
        self.count = 0
        self.total_sum = 0

        def reverse_inorder(node):
            if not node or self.count >= k:
                return

            reverse_inorder(node.right)

            if self.count < k:
                self.count += 1
                self.total_sum += node.val

                reverse_inorder(node.left)

        reverse_inorder(root)
        return self.total_sum


if __name__ == "__main__":
    tree = BinarySearchTree()

    val_input = input("Enter the tree values separated by space: ")
    values = list(map(int, val_input.split()))

    for val in values:
        tree.root = tree.insert(tree.root, val)

    k_val = int(input("Enter the value of k: "))

    print("\nTree values (In-order):", end=" ")
    tree.print_tree(tree.root)

    result = tree.sum_k(tree.root, k_val)
    print(f"\nSum of the {k_val} largest elements: {result}")