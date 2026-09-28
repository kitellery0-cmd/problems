class Node:
    def __init__(self, key, val):
        self.key, self.val = key, val
        self.prev = self.next = None

class LRUCache:
    def __init__(self, capacity: int):
        self.cap = capacity
        self.cache = {}  # map key to node

        self.head, self.tail = Node(0,0), Node(0,0)
        self.head.next = self.tail
        self.tail.prev = self.head


    def get(self, key: int) -> int:
        node = self.cache.get(key)
        if not node:
            return -1
        self.remove(node)
        self.insert(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        node = self.cache.get(key)
        if node:
            node.val = value
            self.remove(node)
        else:
            node = self.cache[key] = Node(key, value)

        self.insert(node)
        if len(self.cache) > self.cap:
            lru = self.tail.prev
            self.remove(lru)
            self.cache.pop(lru.key)

    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev

    def insert(self, node):
        nxt = self.head.next
        node.next = nxt
        node.prev = self.head
        self.head.next = node
        nxt.prev = node


# ordered dict is perfect here too, but this shows better understanding
# of the data structures at play.
