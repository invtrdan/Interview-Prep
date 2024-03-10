"""
Binary Tree Traversals

            1  <-- root
           / \      
          2   3
         / \ / \      
        4  5 6  7  <-- leaf nodes

Tree Traversal Algorithms can be classified broadly into 2 categories:

    - Depth-First Search (DFS) Algorithms
        - Preorder Traversal (current -> left child -> right child) 1-2-4-5-3-6-7
        - Inorder Traversal (left subtree -> current node -> right subtree) 4-2-5-1-6-3-7
        - Postorder Traversal (left subtree -> right subtree -> current) 4-5-2-6-7-3-1
        
    - Breadth-First Search (BFS) Algorithms
        - Level Order Traversal (level-by-level and left-to-right) 1-2-3-4-5-6-7
        
"""


class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


# Preorder Traversal
def printPreOrder(root):
    if root:
        print(root.val)
        printPreOrder(root.left)
        printPreOrder(root.right)


# Inorder Traversal O(N)
def printInOrder(root):
    if root:
        printInOrder(root.left)
        print(root.val, end=" ")
        printInOrder(root.right)


# Postorder Traversal
def printPostOrder(root):
    if root:
        printPostOrder(root.left)
        printPostOrder(root.right)
        print(root, end=" ")
