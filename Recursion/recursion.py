"""
Recursion
    - Recursion is the process a procedure goes through when one of the steps of the procedure involves invoking the procedure itself.
"""


def factorial(n):
    if n == 1:
        return n
    else:
        return n * factorial(n - 1)
