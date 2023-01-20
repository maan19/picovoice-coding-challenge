import unittest
from cache import LRUCache
from book import Book

class TestLruCache(unittest.TestCase):
    #Set up is not being used, but could be in future.
    @classmethod
    def setUpClass(self):
        #self.cache = LRUCache(4)
        pass
    def initialize_cache(self,cache):
        cache.put("1", Book("1","Good book for Go lang","Jagdeep","English"))
        cache.put("2", Book("2","Good book for Python","Jagdeep", "English"))
        cache.put("3", Book("3","Good book for Deep Learning","Jagdeep", "English"))
        cache.put("4", Book("4","Good book for Statistics","Jagdeep", "English"))
    
    def test_normal_get_hit(self):
        cache = LRUCache(4)
        book = Book("1","Good book for Go lang","Jagdeep","English")
        self.initialize_cache(cache)
        self.assertEqual(cache.get("1"), book)

    def test_normal_get_miss(self):
        cache = LRUCache(4)
        self.assertEqual(cache.get("1001"), None)
    
    #test to check if getting an element makes that element a most recently used element
    def test_get_causes_element_to_be_mru_linkedlist(self):
        cache = LRUCache(4)
        self.initialize_cache(cache)
        book = Book("3","Good book for Deep Learning","Jagdeep", "English")
        self.assertEqual(cache.get("3"),book)
        self.assertEqual(cache.right.prev.key, "3")
        self.assertEqual(cache.left.next.key, "1")
        self.assertEqual(len(cache.cache), 4)
    
    #test to check if putting an existing element works, it should also make that element mru in cache
    def test_put_existing_element(self):
        cache = LRUCache(4)
        self.initialize_cache(cache)
        book = Book("3","Good book for Deep Learning","Jagdeep", "English")
        cache.put("3", book)
        self.assertEqual(cache.get("3"), book)
        self.assertEqual(cache.right.prev.key, "3")
        self.assertEqual(cache.left.next.key, "1")
    
    #test to check if putting an existing key with different value works, it should also make that element mru in cache
    def test_put_existing_element_but_new_value(self):
        cache = LRUCache(4)
        self.initialize_cache(cache)
        book = Book("3","Good book for Deep Learning","Jagdeep", "Punjabi")
        cache.put("3", book)
        self.assertEqual(cache.get("3"), book)
        self.assertEqual(cache.right.prev.key, "3")
        self.assertEqual(cache.left.next.key, "1")
    
    #test to check if adding element when cache is full removes the least recently used element.
    def test_put_on_full_cache(self):
        cache = LRUCache(4)
        self.initialize_cache(cache)
        book = Book("5","Good book for Computer Vision","Jagdeep", "English")
        cache.put("5", book)
        self.assertEqual(cache.right.prev.key, "5")
        self.assertEqual(cache.left.next.key, "2")
        self.assertEqual(cache.get("5"), book)
        self.assertEqual(cache.get("1"), None)
        
    

unittest.main()


