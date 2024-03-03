"""
Array
    - a collection of items (of the same type) stored at contiguous memory locations

"""

# Creating an Array

import array as arr

a = arr.array("i", [1, 3, 4])  # creaing an integer array

b = arr.array("d", [1.2, 2.3, 3.4])  # creating a floating point array

"""
Complexities of Creating an Array
    - Time Complexity: O(1)
    - Space Complexity: O(n)
"""

# Adding Elements to an Array

a.insert(1, 2)  # Added Elements at any given index - .insert(index, elements)

b.append(4.5)  # Adding Elements to the end of an array - .append(element)

"""
Complexities of intersting elements into an Array
    - Time Complexity: O(1) or O(n)
        O(1) for inserting elements at the end of the array
        O(n) for inserting elemets anywhere else in the array
"""

# Accessing Elements in an Array

first_element = f"The first elemet in the integer array is:", a[0]

"""
Complexities of accessing elements in Arrays
    - Time Complexity: O(1)
    - Space Complexity: O(1)
"""

# Removing Elements from the Array

a.remove(4)  # remove a single element. (Error if the element does not exist)

last_element = a.pop()  # remove and return the last element in the array

first_element = a.pop(0)  # remove and return element at index

"""
Complexities of Removing elemnts in Arrays
    - Time Complexity: O(1) or O(1)
        O(1) for removing elements at the end of the array
        O(n) for removing elements anywhere else
    - Space Complexity: O(1)
"""

# Slicing an Array
# (end index is exclusive)

c = arr.array("i", [0, 1, 2, 3, 4, 5])
print(c)

test_arr = c[:4]  # access elements from the beginning to a range use [:end]

test_arr = c[:-1]  # access elements from end index (from right to left) [:-index]

test_arr = c[1:]  # access elements from specific index to end [index:]

test_arr = c[1:4]  # access elements within a range [start_index:end_index]

test_arr = c[:]  # access an entire array [:]

test_arr = c[::-1]  # array in reverse order [::-1]

"""
Complexities of Slicing an Array
    Time Complexity: O(k) where k is the number of elements in the slice
    Space Complexity: O(k) because the amount of allocated memory os proportional to the # of elements
"""

# Searching for elements in an Array (first occurence)

d = arr.array("i", [1, 2, 3, 2])

first_two = d.index(2)

"""
Complexities for Searching an Array
    Time Complexity: O(n)
    Auxiliary Space: O(1)
"""

# Updating Elements in an Array

e = arr.array("d", [1.1, 1.2, 2.4, 3.4])

e[2] = 2.3

"""
Complexities for Updating elements in an Array
    Time Complexity: O(n)
    Auxiliary Space: O(1)
"""

# Counting elements in an Array

f = arr.array("i", [1, 2, 3, 4, 4, 2, 2, 2, 3])

num_four = f.count(4)

"""
Complexities for counting elements in an Array
    Time Complexity: O(n)
    Auxiliary_Space: O(1)
"""

# Reversing Elements in an Array

g = arr.array("i", [0, 1, 2, 3, 4, 5])

g.reverse()

"""
Complexities for Reversing an Array
    Time Complexity: O(n)
    auxiliary Space: O(1)
"""
