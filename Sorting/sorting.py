"""
Sorting
    - An arrangement of data in a certain order (usually ascending or descending).
    
Sorting Techniques
    - Bubble Sort
    - Selection Sort
    - Insertion Sort
"""


def BubbleSort(arr):
    """
    - Repeatedly compares 2 adjacent elements and swaps them if they are in the wrong order.
    - Complexity: O(n^2), Best Case: O(n) if already sorted
    """
    n = len(arr)
    for i in range(n):
        for j in range(0, n - i - 1):
            if arr[j] > arr[j + 1]:
                arr[j], arr[j + 1] = arr[j + 1], arr[j]


def SelectionSort(arr, size):
    """
    - Repeatedly finds the minimum element and sort it in order
    - Time Complexity: O(n^2)
    """
    for s in range(size):
        min_idx = s
        for i in range(s + 1, size):
            if arr[i] < arr[min_idx]:
                min_idx = i
        (arr[s], arr[min_idx]) = (arr[min_idx], arr[s])


def InsertionSort(list1):
    """
    - Maintaining a sub-array that is always sorted.
    - Values from the unsorted part of the array are placed in the correct position in the sorted part
    - Time Complexity: O(n^2)
    """
    for i in range(1, len(list1)):
        a = list1[i]
        j = i - 1
        while j >= 0 and a < list1[j]:
            list1[j + 1] = list1[j]
            j -= 1
        list1[j + 1] = a
    return list1
