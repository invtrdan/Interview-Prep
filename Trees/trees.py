"""
Binary Tree Data Structure
    - Hierarchical data structure in which each node has at most 2 children, referred to as the left child and the right child.
    
Node
Each Node in a Binary Tree Contains:
    - Data
    - Pointer to the left child
    - Pointer to the right child
"""


# Binary Tree Node
class Node:
    def __init__(self, key):
        self.left = None
        self.right = None
        self.val = key


"""
                                Degree (# Children)    Height
root      1         Level 0            2                 0
         / \       
        2   3       Level 1            2                 1
       / \ / \ 
      4  5 6  7     Level 2            0                 2
     
Properties of a Binary Tree
    - The maximum number of nodes at level L of a binary tree is 2^L
        Level 0 - 1
        Level 1 - 2
        Level 2 - 4 ...
    - The maximum number of node in a binary tree of height h is 2^h -1
        Height = 1 -> 1
        Height = 1 -> 3 ...
"""

"""
Types of Binary Trees
    - Full Binary Tree: every node has 0 or 2 children
    - Degenerate/Pathological Binary Tree: Every internal node has one child
    - Skewed Binary Tree: Degenerate tree in which the tree is either dominated by the left nodes or the right nodes.
        Left-Skewed Binary Tree / Right-Skewed Binary Tree
        
    - Complete Binary Tree: all levels are complete except the last level
    - Perfect Binary Tree: all nodes have 2 children and all leaf nodes are on the same level
    - Balanced Binary Tree: height of the tree is O(Log n)
"""

"""
Basic Operations on Binary Trees
    - Inserting an element
    - Removing an element
    - Searching for an element
    - Deletion for an element
    - Traversing an element
"""

"""
Auxiliary Operations on Binary Trees:
    - Find the height of the tree
    - Find the level of the tree
    - Find the size of the entire tree
"""


# Array Implementation
tree = [None] * 10
print(tree)


def root(key):
    if tree[0] != None:
        print("Tree already has a root")
    else:
        tree[0] = key


def set_left(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 1, ", no parent found")
    else:
        tree[(parent * 2) + 1] = key


def set_right(key, parent):
    if tree[parent] == None:
        print("Can't set child at", (parent * 2) + 2, ", no parent found")
    else:
        tree[(parent * 2) + 2] = key


def print_tree():
    for i in range(10):
        if tree[i] != None:
            print(tree[i], end="")
        else:
            print("-", end="")
    print()


root("A")
set_left("B", 0)
set_right("C", 0)
set_left("D", 1)
set_right("E", 1)
set_right("F", 2)
print_tree()
