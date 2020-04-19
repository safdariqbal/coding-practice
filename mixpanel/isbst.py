class Node:

    def __init__(self, key):
        self.left = None
        self.right = None
        self.key = key
        self.data = None

def is_BST(tree_root):

    stack = []
    tree_root.data = (-(2**31),2**31)
    stack.append(tree_root)

    result = True

    while len(stack > 0):

        n = stack.pop()
        if not (n.key > n.data[0] and n.key < n.data[1]):
            result = False
            break

        if n.left:
            n.left.data = (n.data[0], n.key)
            stack.append(n.left)

        if n.right:
            n.right.data = (n.key, n.data[1])
            stack.append(n.right)

    return result

def is_BST2(tree_root):
    return is_BST2_aux(tree_root, -(2**31), 2**31)

def is_BST2_aux(node, min_key, max_key):
    if node == None:
        return True
    if node.key < min_key or node > max_key:
        return False
   
    result = True
    if node.left:
        result &= is_BST2_aux(node.left, min_key, node.key)
    if node.right:
        result &= is_BST2_aux(node.right, node.key, max_key)

    return result


