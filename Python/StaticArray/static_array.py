from typing import Optional


class StaticArray:
    def __init__(self, capacity: int):
        self.array = [0] * capacity
        self.capacity = capacity
        self.size = 0

    # O(1)
    def insertEnd(self, value: int):
        if self.size < self.capacity:
            self.array[self.size] = value
            self.size += 1

    # O(n)
    def insert(self, index: int, value: int):
        if self.size < self.capacity and 0 <= index < self.size + 1:
            for i in range(self.size, index, -1):
                self.array[i] = self.array[i - 1]
            self.array[index] = value
            self.size += 1

    def get(self, index: int) -> Optional[int]:
        if 0 <= index < self.size:
            return self.array[index]

    def update(self, index: int, value: int):
        if 0 <= index < self.size:
            self.array[index] = value

    # O(1)
    def removeEnd(self):
        if self.size > 0:
            self.array[self.size - 1] = 0
            self.size -= 1

    # O(n)
    def remove(self, index: int):
        if 0 <= index < self.size:
            for i in range(index, self.size - 1):
                self.array[i] = self.array[i + 1]
            self.array[self.size - 1] = 0
            self.size -= 1

    def __str__(self):
        return '[' + ', '.join([str(n) for n in self.array]) + ']'

