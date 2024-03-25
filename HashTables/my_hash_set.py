class MyHashSet:
    def __init__(self):
        self.size = 0
        self.hash_table = [[None]]

    def add(self, key: int) -> None:
        """
        Inserts the value key into the HashSet
        """
        self.size += 1
        self.hash_table.append([None])
        index = key % self.size
        if self.hash_table[index] == [None]:
            self.hash_table[index] = [key]
            return
        while True:
            index += 1
            if index > self.size:
                index = 0
            if self.hash_table[index] == [None]:
                self.hash_table[index] = [key]
                return

    def remove(self, key: int) -> None:
        """
        Removes the value key in the HashSet.
        If key does not exist in the HashSet, do nothing.
        """
        index = key % self.size
        if self.hash_table[index] == [key]:
            self.hash_table[index] = [None]
        index2 = index + 1
        while True:
            if index2 == index:
                return
            if index2 >= self.size:
                index2 = 0
            if self.hash_table[index2] == [key]:
                self.hash_table[index2] = [None]
            index2 += 1

    def contains(self, key: int) -> bool:
        """
        Returnd whether the value key exists in the HashSet or not
        """
        index = key % self.size
        if self.hash_table[index] == [key]:
            return True
        index2 = index + 1
        while True:
            if index2 == index:
                return False
            if index2 >= self.size:
                index2 = 0
            if self.hash_table[index2] == [key]:
                return True
            index2 += 1


# obj = MyHashSet()
# print(obj.hash_table)
# obj.add(1)
# print(obj.hash_table)
# obj.add(2)
# print(obj.hash_table)
# obj.add(1)
# print(obj.hash_table)
# obj.remove(1)
# print(obj.hash_table)
# param_3 = obj.contains(1)
# print(param_3)

myHashSet = MyHashSet()
myHashSet.add(1)
print(myHashSet.hash_table)
myHashSet.add(2)
print(myHashSet.hash_table)
print(myHashSet.contains(1))
print(myHashSet.contains(3))
myHashSet.add(2)
print(myHashSet.hash_table)
print(myHashSet.contains(2))
myHashSet.remove(2)
print(myHashSet.hash_table)
print(myHashSet.contains(2))
