"""
LRU cache with capacity N and it stores most recently used N Book objects by isbn as key
To keep track of most recently used books, we use LRU cache with doubly linked list
Each time a new book is added to the cache, we add it to the right/beginning of the list, as MRU item
Similarly, when a book is accessed, we add it to the right/beginning of the list, as MRU item
Adding elements to full cache will remove the least recently accessed item"""
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
    
    #insert into right in linked list
    def insert_right_list(self, node):
        prev = self.right.prev
        node.prev = prev
        prev.next = node
        self.right.prev = node
        node.next = self.right
    
    #delete least recently used from left in linked list
    def delete_node_list(self, node):
       prev = node.prev
       next = node.next
       del node
       prev.next = next
       next.prev = prev

    #get element by key
    #get operation will move to the right/beginning of the list as most recently accessed item
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
    
    #put element into cache
    #if the cache is full, remove the least recently accessed item
    #if key already exists, update the value
    #put operation will make the elememt to the right/beginning of the list as most recently accessed item
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
