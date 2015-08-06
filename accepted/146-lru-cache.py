# https://leetcode.com/problems/lru-cache/
class LRUNode:
    def __init__(self, key, val):
        self.key = key
        self.val = val
        self.prev = None
        self.next = None

class LRUCache:
    # @param capacity, an integer
    def __init__(self, capacity):
        self.head = LRUNode(None, None)
        self.end = LRUNode(None, None)
        self.end.prev = self.head
        self.head.next = self.end
        
        self.capacity = capacity
        self.table = {}

    # @return an integer
    def get(self, key):
        if key not in self.table:
            return -1
        
        found = self.table[key]
        self.remove(found)
        self.add(found)
        
        return found.val

    # @param key, an integer
    # @param value, an integer
    # @return nothing
    def set(self, key, value):
        if key not in self.table:
            node = LRUNode(key, value)
            
            if len(self.table) == self.capacity:
                del self.table[self.end.prev.key]
                self.remove(self.end.prev)
            
            self.add(node)
            self.table[key] = node
        else:
            self.get(key)
            self.table[key].val = value
        
    def remove(self, node):
        node.prev.next = node.next
        node.next.prev = node.prev
        
    def add(self, node):
        node.next = self.head.next
        node.next.prev = node
        self.head.next = node
        node.prev = self.head
