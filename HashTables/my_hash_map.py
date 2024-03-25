class MyHashMap:
    def __init__(self):
        """
        Initializes an object with an empty map
        """
        self.map = [[None]]
        self.length = 1

    def put(self, key: int, value: int) -> None:
        """
        Inserts a key: value pair into the map
        If they key already exists, update the correponding value
        """
        if key < self.length:
            self.map[key] = [value]
        else:
            self.map.append([None])
            self.map[key] = [value]
            self.length += 1

    def get(self, key: int) -> int:
        """
        Returns the value to which the specific key is mapped
        Returns -1 if the map contains no value for the key
        """
        if key < self.length and self.map[key] != [None]:
            return self.map[key][0]
        else:
            return -1

    def remove(self, key: int) -> None:
        """
        Removes the key and its corresponding value if the map contains the mapping for the key
        """
        if self.map[key]:
            self.map[key] = [None]


# Your MyHashMap object will be instantiated and called as such:
obj = MyHashMap()
obj.put(1, 1)
obj.put(2, 4)
print(obj.map)
print(obj.get(2))
# obj.remove(key)
