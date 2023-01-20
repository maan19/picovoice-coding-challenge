"""
Design a LRU cache with capacity N and it stores most recently used N Book objects by isbn as key"""

class Node:
    def __init__(self, key, value):
        self.key = key
        self.value = value
        self.prev = None
        self.next = None

class LRUCache:
    def __init__(self, capacity):
        self.capacity = capacity
        self.cache = {}
        self.left = Node(0,0)
        self.right = Node(0, 0)
        self.left.next = self.right
        self.right.prev = self.left
        #implement locks
    
    #insert into right in list
    def insert_right_list(self, node):
        prev = self.right.prev
        node.prev = prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
    
    #delete least recently used from left in list
    def delete_node_list(self, node):
       prev = node.prev
       next = node.next
       del node
       prev.next = next
       next.prev = prev

    def get(self, key):
        if key in self.cache:
            #update the MRU list
            node = Node(key,self.cache[key].value)
            self.insert_right_list(node)
            self.delete_node_list(self.cache[key])
            self.cache[key] = node
            return self.cache[key].value
        else:
            return None
    
    def put(self, key, value):
        if key in self.cache:
            #update the MRU list
            node = Node(key,value)
            self.delete_node_list(self.cache[key])
            self.insert_right_list(node)
            self.cache[key] = node
            return
        else:
            if len(self.cache) == self.capacity:
                #Pop the least recently accessed element
                lru = self.left.next
                self.delete_node_list(lru)
                del self.cache[lru.key]
            #We need to update the MRU list with this item.
            node = Node(key, value)
            self.cache[key] = node
            self.insert_right_list(node)
