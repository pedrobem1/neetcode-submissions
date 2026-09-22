class ListNode:

    def __init__(self, key=0, val=0):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None


class LRUCache:

    def __init__(self, capacity: int):
        self.capacity = capacity
        self.cache = {}

        self.least_used = ListNode()
        self.most_used = ListNode()

        self.least_used.next = self.most_used
        self.most_used.prev = self.least_used

    def used(self, key):
        node = self.cache[key]
        self.remove(node)
        self.insert(node)

    def remove(self,node):
        nxt = node.next
        prev = node.prev
        nxt.prev = prev
        prev.next = nxt

    def insert(self,node):
        prev = self.most_used.prev

        prev.next = node
        node.prev = prev
        node.next = self.most_used
        self.most_used.prev = node


    def get(self, key: int) -> int:
        if key in self.cache:
            self.used(key)
            return self.cache[key].val
        return -1

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.cache[key].val = value
            self.used(key)
        else:
            if len(self.cache) == self.capacity:
                lru_node = self.least_used.next
                self.remove(lru_node)
                del self.cache[lru_node.key]
            self.cache[key] = ListNode(key,value)
            self.insert(self.cache[key])
        














