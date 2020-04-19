class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key

def is_BST(tree_root):

    stack = []
    stack.append(tree_root)

    result = True

    while len(stack > 0):

        n = stack.pop()

        if n.left:
            if n.left.key > n.key:
                result = False
                break
            stack.append(n.left)

        if n.right:
            if n.right.key < n.key:
                result = False
                break
            stack.append(n.right)

    return result
