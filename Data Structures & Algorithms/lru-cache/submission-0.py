class Node:
    def __init__(self,key,val):
        self.val = val
        self.key = key
        self.prev = None
        self.next = None
class LRUCache:
    def remove(self,Node):
        prev = Node.prev
        nxt = Node.next
        prev.next = nxt
        nxt.prev = prev
    def insert(self,Node):
        prev = self.tail.prev
        prev.next = Node
        Node.prev = prev

        Node.next = self.tail
        self.tail.prev = Node
    def __init__(self, capacity: int):
        self.cache = {}
        self.cap = capacity
        self.head = Node(0,0)
        self.tail = Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head
    def get(self, key: int) -> int:
        if key not in self.cache:
            return -1
        self.remove(self.cache[key])
        self.insert(self.cache[key])
        return self.cache[key].val

    def put(self, key: int, value: int) -> None:
        if key in self.cache:
            self.remove(self.cache[key])
        self.cache[key] = Node(key,value)
        self.insert(self.cache[key])
        if len(self.cache) > self.cap:
            lru = self.head.next
            self.remove(lru)
            del[self.cache[lru.key]]

        
        
        
