class BinaryTree:
    def __init__(self, value: int):
        self.value = value
        self.left = None
        self.right = None

def print_binary_tree(tree):
    if tree is not None:
        print(tree.value, end=" ")
        print_binary_tree(tree.left)
        print_binary_tree(tree.right)

def invert_binary_tree(tree) -> BinaryTree:
    if tree is None:
        return None

    stack = [tree]
    while stack:
        node = stack.pop()
        node.left, node.right = node.right, node.left
        if node.left:
            stack.append(node.left)
        if node.right:
            stack.append(node.right)

    return tree

root = BinaryTree(1)
root.left = BinaryTree(2)
root.right = BinaryTree(3)
root.left.left = BinaryTree(4)
root.left.right = BinaryTree(5)
root.right.left = BinaryTree(6)
root.right.right = BinaryTree(7)

print("Given binary tree:")
print_binary_tree(root)
print("\n")

inverted_tree = invert_binary_tree(root)

print("Inverted binary tree:")
print_binary_tree(inverted_tree)
