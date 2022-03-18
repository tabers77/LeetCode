class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.key_dict = {}

    def get(self, key: int) -> int:

        if key in self.key_dict.keys():
            return key
        else:
            return -1

    def put(self, key: int, value: int) -> None:

        if len(self.key_dict) == self.capacity:
            self.key_dict.popitem()
            self.key_dict[key] = value
            print(f'current cache: {self.key_dict}')
        else:
            self.key_dict[key] = value
            print(f'current cache: {self.key_dict}')




ob = LRUCache(2)
ob.put(1, 1)
ob.put(2, 2)
print(ob.get(1))
ob.put(3, 3)
print(ob.get(3))
ob.put(4, 4)