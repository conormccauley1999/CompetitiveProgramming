INF = 10 ** 12

class LRUCache:

    def __init__(self, capacity: int):
        self.time = 0
        self.cap = capacity
        self.dict = {}

    def get(self, key: int) -> int:
        if key not in self.dict:
            return -1
        self.time += 1
        self.dict[key][1] = self.time
        return self.dict[key][0]

    def put(self, key: int, value: int) -> None:
        if key not in self.dict and len(self.dict) == self.cap:
            mn_k, mn = -1, INF
            for k in self.dict:
                if self.dict[k][1] < mn:
                    mn = self.dict[k][1]
                    mn_k = k
            del self.dict[mn_k]
        self.time += 1
        self.dict[key] = [value, self.time]


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)