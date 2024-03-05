"""
Stack
    - a linear data structure 
    - LIFO / FILO
        - insertion (push) and deletion (pop) happen on the same end
"""
"""
Stack Functions:
    empty() - returns whether the stack is empty
        Time Complexity: O(1)
    size() - returns the size of the stack
        Time Complexity: O(1)
    top() / peak() - returns a reference to the topmost element of the stack
        Time Complexity: O(1)
    push(a) - inserts the element 'a' at the top of the stack
        Time Complexity: O(1)
    pop() - deletes the topmost element of the stack
        Time Complexity: O(1)
"""

# Stack Implementation using a List
# append(), pop()

print("Stack Implementation using a List")

stack = []

stack.append("a")
stack.append("b")
stack.append("c")

print(stack)

print("Elements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)

print()

# Stack Implementation using collections.deque
# append(), pop()

print("Stack Implementation using collections.deque")

from collections import deque

stack = deque()

stack.append("a")
stack.append("b")
stack.append("c")

print(stack)

print("Elements popped from stack:")
print(stack.pop())
print(stack.pop())
print(stack.pop())

print(stack)

print()
