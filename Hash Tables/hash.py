"""
Hash Table
    - A hash table is a data structure that allows for quick insertion, deletion and retrieval of data. 
    - It works by using a hash function to map a key to an index in an array.
    
    Key     ->     Hash Function     ->     Index, Value
    
Separate Chaining
    - A technique used to handle collisions in a hash table.
    - When 2 ore more keys map to the same index in the array, we store them in a LinkedList at tat index.
    - This allows us to be able to store multiple values at the same index and still be able to retrieve them using their key.
"""

"""
Node Class 
    - Each node will contain a key: value pair, as well as a pointer to the next Node in the LinkedList
"""


class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.next = None


"""
Hash Table Class
    - Contains the array that will hold the LinkedList, as well as methods to insert, retrieve, and delete data from the hash table
"""


class HashTable:
    def __init__(self, capacity):  # Initialize the hash table with a given capacity
        self.capacity = capacity
        self.size = 0
        self.table = [None] * capacity

    def _hash(self, key):
        """
        Takes a key and returns an index index in the array where the key-value pair should be stored
        """
        return hash(key) % self.capacity

    def insert(self, key, value):
        """
        Insert a key: value pair into the HashTable
        """
        index = self._hash(key)

        # If there is no LinkedList at that index
        if self.table[index] is None:
            # Create a new Node with the key: value pair and sets it as the head of the LinkedList
            self.table[index] = Node(key, value)
            self.size += 1

        # If there is a LinkedList at the index
        else:
            # Iterate through the LinkedList until the last Node is found or the key already exists
            current = self.table[index]
            while current:
                # update the value
                if current.key == key:
                    current.value = value
                    return
                current = current.next
            new_node = Node(key, value)
            new_node.next = self.table[index]
            self.table[index] = new_node
            self.size += 1

    def search(self, key):
        """
        Retrieves the value associated with a given key
        """
        # Get the index where the key: value pair should be stored using the _hash method
        index = self._hash(key)

        # Search the LinkedList at that index for the key
        current = self.table[index]
        while current:
            if current.key == key:
                return current.value
            current = current.next
        raise KeyError(key)  # If the key is not found

    def remove(self, key):
        """
        Removes a key: value pair from a HashTable
        """
        # Get the index where the key: valye pair should be stored using the _hash method
        index = self._hash(key)

        # Search the LinkedList at that index for the key
        previous = None
        current = self.table[index]
        while current:
            if current.key == key:
                if previous:
                    previous.next = current.next
                else:
                    self.table[index] = current.next
                self.size -= 1
                return
            previous = current
            current = current.next
        raise KeyError(key)

    def __str__(self):
        """
        Returns a string representation of the HashTable
        """
        elements = []
        for i in range(self.capacity):
            current = self.table[i]
            while current:
                elements.append((current.key, current.value))
                current = current.next
        return str(elements)


# Driver code
if __name__ == "__main__":
    # Create a hash table with
    # a capacity of 5
    ht = HashTable(5)

    # Add some key-value pairs
    # to the hash table
    ht.insert("apple", 3)
    ht.insert("banana", 2)
    ht.insert("cherry", 5)

    # Check if the hash table
    # contains a key
    print("apple" in ht)  # True
    print("durian" in ht)  # False

    # Get the value for a key
    print(ht.search("banana"))  # 2

    # Update the value for a key
    ht.insert("banana", 4)
    print(ht.search("banana"))  # 4

    ht.remove("apple")
    # Check the size of the hash table
    print(len(ht))  # 3
