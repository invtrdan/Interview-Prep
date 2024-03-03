# Creating an Array

import array as arr

a = arr.array("i", [1, 3, 4])  # creaing an integer array

b = arr.array("d", [1.2, 2.3, 3.4])  # creating a floating point array

# Adding Elements to an Array

a.insert(1, 2)  # Added Elements at any given index - .insert(index, elements)
print(a)