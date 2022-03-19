# Inorder: Left Root Right
# 1. Go to the left node, and perform a recursive inorder traversal.
# 2. Execute the necessary action on the node.
# 3. Go to the right node, and perform a recursive inorder traversal.

# Tree structure:
#               50
#             /    \
#           20      53
#          /  \    /  \
#         11  22  52  78
 
class BinarySearchTreeNode:
    def __init__(self, data):
        self.data = data
        self.left = None
        self.right = None

def inorder_tree_traversal(root, result = []):
    if root is None:
        return
    inorder_tree_traversal(root.left, result)
    result.append(root.data)
    inorder_tree_traversal(root.right, result)
    return result

def insert_data(root, value):
    if root is None:
        root = BinarySearchTreeNode(value)
        return root
    
    if value < root.data:
        root.left = insert_data(root.left, value)
    else:
        root.right = insert_data(root.right, value)

    return root

if __name__ == "__main__":
    root = insert_data(None, 50)
    insert_data(root, 20)
    insert_data(root, 53)
    insert_data(root, 11)
    insert_data(root, 22)
    insert_data(root, 52)
    insert_data(root, 78)
    print("Inorder Traversal: ", inorder_tree_traversal(root))