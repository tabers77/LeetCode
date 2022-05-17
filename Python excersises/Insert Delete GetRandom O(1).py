import random


class RandomizedSet:

    def __init__(self):
        self.value_container = []

    def insert(self, val: int) -> bool:
        if val not in self.value_container:
            self.value_container.append(val)
            return True
        else:
            return False

    def remove(self, val: int) -> bool:
        if val in self.value_container:
            self.value_container.remove(val)
            return True
        else:
            return False

    def getRandom(self) -> int:
        return random.choice(self.value_container)

# Your RandomizedSet object will be instantiated and called as such:

obj = RandomizedSet()
param_1 = obj.insert(1)
param_2 = obj.insert(2)
param_3 = obj.remove(2)
param_3 = obj.getRandom()
